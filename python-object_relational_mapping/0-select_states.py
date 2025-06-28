#!/usr/bin/python3
"""
This script connects to a MySQL server and lists all states from a specified database.
As a Holberton School intern, I am learning how to interact with databases using Python's MySQLdb module.
This task helps me understand how to fetch and display data from a database table.
"""
import MySQLdb
import sys


def list_states(username, password, db_name):
    """
    Connects to the MySQL server running on localhost at port 3306
    and retrieves all records from the 'states' table, sorted by their IDs.
    Each record is then printed to the console.

    Args:
        username (str): The MySQL username to connect with.
        password (str): The password for the MySQL user.
        db_name (str): The name of the database to connect to.
    """
    try:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=username,
                             passwd=password,
                             db=db_name)
        cursor = db.cursor()
        # As an intern, I'm learning to write SQL queries directly in Python.
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cursor.fetchall()
        for row in rows:
            # Print the string representation of the tuple to match the example exactly.
            print(str(row))
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")


if __name__ == "__main__":
    # This part ensures the script only runs when executed directly,
    # not when imported as a module.
    if len(sys.argv) == 4:
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        mysql_db_name = sys.argv[3]
        list_states(mysql_username, mysql_password, mysql_db_name)