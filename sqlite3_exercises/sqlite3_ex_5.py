# # format results
# https://www.youtube.com/watch?v=byHcYRpMgI4

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        print("Successfully connect to " + db_file)
        return conn

    except Error as e:
        print("Ups can't connect " + db_file)

    return conn


con = create_connection("ranking.db")
cur = con.cursor()

cur.execute("SELECT * FROM ranking")

items = cur.fetchall()
#print(items)

for item in items:
    print(item)

for item in items:
    print(item[0])

print("NAME" + "\t|\t" + "SCORE")
print("----" + "\t|\t" + "-----")
for item in items:
    print(item[0] + "\t|\t" + str(item[1]))
