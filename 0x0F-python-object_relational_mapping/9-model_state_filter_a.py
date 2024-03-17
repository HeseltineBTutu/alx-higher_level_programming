#!/usr/bin/python3
"""
Script for querying the  database for States containing
letter 'a'
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    connection_string = 'mysql+mysqldb://{}:{}@localhost/{}' \
        .format(username, password, database_name)

    engine = create_engine(connection_string, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    states_with_letter_a = session.query(State) \
        .filter(State.name.contains('a')).all()

    if states_with_letter_a:
        for state in states_with_letter_a:
            print(f"{state.id}: {state.name}")

    session.close()
