# # AND/OR
# https://www.youtube.com/watch?v=byHcYRpMgI4

import sqlite3

conn = sqlite3.connect("ranking.db")

cur = conn.cursor()

# AND/OR
# cur.execute("SELECT rowid, * FROM ranking WHERE name LIKE 'mar%' AND score > 60")
cur.execute("SELECT rowid, * FROM ranking WHERE name LIKE 'mar%' OR score > 60")

items = cur.fetchall()

for item in items:
    print(item)

conn.commit()

conn.close()