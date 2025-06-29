#!/usr/bin/python3
""" Python x MySQL : Listing all cities by state """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name\
               FROM cities\
               JOIN states ON cities.state_id = states.id\
               ORDER BY cities.id ASC")
    for row in c.fetchall():
        print(row)
    c.close()
    db.close()