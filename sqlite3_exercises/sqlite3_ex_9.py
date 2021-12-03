# # update records
# https://www.youtube.com/watch?v=byHcYRpMgI4

import sqlite3

conn = sqlite3.connect("ranking.db")

cur = conn.cursor()

# update records
# because there could be many same names we should rather make changes by id number
cur.execute("""UPDATE ranking SET score = 10
WHERE rowid = 5""")

cur.execute("SELECT rowid, * FROM ranking")

items = cur.fetchall()

for item in items:
    print(item)

conn.commit()

conn.close()
