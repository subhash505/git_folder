import mysql.connector
conn={'user':'root','password':'Subhash2047@','host':'localhost','database':'subhashdb'}
#connection = mysql.connector.connect(host='localhost',database = 'testdb',user='root',password='cdac123')
connection = mysql.connector.connect(**conn)
if connection.is_connected():
    print("connection is established")
    cursor = connection.cursor()
    # qry="""create table Laptop1
    #     ( Id  int(11) not null,
    #     name varchar(50) not null,
    #     Price float not null,
    #     purchase_date date,
    #     primary key(Id))
    #     """
    qry="""select * from Laptop1;"""
    cursor.execute(qry)
    print("Table Created successfully")
    #print(result)
    cursor.close()
    connection.close()
