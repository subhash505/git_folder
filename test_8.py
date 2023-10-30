# import re


# input_string = "Algt_algt_enfusion_11_30_2023.zip"


# new_date = "10_15_2023" 


# pattern = r'\d{2}_\d{2}_\d{4}'


# output_string = re.sub(pattern, new_date, input_string)

# print(output_string)


# from datetime import datetime

# fmt = '%Y-%m-%d %H:%M:%S'
# tstamp1 = datetime.strptime('2016-04-06 21:26:27', fmt)
# tstamp2 = datetime.strptime('2016-04-07 09:06:02', fmt)

# if tstamp1 > tstamp2:
#     td = tstamp1 - tstamp2
# else:
#     td = tstamp2 - tstamp1
# td_mins = int(round(td.total_seconds() / 60))

# print('The difference is approx. %s minutes' % td_mins)



import re

from datetime import datetime

 

# desired_filename = 'Algt_algt_enfusion'

# base_filename = '{}_{}_{}_{}.zip'.format(desired_filename, '{}', '{}', '{}')
 

# current_year = datetime.now().year

# current_month = datetime.now().month

# remaining_months = 12 - current_month + 1

 

# for i in range(remaining_months):

#     month = current_month + i

#     formatted_filename = base_filename.format(month, 30, current_year)

#     print(formatted_filename)
# from datetime import datetime

                    
desired_filename = 'Algt_algt_enfusion_..zip'
if "..zip" in desired_filename:
    desired_filename = desired_filename[:-6]
    print(desired_filename)
    base_filename = '{}_{}_{}_{}.zip'.format(desired_filename, '{}', '{}', '{}')
    if datetime.now().month < 10:
       current_year, current_month, remaining_months = datetime.now().year, int('0'+ str(datetime.now().month)), 12 - datetime.now().month + 1 
    else:
        current_year, current_month, remaining_months = datetime.now().year, datetime.now().month, 12 - datetime.now().month + 1
    formatted_filenames = [base_filename.format(current_month + i, 30, current_year) for i in range(remaining_months)]
    print(formatted_filenames)

# import os
# for root, dirs, files in os.walk(r'C:\Users\SubhashSharma\Desktop\enfusion_testing\welton_rec dev\Welton data VD 0926\Welton data VD 0926', topdown=False):
#     for i in files :
#         print(root)
#         print(dirs)
#         print(files)

#     for name in files:
#         os.remove(os.path.join(root, name))
#     for name in dirs:
#         os.rmdir(os.path.join(root, name))



# -----------------------------------------

# import os
# import datetime
# from datetime import datetime 
# desired_filename = 'subhash.sharma'
# base_filename = '{}_{}_{}_{}.zip'.format(desired_filename, '{}', '{}', '{}')

# current_year, current_month, remaining_months = datetime.now().year, datetime.now().month, 12 - datetime.now().month + 1
# formatted_file_name = [base_filename.format(current_month + i, 30, current_year) for i in range(remaining_months)]

# print(formatted_file_name)

# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
# for name, phone in table.items():
#     print(f'{name:10} ==> {phone:10d}')


# list1 = ['Sjoerd','Jack', 'Dcab','sharma']
# dict1= {}
# data = dict([(k, '') for k in range(2)])
# print(data)


# Write a Python script to add a key to a dictionary.

# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

Sample_Dictionary ={0: 10, 1: 20}
Sample_Dictionary2= {2:30}
Sample_Dictionary.update(Sample_Dictionary2)
print(f"expected result {Sample_Dictionary}")


from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d = Counter(d1) + Counter(d2)
# print(d)

#  Write a Python program to find the highest 3 values of corresponding keys in a dictionary.

d2 = {'a': 300, 'b': 200, 'd':400, 'e': 500, 'f': 600}
length = len(list(d2))
l= list(d2.values())
for i in range(length):
    if  i == (length-2):
        exit()
    else:
        print(l[i],l[i+1],l[i+2])

d2= sorted(d2)
d3 =sorted(d2.items(), key=lambda x: x[1], reverse=True)
print(d3[:3])


