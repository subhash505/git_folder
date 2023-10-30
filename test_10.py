column_name_diff = 'Position_asdfg_fghjk_werty_thnm,'
m_column_name_diff = column_name_diff.replace("_", " ")

print(m_column_name_diff)

lst = [33, 3, 22, 2, 11, 1]
s= sorted(filter(lambda x: x > 10, lst), reverse= True)
print(s)


footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[1])
print(sorted_footballers_by_goals)

