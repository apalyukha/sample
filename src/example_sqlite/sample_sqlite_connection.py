import sqlite3


conn = sqlite3.connect('test.db')
cursor = conn.cursor()
print("Opened database successfully")

sqlite_select_Query = "select sqlite_version();"
cursor.execute(sqlite_select_Query)
record = cursor.fetchall()
print("SQLite Database Version is: ", record)

cursor.close()
print("The SQLite connection is closed")
