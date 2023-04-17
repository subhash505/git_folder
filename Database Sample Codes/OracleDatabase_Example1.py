import cx_Oracle
con=cx_Oracle.connect("system/Cdac1234@localhost:1521/orcl.226.42.58")
cursor =con.cursor()
cursor.execute("insert into demo1(a,b) values(1,'Nimesh')")
con.commit()
print("Record Inserted sucessfully")
cursor.close()
con.close()
