import mysql.connector
conn={'user':'root','password':'cdac123','host':'127.0.0.1','database':'testdb'}
#connection = mysql.connector.connect(host='localhost',database = 'testdb',user='root',password='cdac123')
connection = mysql.connector.connect(**conn)
if connection.is_connected():
    
    cursor = connection.cursor()
    qry="""create table Laptop1
        ( Id  int(11) not null,
        name varchar(50) not null,
        Price float not null,
        purchase_date date,
        primary key(Id))
        """
    cursor.execute(qry)
    print("Table Created successfully")
    #print(result)
    cursor.close()
    connection.close()
