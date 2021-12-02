import sqlite3
from sqlite3 import Error

# https://www.sqlitetutorial.net/sqlite-python


# first create connection and check if any error occurs
def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print("Connected to " + db_file)
    except Error:
        print("Ups something went wrong ...")
    finally:
        if connection:
            connection.close()
            print("Close connection to " + db_file)


create_connection("ranking.db")

