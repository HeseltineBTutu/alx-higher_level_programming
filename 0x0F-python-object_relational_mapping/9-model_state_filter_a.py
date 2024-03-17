#!/usr/bin/python3
"""
Script for querying the  database for States containing
letter 'a'
"""
import sys
from db import create_session, State

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    session = create_session(username, password, database_name)
    states_with_letter_a = session.query(State) \
        .filter(State.name.contains('a')).all()

    if states_with_letter_a:
        for state in states_with_letter_a:
            print(f"{state.id}: {state.name}")

    session.close()
