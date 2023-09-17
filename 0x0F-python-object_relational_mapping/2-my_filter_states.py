#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import MySQLdb

    usernamee = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306, user=username, passwd=password, db=database)
    c = db.cursor()

    query = "SELECT * states WHERE name LIKE BINARY '{}' ORDER BY ASC"
    c.execute(query, .format(state_name))

    result = c.fetchall()

    for arg in result:
        print(arg)

        c.close()
        db.close()
