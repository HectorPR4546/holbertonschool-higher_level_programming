#!/usr/bin/python3
"""
Defines the City class for a MySQL database.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """
    Represents a city for a MySQL database.

    Attributes:
        __tablename__ (str): The name of the MySQL table to link to.
        id (sqlalchemy.Integer): The city's id.
        name (sqlalchemy.String): The city's name.
        state_id (sqlalchemy.Integer): The state id the city belongs to.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
