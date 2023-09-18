#!/usr/bin/python3
"""a python file that contains the class definition of a State
and an instance Base = declarative_base():"""

from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
"""Import SQLAlchemy"""


Base = declarative_base()
"""Define the database models"""


class State(Base):
    __tablename__ = 'states'

    id = column(integer, unique=True, nullable=False, primary_key=True)
    name = column(string(128), nullable=False)
