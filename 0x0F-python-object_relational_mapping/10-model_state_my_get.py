#!/usr/bin/python3

"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    """
    Create the database engine
    """
    engine = ('mysql://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    """
    create a session to interact with the engine
    """
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = sys.argv[4]

    arg_state = session.query(State).filter(State.name == state).all()

    if arg_state:
        for instance in arg_state:
            print(instance.name, instance.id)
    else:
        print("Not found")
