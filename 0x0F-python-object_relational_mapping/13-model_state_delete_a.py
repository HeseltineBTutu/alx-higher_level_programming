#!/usr/bin/python3
"""
 a script that deletes all State objects with a name
  containing the letter a from the database
"""
import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


def delete_states_with_a(username, password, db_name):
    """Deletes State objects with names containing the letter 'a'."""

    engine_str = f"mysql+mysqldb://{username}:{password} \
            @localhost:3306/{db_name}"
    engine = create_engine(engine_str, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Filter States with names containing 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%'))

    # Delete the selected states
    for state in states_to_delete:
        session.delete(state)
    session.commit()
    session.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description='Delete states with the letter "a" in their name.'
            )
    parser.add_argument('username', help='MySQL username')
    parser.add_argument('password', help='MySQL password')
    parser.add_argument('database_name', help='Database name')
    args = parser.parse_args()

    delete_states_with_a(args.username, args.password, args.database_name)
