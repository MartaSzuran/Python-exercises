# sqlite3_ex_14.py# # LIMITS
# https://www.youtube.com/watch?v=byHcYRpMgI4

import sqlite3

conn = sqlite3.connect("ranking.db")

cur = conn.cursor()

# LIMIT
# limit need to be at the end of the query
cur.execute("SELECT rowid, * FROM ranking ORDER BY score DESC LIMIT 3")

items = cur.fetchall()

for item in items:
    print(item)

conn.commit()

conn.close()