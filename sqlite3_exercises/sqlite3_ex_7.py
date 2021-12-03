# # quick insert practise
# https://www.youtube.com/watch?v=byHcYRpMgI4

import sqlite3

conn = sqlite3.connect("ranking.db")

cur = conn.cursor()

cur.execute("INSERT INTO ranking VALUES ('adam', 80)")

cur.execute("SELECT rowid, * FROM ranking")
items = cur.fetchall()

for item in items:
    print(item)

conn.commit()

conn.close()
