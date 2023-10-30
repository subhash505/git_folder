import pandas as pd
csv2_df = pd.read_csv(r"C:\Users\SubhashSharma\Desktop\subhash_practice_demo\s1test.csv")
csv1_df = pd.read_csv(r"C:\Users\SubhashSharma\Desktop\subhash_practice_demo\s2_test.csv")
# for index, row in csv2_df.iterrows():
#     roll_value = row['Custodian Acct']
#     matching_row = csv1_df[csv1_df['Custodian Acct'] == roll_value]
#     if not matching_row.empty:
#         csv1_df = pd.concat([csv1_df, matching_row], ignore_index=True)
# csv1_df.to_csv('file1.csv', index=False)
# print(csv1_df)

unique_roll_values = set()
for index, row in csv2_df.iterrows():
    roll_value = row['Custodian Acct']
    if roll_value not in unique_roll_values:
        unique_roll_values.add(roll_value)
        matching_row = csv1_df[csv1_df['Custodian Acct'] == roll_value]
        if not matching_row.empty:
            csv1_df = pd.concat([csv1_df, matching_row], ignore_index=True)
csv1_df.to_csv('file1.csv', index=False)
print(csv1_df)