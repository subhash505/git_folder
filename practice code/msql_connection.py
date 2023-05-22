import mysql.connector  

def main():  
    #Create the connection object   
    myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "Subhash2047@")  

    #printing the connection object   
    print(myconn)  
    if myconn.is_connected():
        print("connection is established")
    print("now we are closing the connection")
    myconn.close()
    print("connection is closed")
if __name__=="__main__":
    main()