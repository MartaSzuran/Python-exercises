# # searching specific data in database
# https://www.youtube.com/watch?v=byHcYRpMgI4

import sqlite3

conn = sqlite3.connect("ranking.db")

cur = conn.cursor()

# search in records
# like in normal sql we can use many operators like >,<,>=,<=
# # few examples
cur.execute("SELECT * FROM ranking WHERE name = 'adam'")
# cur.execute("SELECT * FROM ranking WHERE name LIKE 'mar%'")
# cur.execute("SELECT * FROM ranking WHERE name LIKE 'MAR%'")
# cur.execute("SELECT * FROM ranking WHERE name LIKE '%M'")
items = cur.fetchall()

for item in items:
    print(item)

conn.commit()

conn.close()
