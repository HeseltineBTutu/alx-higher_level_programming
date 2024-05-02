#!/usr/bin/python3
"""
This script connects to a MySQL database and displays
all values in the cities of the given state..

Usage: ./5-filter_cities.py username password database_name state_name
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
    # Cretae a cursor object using context manager
    with db.cursor() as cursor:
        cursor.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %s
            ORDER BY
                cities.id ASC
        """, (state_name,))

        # Fetch the rows
        rows = cursor.fetchall()

        print(", ".join([row[1] for row in rows]))

    db.close()
