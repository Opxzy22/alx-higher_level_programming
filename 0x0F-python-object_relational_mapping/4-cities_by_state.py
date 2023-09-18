#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    stateName = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306, user=username, passwd=password, db=database)
    c = db.cursor()

    c.execute("SELECT cities.id, cities.name, states.name\
                   FROM cities LEFT JOIN states\
                   ON states.id = cities.state_id\
                   ORDER BY cities.id ASC")

    cities = c.fetchall()

    print(", ".join(city[0] for city in cities))

    c.close()
    db.close()