#!/usr/bin/python3
"""Make a connectiion to the database using the MySQldb module"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, database=db_name,
                         user=username, password=password)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    cursor.execute(query, (search_name,))
    rows = cursor.fetchall()
    for row in rows:
        if row[1] == search_name:
            print(row)
    cursor.close()
    db.close()
