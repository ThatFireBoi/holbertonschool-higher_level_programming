#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    try:
        """Connect to a MySQL server."""
        db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3])

        """Create a cursor object."""
        cur = db.cursor()

        """Execute the query."""
        query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY states.id ASC"
        cur.execute(query, (argv[4],))

        """Print the results of the query."""
        for row in cur.fetchall():
            print(row)

        """Close all cursors."""
        cur.close()

        """Close all databases."""
        db.close()

    except MySQLdb.Error as e:
        try:
            print("MySQL Error [{:d}]: {}".format(e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: {}".format(str(e)))
