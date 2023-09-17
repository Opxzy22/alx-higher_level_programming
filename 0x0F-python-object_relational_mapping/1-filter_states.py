#!/usr/bin/python3

import sys
import MySQLdb

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(host="local host", port=3306, user=username, 
        passwd=password, db=database)

c = db.cursor()

Nstate = c.execute ("select * FROM states WHERE UPPER(name) LIKE 'N%'")
c.fetchall()

for state in Nstate:
    print(state)
