import pandas as pd
import numpy as np


df = pd.read_csv(r"C:\Users\SubhashSharma\Desktop\subhash_practice_demo\s1test.csv")
df1 = pd.read_csv(r"C:\Users\SubhashSharma\Desktop\subhash_practice_demo\s2_test.csv")

list1 = df['Custodian Acct'].unique()
print(df.shape)

list2 = df1['Custodian Acct'].unique()
print(df1.shape)

count = 0
last_index =0
D_index = 0
l_count = 0
index_s1 = []
for count in range(len(list1)):
    for i in range(len(df['Custodian Acct'])):
        if list1[count] == df['Custodian Acct'][i]:
            D_index = i
            l_count+=1
    last_index = D_index
    print(f"last index of column Custodian Acct {last_index} for {list1[count]} and number of rows would be {l_count}")
    index_s1.append(last_index)
    D_index =0    
    l_count =0

count = 0
last_index =0
D_index = 0
l_count = 0
index_s2=[]
for count in range(len(list2)):
    for i in range(len(df1['Custodian Acct'])):
        if list2[count] == df1['Custodian Acct'][i]:
            D_index = i
            l_count+=1
    last_index = D_index
    print(f"last index of column Custodian Acct {last_index} for {list2[count]}and number of rows would be {l_count}")
    index_s2.append(last_index)
    D_index =0  
    l_count =0 

print(index_s1)
print(index_s2)

# count= 0
# count1 =0
# # first_index
# for i in range(len(index_s1)):
#     for k in range(len(df1['Custodian Acct'])):
#         if count == len(index_s2):
#             break
#         elif k == index_s2[count]:
#             for first_index in index_s1:
#                 df1.iloc[k]= df.loc[count1:first_index]
#                 count1 = first_index
                
#         count+=1

result1 = []
result2 = []
first = 0
second = 0
for l in range(0, len(index_s1)):    
    result1.append((first, index_s1[l]))
    first = index_s1[l]+1

for m in range(0, len(index_s2)):    
    result2.append((second, index_s2[m]))
    second = index_s2[m]+1


# df1.loc[4] = df.loc[0:2]
print(result1)
print(result2)

print(df1.shape)