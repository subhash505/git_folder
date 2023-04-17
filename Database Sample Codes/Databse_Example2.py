import mysql.connector
connection = mysql.connector.connect(host='localhost',database = 'testdb',user='root',password='cdac123')
if connection.is_connected():
    print(connection.get_server_info())
    cursor = connection.cursor()
    cursor.execute("Show Tables;")
    record=cursor.fetchall()
    print("Tables : ",record)
    cursor.close()
    connection.close()
    
