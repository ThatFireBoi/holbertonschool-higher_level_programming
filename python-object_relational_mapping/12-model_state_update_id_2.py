#!/usr/bin/python3
"""Script that changes the name of a State object from the database
hbtn_0e_6_usa using SQLAlchemy.
"""

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
    state = session.query(State).filter(State.id == 2).first()
    if state:
        state.name = "New Mexico"
        session.commit()

    """Close the session."""
    session.close()
