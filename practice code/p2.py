import pyodbc

try:
    server = 'localhost'
    database = 'subhashdb'
    username = 'root'
    password = 'Subhash2047@'
    connection_string = f"DRIVER={{MySQL ODBC 8.0 Unicode Driver}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    cnxn = pyodbc.connect(connection_string)
    print("connection established")
    print(cnxn)
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM laptop1")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    cnxn.close()
except:
    print("error in connection")
