#!/usr/bin/python3
"""
This script connects to a MySQL database and displays
all values in the cities of that state.

Usage:./5-filter_cities.py
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
            )
    cursor = db.cursor()
    sql_query = "SELECT GROUP_CONCAT(cities.name ORDER BY cities.id \
            ASC SEPARATOR ', ') \
            FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s"
    cursor.execute(sql_query, (state_name,))
    # Fetch the row
    row = cursor.fetchone()
    if row[0]:
        print(row[0])
    cursor.close()
    db.close()
