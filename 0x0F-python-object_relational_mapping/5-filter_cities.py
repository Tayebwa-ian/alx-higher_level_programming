#!/usr/bin/python3
"""Make a connectiion to the database using the MySQldb module"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, database=db_name,
                         user=username, password=password)
    cursor = db.cursor()
    query = """SELECT city_name FROM (SELECT cities.id, cities.name
           AS city_name, states.name AS state_name
          FROM cities INNER JOIN states ON cities.state_id = states.id
          ORDER BY cities.id ASC) AS table1
          WHERE table1.state_name = %s"""

    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    if len(rows) > 0:
        for row in rows:
            if row is not rows[-1]:
                print(row[0], end=", ")
            else:
                print(row[0])
    else:
        print()
    cursor.close()
    db.close()
