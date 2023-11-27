#!/usr/bin/python3
"""Script that adds the State object “Louisiana” to the database
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

    """Create a new state object."""
    new_state = State(name='Louisiana')

    """Add the new state to the session."""
    session.add(new_state)

    """Commit changes."""
    session.commit()

    """Print the new state id."""
    print("{}".format(new_state.id))

    """Close the session."""
    session.close()
