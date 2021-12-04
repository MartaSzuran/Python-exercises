# create database with functions for small app
# https://www.youtube.com/watch?v=byHcYRpMgI4

import sqlite3


def show_all():
    """Query the database and return all results."""
    # create a connection
    conn = sqlite3.connect("../ranking.db")
    # create a cursor
    cur = conn.cursor()
    cur.execute("SELECT rowid, * FROM ranking")
    items = cur.fetchall()

    for item in items:
        print(item)

    # commit changes
    conn.commit()
    # close connection
    conn.close()


def add_one(name, score):
    """add new record into db."""
    # create a connection
    conn = sqlite3.connect("../ranking.db")
    # create a cursor
    cur = conn.cursor()
    # insert data
    cur.execute("INSERT INTO ranking VALUES (?,?)", (name, score))

    # commit changes
    conn.commit()
    # close connection
    conn.close()


def delete_one(element_id):
    """Delete one record from the database."""
    # create a connection
    conn = sqlite3.connect("../ranking.db")
    # create a cursor
    cur = conn.cursor()
    # delete one record with id 6
    cur.execute("DELETE FROM ranking WHERE rowid=(?)", element_id)

    # commit changes
    conn.commit()
    # close connection
    conn.close()


def add_many(records_list):
    """Add many records to the database."""
    # create a connection
    conn = sqlite3.connect("../ranking.db")
    # create a cursor
    cur = conn.cursor()
    # add many records with executemany
    cur.executemany("INSERT INTO ranking VALUES (?, ?)", records_list)
    # commit changes
    conn.commit()
    # close connection
    conn.close()


def look_up(name):
    """Search for particular results."""
    # create a connection
    conn = sqlite3.connect("../ranking.db")
    # create a cursor
    cur = conn.cursor()
    # add many records with executemany
    cur.execute("SELECT * FROM ranking WHERE name = (?)", (name,))
    items = cur.fetchall()

    for item in items:
        print(item)

    # commit changes
    conn.commit()
    # close connection
    conn.close()
