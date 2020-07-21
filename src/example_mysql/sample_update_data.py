import mysql.connector
from mysql.connector import Error

try:
    connect = mysql.connector.connect(host='localhost',
                                      database='sample',
                                      user='root',
                                      password='')
    cursor = connect.cursor()

    print("Before updating a record ")
    sql_select_query = """select * from Laptop where id = 1"""
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    # Update single record now
    sql_update_query = """Update Laptop set Price = 70888 where id = 1"""
    cursor.execute(sql_update_query)
    connect.commit()
    print("Record Updated successfully ")

    print("After updating record ")
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

except Error as error:
    print("Failed to update table record: {}".format(error))
finally:
    if connect.is_connected():
        connect.close()
        print("MySQL connection is closed")
