#!/usr/bin/python3
"""
This script connects to a MySQL database and lists
all states from the specified table.

Usage: ./0-select_states.py
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
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close cursor sand database connection
    cursor.close()
    db.close()
