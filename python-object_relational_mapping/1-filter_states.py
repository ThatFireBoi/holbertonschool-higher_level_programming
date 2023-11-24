#!/usr/bin/python3
"""Script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    """Connect to a MySQL server."""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    """Create a cursor object."""
    cur = db.cursor()

    """Execute the query."""
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    """Print the results of the query."""
    for row in cur.fetchall():
        if row[1][0] == 'N':
            print(row)

    """Close all cursors."""
    cur.close()

    """Close all databases."""
    db.close()
