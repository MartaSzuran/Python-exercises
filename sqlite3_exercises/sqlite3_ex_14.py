# sqlite3_ex_15.py
# # DELETE TABLE
# https://www.youtube.com/watch?v=byHcYRpMgI4

import sqlite3

conn = sqlite3.connect("ranking.db")

cur = conn.cursor()

# drop table
# limit need to be at the end of the query
cur.execute("DROP TABLE ranking")

# information that there is no such table
cur.execute("SELECT rowid, * FROM ranking ORDER BY score DESC LIMIT 3")
conn.commit()

items = cur.fetchall()

for item in items:
    print(item)

conn.close()
