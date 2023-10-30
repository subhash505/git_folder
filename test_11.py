import pandas as pd
import math 


df= pd.read_csv(r"C:\Users\SubhashSharma\Downloads\WT_UBS_UBSSwapSettlement_102023_005624.csv")
# df = pd.read_excel(r"C:\Users\SubhashSharma\Downloads\test_12.xlsx")

# pd.set_option('display.max_rows', 50)
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.width', 1000)
column_name_diff = 'Account_Id'
# m_column_name_diff = column_name_diff + " Acct"
m_column_name_diff = column_name_diff.replace("_", " ")
accounts_b = set(df[m_column_name_diff])
# print(accounts_b)
print(accounts_b)
for i in accounts_b:
    print(type(i))

if all(isinstance(x, str) or(isinstance(x, int))or (isinstance(x, float) and not math.isnan(x)) for x in accounts_b):
    print(accounts_b)
else:
    print("this is the blank file")
# print(df)
# print(df.empty)


list1=[('00190893',), ('003AOFWE',), ('003AONWE',), ('009ACLWE',), ('009WELT1',), ('009WELT2',), ('00N60371',), ('00N60372',), ('0242929',), ('02500190',), ('03385BLO0',), ('038CACMC3',), ('038CADSO9',), ('038CAE355',), ('038CDKMN8',), ('0425551',), ('0456AA2K5',), ('0456AA2K5',), ('0456ADHE7',), ('0456ADHE7',), ('04F118477',), ('04F118477',), ('04F141842',), ('04FA22107',), ('04FA30134',), ('04FY028J9',), ('04FY02FP7',), ('052BAKCC9',), ('052BAN7W5',), ('052BAOFC8',), ('052BAPCT1',), ('052BARB92',), ('054082441',), ('05408245',), ('054892849',), ('054960851',), ('059L4ALP0',), ('05ABAKCC0',), ('05ABAN7W6',), ('05ABAPCT2',), ('0617865U9',), ('0617865U',), ('0617884V4',), ('0617884V',), ('06296356',), ('062963574',), ('06296357',), ('062BWAGM9',), ('06500787',), ('065040040',), ('06504004',), ('06523347',), ('06523348',), ('06543196',), ('065NAAS74',), ('06733837',), ('07570577',), ('0CM8459',), ('1020204127',), ('10202041',), ('1020204226',), ('10202042',), ('10203149',), ('10253146',), ('11160',), ('12000CV46',), ('1798 ADAPT MASTER FUND LTD-521863135',), ('1798 ADAPT MASTER FUND-521863135',), ('1798 ADAPT MASTER FUND',), ('1798 ADAPT MASTER NIP CS1',), ('1798 ADAPT MASTER',), ('1798 Adapt Master Fund Ltd',), ('1798 Adapt Master Fund',), ('19-515962',), ('19-519280',), ('19-6176',), ('2000AC14',), ('2000CV54',), ('2000EP05',), ('200ACL35',), ('2500190',), ('410535692',), ('41297226',), ('41297236',), ('424201',), ('4270015943',), ('4270015978',), ('4270015994',), ('4270042894',), ('4270042924',), ('4270042975',), ('43300251',), ('453238',), ('492741',), ('5000216-001',), ('5000216-003',), ('5183933',), ('5183964',), ('54082441',), ('5408245',), ('5489284',), ('54960851',), ('6151798A',), ('62963558',), ('63399141',), ('63498133',), ('682266',), ('733224',), ('7450017',), ('75207626',), ('8703A',), ('91792781',), ('946589',), ('95U06380',), ('9763',), ('AISC01',), ('C7530036',), ('CM5598',), ('CN0135',), ('DU6I',), ('DU6J',), ('EMN ASC FUND, LP',), ('EMN ASC FUND',), ('FT_W031',), ('FT_W080',), ('GEI31',), ('I0003043',), ('I0003285',), ('JPG',), ('L2000AC14',), ('L2000CV54',), ('L2000EP05',), ('L200ACL35',), ('M4MW',), ('MUDDY WATERS CAP GLOB OPP',), ('MUDDY WATERS CAPITAL DOMINO MASTER FUND LP',), ('MUDDY WATERS CAPITAL GLOBAL OPPORTUNITIES MASTER FUND LP',), ('MYWTCS11',), ('MYWTCS12',), ('MYWTCS22',), ('N0SB',), ('N1YH',), ('N2WZ',), ('N3UR',), ('N4UR',), ('NE61',), ('P910063861',), ('WELTON - ABBEY ACL FD',), ('WELTON GL CAP MARKET',), ('WELTON MULTI-STRATEGY GLOBAL MACRO UCITS FUND',), ('WT CHINA FOCUS FUND_Alternative Energy',), ('WT CHINA FOCUS FUND_Consumer',), ('WT CHINA FOCUS FUND_EV',), ('WT CHINA FOCUS FUND_SMALL-MID',), ('WT CHINA FOCUS FUND_Tech',), ('WT CHINA FOCUS FUND_WT1',), ('WT CHINA FOCUS FUND',), ('WT CHINA FUND LIMITED_Alternative Energy',), ('WT CHINA FUND LIMITED_Alternative Energy',), ('WT CHINA FUND LIMITED_Consumer',), ('WT CHINA FUND LIMITED_Consumer',), ('WT CHINA FUND LIMITED_EV',), ('WT CHINA FUND LIMITED_EV',), ('WT CHINA FUND LIMITED_SMALL-MID',), ('WT CHINA FUND LIMITED_SMALL-MID',), ('WT CHINA FUND LIMITED_Tech',), ('WT CHINA FUND LIMITED_Tech',), ('WT CHINA FUND LIMITED_WT1',), ('WT CHINA FUND LIMITED_WT1',), ('WT CHINA FUND LIMITED',), ('WT CHINA FUND LIMITED',), ('WT_CAPITALFF',), ('WT_CAPITAL',), ('WT_FOCUSFF',), ('WT_FOCUS',), ('Welton Trend',), ('YWTCS11',), ('YWTCS12',), ('YWTCS21',), ('YWTCS22',), ('muddywaters.1685.1657.mddy',), ('muddywaters.41.72.td-scrts',), ('muddywaters.42.58.mddy',)]

# count =0
# print(len(list1))
# # for i in list1:
# #     count+=1
# #     # print(i)
# # print(count)
