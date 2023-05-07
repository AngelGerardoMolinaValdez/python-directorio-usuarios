import sqlite3
import os

path = os.path.join(
    os.path.dirname(__file__), "directory.db"
)

print(path)

connection = sqlite3.connect(path)

cursor = connection.cursor()

cursor.execute('''CREATE TABLE users
             (id INTEGER PRIMARY KEY,
             name TEXT,
             phone TEXT,
             email TEXT,
             address TEXT)''')

connection.commit()

connection.close()
