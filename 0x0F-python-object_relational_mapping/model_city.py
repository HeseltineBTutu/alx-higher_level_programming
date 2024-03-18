#!/usr/bin/python3
"""Define City class that inherit from Base Class"""
from sqlalchemy import Column, Integer, String, ForeignKey

from model_state import Base


class City(Base):
    """
    Represents a City in the city table of a MySQL database
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
