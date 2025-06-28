#!/usr/bin/python3
"""
This script connects to a MySQL server and lists all states from a specified database.
As a Holberton School intern, I am learning how to interact with databases using Python's MySQLdb module.
This task helps me understand how to fetch and display data from a database table.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
        )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()