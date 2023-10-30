import pandas as pd
import datetime
from datetime import datetime as dt
import re

desired_filename = 'Algt_algt_enfusion_.*.zip'
current_date = dt.now()
month = current_date.strftime('%m')
year = current_date.strftime('%Y')

desired_filename_list= []
for i in range(1, 13):
    # print(i)
    if '.*' in desired_filename:
        desired_filename = desired_filename.replace(".*", f"0{i}_30_{year}")    
    elif i>=10:
        desired_filename = re.sub(r'_\d{2}_\d{2}_\d{4}', f"_{i}_30_{year}", desired_filename)   
    else:
        desired_filename = re.sub(r'_0\d{1}_\d{2}_\d{4}', f"_0{i}_30_{year}", desired_filename)   
    desired_filename_list.append(desired_filename)
    # print(desired_filename)
print(desired_filename_list)




# desired_filename = 'Algt_algt_enfusion_.*.zip'
# for i in range(1,13):
#     s=dt.now().strftime(f"%{i}_30_%Y")
#     print(s)
#     desired_filename=desired_filename.replace(".*",s)
#     print(desired_filename)

# Previous_Date = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%m_%d_%Y")
# print ('Previous Date: ' + str(Previous_Date))