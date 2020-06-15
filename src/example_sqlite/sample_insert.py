import sqlite3


conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT INTO PERSON (ID,NAME,AGE) \
      VALUES (1, 'Andriy', 39 )")

conn.execute("INSERT INTO PERSON (ID,NAME,AGE) \
      VALUES (2, 'Maria', 37 )")

conn.execute("INSERT INTO PERSON (ID,NAME,AGE) \
      VALUES (3, 'Roksi', 9 )")

conn.commit()
print("Records created successfully")
conn.close()
