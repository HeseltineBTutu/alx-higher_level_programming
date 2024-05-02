#!/usr/bin/python3
"""
 a script that changes the name of a State object from the database
"""
import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


def change_state_name(username, password, db_name):
    """Changes the name of the State with id=2 to 'New Mexico'."""
    engine_str = f"mysql+mysqldb://{username}:{password} \
            @localhost:3306/{db_name}"
    engine = create_engine(engine_str)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the existing state with id=2
    state_to_update = session.query(State).filter(State.id == 2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
    session.close()


if __name__ == "__main__":
    parser = argparse \
            .ArgumentParser(description='Change state name in database.')
    parser.add_argument('username', help='MySQL username')
    parser.add_argument('password', help='MySQL password')
    parser.add_argument('database_name', help='Database name')
    args = parser.parse_args()

    change_state_name(args.username, args.password, args.database_name)
