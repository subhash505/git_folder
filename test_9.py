import re
import pandas as pd
import numpy as np
import datetime 
from datetime import datetime as dt

df = pd.read_excel(r"C:\Users\SubhashSharma\Downloads\TB_Asset.xlsx",sheet_name= 0)
df1 = pd.read_excel(r"C:\Users\SubhashSharma\Downloads\TB_Asset.xlsx",sheet_name= 1)
df2 = pd.read_excel(r"C:\Users\SubhashSharma\Downloads\TB_Asset.xlsx",sheet_name= 2)

# print(df.columns)

# list_unique=df['ACCOUNT_DESCRIPTION'].unique()
# df_grouped = df.groupby('ACCOUNT_DESCRIPTION')
# df2 = pd.DataFrame()

# for desc, frame in df_grouped:
#     # print(desc, end="\n\n")
#     pass
# count =0
# print(list_unique)
# for i in list_unique:
#     # print(i)
#     for index1, row in df.iterrows():
#         if i in row['ACCOUNT_DESCRIPTION']:
#             count+= 1
#         if count > 1:
#             df=df.drop(index=[index1])
            
#         # print(row['ACCOUNT_DESCRIPTION'])        
#     count=0

unique_values = set()
df2['ACCOUNT_DESCRIPTION'] = df2['ACCOUNT_DESCRIPTION'].apply(lambda x: '' if x in unique_values else (unique_values.add(x) or x))
df_0 = df[[ 'ACCOUNT_TYPE','S1_AMOUNT', 'S2_AMOUNT', 'DIFFERENCE']]
print(df_0)


# print(unique_values)

# print(df2)
# df2= df_grouped
