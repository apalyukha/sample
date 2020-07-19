import mysql.connector
from mysql.connector import Error

try:
    connect = mysql.connector.connect(host='localhost',
                                      database='sample',
                                      user='root',
                                      password='')
    if connect.is_connected():
        db_Info = connect.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connect.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connect.is_connected():
        cursor.close()
        connect.close()
        print("MySQL connection is closed")
