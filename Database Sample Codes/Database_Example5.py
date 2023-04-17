import mysql.connector


def InsertIntoTable(id,name,price,purchase_date):
    connection = mysql.connector.connect(host='localhost',database = 'testdb',user='root',password='cdac123')
    Insertqry="""insert into Laptop(id,name,price,purchase_date)
        values(%s,%s,%s,%s)
        """
    
    cursor = connection.cursor()
    recordtuple=(id,name,price,purchase_date)
    cursor.execute(Insertqry,recordtuple)
    connection.commit();
    print("Inserted record successfully")
    #print(result)
    cursor.close()
    connection.close()
