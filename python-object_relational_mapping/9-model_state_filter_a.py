#!/usr/bin/python3
"""Script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa."""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    """Create an engine."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    """Create a configured class Session."""
    Session = sessionmaker(bind=engine)

    """Create a Session instance."""
    session = Session()

    """Querying is done via the Query API"""
    for state in session.query(State).filter(State.name.like('%a%'))\
            .order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    """Close the session."""
    session.close()
