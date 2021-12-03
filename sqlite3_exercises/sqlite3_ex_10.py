# # delete
# https://www.youtube.com/watch?v=byHcYRpMgI4

import sqlite3

conn = sqlite3.connect("ranking.db")

cur = conn.cursor()

# delete records
# delete is permanent
cur.execute("DELETE from ranking WHERE rowid = 9")

cur.execute("SELECT rowid, * FROM ranking")

items = cur.fetchall()

for item in items:
    print(item)

conn.commit()

conn.close()