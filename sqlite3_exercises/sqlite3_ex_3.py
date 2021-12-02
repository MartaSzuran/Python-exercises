# # insert and print table using sql
# https://www.sqlitetutorial.net/sqlite-python
# https://www.youtube.com/watch?v=byHcYRpMgI4

import sqlite3
from sqlite3 import Error


# create connection
def create_connection(db_file):
    """Function returns a Connection object which represents an SQLite database
    specified by the database file parameter db_file."""

    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print("Connected to " + db_file)
        return connection
    except Error as e:
        print(e)

    return connection


def main():
    # create connection
    connection = create_connection("ranking.db")

    # create cursor
    cur = connection.cursor()

    # insert into ranking some values
    cur.execute("INSERT INTO ranking VALUES ('marta', 60)")

    # commit on connection
    connection.commit()

    # select all from table ranking
    cur.execute("SELECT * FROM ranking")

    print(cur.fetchall())
    # cur.fetchone()
    # cur.fetchmany()

    print("Operation done successfully")

    connection.close()


main()
