import argparse
import os
import glob



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir",help="directory to find")
    parser.add_argument("--pattern",help="pattern to that file to find")

    # parser.add_argument("--number1", help="first number")
    # parser.add_argument("--number2", help="second number")
    # parser.add_argument("--operation", help="operation", choices=["add","subtract","multiply"])
    args = parser.parse_args()
    directory=str(args.dir)
    pattern=str(args.pattern)
    # print(args.dir)
    # print(args.pattern)
    my_tuple=(directory,"\*",pattern)
    file_path= "".join(my_tuple)
    print("file pattern that you are looking for",file_path)
    #print("this is the currect directory",os.chdir(directory))
    dir_path = os.path.dirname(os.path.realpath("plugin.py"))
    print("the file path of the current running plugin",dir_path)
    files=glob.glob(file_path)
    print("here are the file that you may be looking for",files)
    
    print("working directory is : ",os.getcwd())


if __name__=="__main__":
    print("you have to follow these insturction to run this plugin")
    print("make sure you have written the plugin command in correct format to run the plugin which should be")
    print("python plugin_filename.py --dir directory name --pattern /*.txt/*.csv/*.txt ")
    main()