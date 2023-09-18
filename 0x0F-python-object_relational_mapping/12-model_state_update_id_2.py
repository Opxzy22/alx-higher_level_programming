#!/usr/bin/python3

"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import State, Base
from sqlalchemy.orm import sessionmaker

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

    change_name = session.query(State).filter_by(id=2).first()

    change_name.name = 'New Mexico'

    session.add(change_name)

    session.commit()
