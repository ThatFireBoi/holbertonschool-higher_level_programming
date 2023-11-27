#!/usr/bin/python3
"""Script that lists all City objects from the database hbtn_0e_14_usa."""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    """Create an engine."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    """Create a configured class Session."""
    Session = sessionmaker(bind=engine)

    """Create a Session instance."""
    session = Session()

    """Querying is done via the Query API"""
    for city, state in session.query(City, State).filter(City.state_id == State.id)\
            .order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    """Close the session."""
    session.close()
