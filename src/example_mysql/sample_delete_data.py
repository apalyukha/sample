import mysql.connector

try:
    connect = mysql.connector.connect(host='localhost',
                                      database='sample',
                                      user='root',
                                      password='')
    cursor = connect.cursor()
    print("Displaying laptop record Before Deleting it")
    sql_select_query = """select * from Laptop where id = 4"""
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    sql_Delete_query = """Delete from Laptop where id = 4"""
    cursor.execute(sql_Delete_query)
    connect.commit()

    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    if len(records) == 0:
        print("\nRecord Deleted successfully ")

except mysql.connector.Error as error:
    print("Failed to delete record from table: {}".format(error))
finally:
    if connect.is_connected():
        cursor.close()
        connect.close()
        print("MySQL connection is closed")
