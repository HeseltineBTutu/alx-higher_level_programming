#!/usr/bin/python3
""" lists all State objects from the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    connection_string = 'mysql+mysqldb://{}:{}@localhost/{}' \
        .format(username, password, database_name)

    engine = create_engine(connection_string, pool_pre_ping=True)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Start a session
    session = Session()

    # Query for all states, sorted by id
    all_states = session.query(State).order_by(State.id).all()

    # Display results
    for state in all_states:
        print(f"{state.id}: {state.name}")
    session.close()
