import mysql.connector
conn={'user':'root','password':'cdac123','host':'127.0.0.1','database':'testdb'}
#connection = mysql.connector.connect(host='localhost',database = 'testdb',user='root',password='cdac123')
connection = mysql.connector.connect(**conn)
if connection.is_connected():
    
    
    Insertqry="""insert into Laptop(id,name,price,purchase_date)
        values(1,'Lenovo ThinkPad',55000,'2022-04-19')
        """
    cursor = connection.cursor()
    cursor.execute(Insertqry)
    connection.commit
    print("Inserted record successfully")
    #print(result)
    cursor.close()
    connection.close()
