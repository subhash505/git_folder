import pyodbc
 
cursor = cnxn.cursor()
cnxn = pyodbc.connect('DSN=CData Excel Source;User=MyUser;Password=MyPassword')
cursor.execute("SELECT Name, Revenue FROM Sheet WHERE Name = 'Bob'")
rows = cursor.fetchall()
for row in rows:
print(row.Name, row.Revenue)