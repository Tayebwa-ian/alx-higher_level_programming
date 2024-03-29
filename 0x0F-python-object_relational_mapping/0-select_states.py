#!/usr/bin/python3
"""Make a connectiion to the database using the MySQldb module"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, database=db_name,
                         user=username, password=password)
    cursor = db.cursor()

    cursor.execute("""SELECT * FROM states ORDER BY id ASC""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
