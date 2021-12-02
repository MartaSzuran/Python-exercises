# # CREATING TABLES

import sqlite3
from sqlite3 import Error

# https://www.sqlitetutorial.net/sqlite-python


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


def create_table(con, create_table_sql):
    try:
        c = con.cursor()
        c.execute(create_table_sql)

    except Error as e:
        print(e)


def main():
    database = "ranking.db"

    sql_create_ranking_table = """CREATE TABLE IF NOT EXISTS ranking (
                                    name text NOT NULL, 
                                    score integer NOT NULL
                                    );"""

    connection = sqlite3.connect(database)

    if connection is not None:
        create_table(connection, sql_create_ranking_table)
        connection.commit()
        print("The table has been created.")
    else:
        print("Error! Cannot create database connection.")

    connection.close()


main()
