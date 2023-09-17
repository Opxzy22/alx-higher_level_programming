#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import MySQLdb

    usernamee = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    stateName = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306, user=username, passwd=password, db=database)
    c = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY '{0}%' ORDER BY id ASC"
    c.execute(query.format(stateName))

    result = c.fetchall()

    for arg in result:
        print(arg)

    c.close()
    db.close()
