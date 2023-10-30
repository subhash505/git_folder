import os
import logging
import email
from email.header import decode_header
import imaplib
import zipfile
import shutil
import argparse
import configparser
import sys
import pandas as pd
import openpyxl
import re
import datetime
from datetime import datetime


aro_home = os.environ['ARO_HOME']
target_folder_1 = os.path.join(aro_home, 'Input')
target_folder_2 = os.path.join(aro_home, 'mail_downloads')



#Provide your EMAIL_ADDRESS and APP_PASSWORD in ''
EMAIL_ADDRESS = "service.ezops@enfusion.com"
APP_PASSWORD = "xxzlidxxrlkepzun"


def add_custom_parser_args(parser):
    parser.add_argument('--File_Name', help=argparse.SUPPRESS,
                        required=True, dest='filename')
    parser.add_argument('--Zip_Password', help=argparse.SUPPRESS,
                        required=False, dest='zip_password')
    parser.add_argument('--From_Zip_File_Name', help=argparse.SUPPRESS,
                        required=False, dest='provided_filename')
    parser.add_argument('--Desired_Sheet_Name', help=argparse.SUPPRESS,
                        required=False, dest='desired_sheet_name')
    return parser

def gen_log():
    logFormatter = logging.Formatter(
        "%(asctime)s [%(threadName)-0.12s] [%(levelname)-0.15s]  %(message)s")
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.INFO)
    fileHandler = logging.FileHandler(
        "{}/{}.log".format(os.path.join(aro_home, 'log'), 'downlode_mail'))
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)


def download_attachment(msg, output_dirs, desired_filename, params):
    zip_password = params.zip_password
    zip_copy_filename = params.provided_filename
    desired_sheet_name = params.desired_sheet_name

    for part in msg.walk():
        if part.get_content_maintype() == "multipart":
            continue
        if part.get("Content-Disposition") is None:
            continue

        filename = part.get_filename()
        decoded_filename = decode_header(filename)[0][0]
        if isinstance(decoded_filename, bytes):
            filename = decoded_filename.decode()
        logging.info(f"Checking attachment: {filename}")
        if filename == desired_filename:
            for output_dir in output_dirs:
                filepath = os.path.join(output_dir, desired_filename)

                if os.path.exists(filepath):
                    logging.info(f"File {desired_filename} already exists in {output_dir}. Skipping download.")
                    continue

                logging.info(f"filepath : {filepath}")
                with open(filepath, "wb") as f:
                    f.write(part.get_payload(decode=True))
                logging.info(f"File downloaded: {desired_filename}")

                if filename.endswith('.zip'):
                    if zipfile.is_zipfile(filepath):
                        with zipfile.ZipFile(filepath, 'r') as zip_ref:
                            try:
                                if zip_password:
                                    logging.info(f"Zip File is Password Protected")
                                    zip_ref.extractall(path=target_folder_2, pwd=zip_password.encode('utf-8'))
                                else:
                                    zip_ref.extractall(path=target_folder_2)
                                logging.info(f"Extraction successful to {target_folder_2}")
                            except RuntimeError as e:
                                logging.info("Extraction failed:", e)

                        if desired_sheet_name:
                            excel_file_path = os.path.join(target_folder_2, zip_copy_filename)
                            wb = openpyxl.load_workbook(excel_file_path)
                            for sheet in wb.sheetnames:
                                if sheet != desired_sheet_name:
                                    del wb[sheet]
                            wb.save(excel_file_path)

                        source_path = os.path.join(target_folder_2, zip_copy_filename)
                        destination_path = os.path.join(target_folder_1, zip_copy_filename)
                        shutil.copy(source_path, destination_path)
                        logging.info(f"Copied {zip_copy_filename} to {target_folder_1}")
                        for file in os.listdir(target_folder_2):
                            source_file_path = os.path.join(target_folder_2, file)
                            os.remove(source_file_path)
                        if os.path.exists(filepath):
                            os.remove(filepath)
                    else:
                        logging.warning(f"Attachment {filename} is not a valid zip file.")
                else:
                    if os.path.abspath(filepath) != os.path.abspath(os.path.join(target_folder_1, filename)):
                        shutil.copy(filepath, os.path.join(target_folder_1, filename))
                        logging.info(f"Copied {filename} to {target_folder_1}")

                if os.path.exists(filepath):
                    os.remove(filepath)
                    logging.info("Deletion successful")


def main():
    gen_log()
    parser = argparse.ArgumentParser(
        description='Description: Enfusion Email Plugin', usage=argparse.SUPPRESS)
    parser = add_custom_parser_args(parser)
    params, extra = parser.parse_known_args()
    desired_filename = params.filename
    logging.info(f" desired filename {desired_filename}")
    if "..zip" in desired_filename:
        desired_filename = desired_filename[:-6]
        base_filename = '{}_{}_{}_{}.zip'.format(desired_filename, '{}', '{}', '{}')
        if datetime.now().month < 10:
            current_year, current_month, remaining_months = datetime.now().year, int('0'+ str(datetime.now().month)), 12 - datetime.now().month + 1 
        else:
            current_year, current_month, remaining_months = datetime.now().year, datetime.now().month, 12 - datetime.now().month + 1
        formatted_filenames = [base_filename.format(current_month + i, 30, current_year) for i in range(remaining_months)]
        logging.info(f"formatted filenames{formatted_filenames[0]}")
    logging.info(f" formated file name list {formatted_filenames}")
    with imaplib.IMAP4_SSL("imap.gmail.com") as server:
        server.login(EMAIL_ADDRESS, APP_PASSWORD)
        server.select("INBOX")
        _, message_ids = server.search(None, "ALL")
        message_ids = message_ids[0].split()
        for message_id in message_ids:
            _, msg_data = server.fetch(message_id, "(RFC822)")
            msg = email.message_from_bytes(msg_data[0][1])
            download_attachment(msg, [target_folder_1, target_folder_2], formatted_filenames[0], params)

if __name__ == "__main__":
    main()