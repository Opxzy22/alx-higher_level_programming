#!/usr/bin/python3

if __name__ == "__main__":
import sys
import MySQLdb

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(
        host="local host",
        port=3306,
        user=username,
        passwd=password,
        db=database)

c = db.cursor()

c.execute("select * FROM states WHERE name BINARY LIKE 'N%' ORDER BY id ASC")
Nstate = c.fetchall()

for state in Nstate:
    print(state)
