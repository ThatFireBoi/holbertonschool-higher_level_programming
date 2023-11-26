#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa."""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Connect to a MySQL server."""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    """Create a cursor object."""
    cur = db.cursor()

    """Execute the query."""
    query = "SELECT cities.id, cities.name, states.name FROM cities \
        INNER JOIN states ON cities.state_id = states.id \
        ORDER BY cities.id ASC"

    cur.execute(query)

    """Print the results of the query."""
    for row in cur.fetchall():
        print(row)

    """Close all cursors."""
    cur.close()

    """Close all databases."""
    db.close()
