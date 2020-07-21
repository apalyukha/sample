import mysql.connector
from mysql.connector import Error

try:
    connect = mysql.connector.connect(host='localhost',
                                      database='sample',
                                      user='root',
                                      password='')

    insert_query = "INSERT INTO Laptop (Id, Name, Price, Purchase_date) VALUES (%s, %s, %s, %s)"

    write_val = [(1, 'MacBook Pro 2020', 60555, '2020-07-19'),
           (2, 'Lenovo IdeaPad 2020', 21300, '2020-07-19'),
           (3, 'HP EliteBook 2020', 41250, '2020-07-19')]

    cursor = connect.cursor()
    # TODO: executemany() приймає послідовність об'єктів параметрів (словників),
    #  якщо лише один словник, просто використовувати execute()
    cursor.executemany(insert_query, write_val)
    connect.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()

except Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if connect.is_connected():
        connect.close()
        print("MySQL connection is closed")
