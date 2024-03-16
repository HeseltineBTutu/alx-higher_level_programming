#!/usr/bin/python3
"""
This script connects to a MySQL database and lists
states with a name starting with N (upper N) from the database

Usage: ./1-filter_states.py
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.Connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
            )
    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
