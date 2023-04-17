import cx_Oracle
import config

connection= cx_Oracle.connect(config.username,config.password,config.dsn,encoding=config.encoding)
print(connection.version)
connection.close()
