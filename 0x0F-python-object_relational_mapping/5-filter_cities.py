#!/usr/bin/python3

if __name__ = "__main__":
    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    stateName = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost,
            port=3306, user=username, passwd=password, db=database)

    c = db.cursor()

    c.execute("SELECT cities.name\
                    FROM cities\
                    INNER JOIN states ON cities.state.id = states.id\
                    WHERE states.name = %s\
                    ORDER BY cities.id ASC", (stateName,))

    cities = c.fetchall()

    print(", ".join([city[0] for city in cities]))

    c.close()
    db.close()
