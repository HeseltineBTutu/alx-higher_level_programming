"""
Module for handling database connections.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def create_session(username, password, database_name):
    """
    Create and return a database session.

    Parameters:
    username (str): MySQL username.
    password (str): MySQL password.
    database_name (str): Name of the database to connect to.

    Returns:
    sqlalchemy.orm.session.Session: A session object ready for use.
    """
    connection_string = f'mysql+mysqldb://{username}: \
            {password}@localhost/{database_name}'
    engine = create_engine(connection_string, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    return Session()
