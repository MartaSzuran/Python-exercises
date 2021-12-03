# # order records
# https://www.youtube.com/watch?v=byHcYRpMgI4

import sqlite3

conn = sqlite3.connect("ranking.db")

cur = conn.cursor()

# order records
# query the database - ORDER BY
# be default ASC / DESC
cur.execute("SELECT rowid, * FROM ranking ORDER BY score DESC")

items = cur.fetchall()

for item in items:
    print(item)

conn.commit()

conn.close()