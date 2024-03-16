#!/usr/bin/python3
"""
This script connects to a MySQL database and displays
all values in the states table where name matches the argument

Usage:./3-my_safe_filter_states.py root root database_name state_name
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
            )

    cursor = db.cursor()
    # Execute SQL query with parameters
    sql_query = "SELECT * FROM states \
            WHERE name LIKE BINARY %s ORDER BY \
            id ASC"
    cursor.execute(sql_query, (state_name,))
    # Fetch all the rows
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
