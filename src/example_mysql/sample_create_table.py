import mysql.connector
from mysql.connector import Error

try:
    connect = mysql.connector.connect(host='localhost',
                                      database='sample',
                                      user='root',
                                      password='')

    mySql_Create_Table_Query = """CREATE TABLE Laptop ( 
                             Id int(11) NOT NULL,
                             Name varchar(250) NOT NULL,
                             Price float NOT NULL,
                             Purchase_date Date NOT NULL,
                             PRIMARY KEY (Id)) """

    cursor = connect.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")

except Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connect.is_connected():
        cursor.close()
        connect.close()
        print("MySQL connection is closed")
