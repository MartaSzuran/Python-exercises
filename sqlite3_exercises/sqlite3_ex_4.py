# # practise with fetching
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


connection = create_connection("ranking.db")

cur = connection.cursor()

cur.execute("SELECT * FROM ranking")

# I take from database data and the number is smaller,
# so if I fetchone, from 7 lines in sql table left 6,
# then if I take 3 more, 3 left
# and later there is just an empty list
print(cur.fetchone()[0])
print(cur.fetchmany(3))
print(cur.fetchall())
print(cur.fetchone())

connection.close()
