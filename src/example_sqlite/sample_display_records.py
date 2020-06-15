import sqlite3


conn = sqlite3.connect('test.db')
print("Opened database successfully")

cursor = conn.execute("SELECT id, name, age from PERSON")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("AGE = ", row[2], "\n")

print("Operation done successfully")
conn.close()
