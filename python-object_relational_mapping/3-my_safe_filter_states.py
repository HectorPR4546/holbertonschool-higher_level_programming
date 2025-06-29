#!/usr/bin/python3
""" Python x MySQL : Listing specific data from a database safely """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    c = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY states.id"
    c.execute(query, (argv[4],))
    for state in c.fetchall():
        print(state)
    c.close()
    db.close()
