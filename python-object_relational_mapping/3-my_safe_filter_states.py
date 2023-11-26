#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    """Connect to a MySQL server."""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    """Create a cursor object."""
    cur = db.cursor()

    """Execute the query."""
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s\
                ORDER BY id ASC", (argv[4],))

    """Print the results of the query."""
    for row in cur.fetchall():
        print(row)

    """Close all cursors."""
    cur.close()

    """Close all databases."""
    db.close()
