#!/usr/bin/python3
"""
a script that adds the State object “Louisiana” to the database
"""
import argparse
import sysy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


def add_louisiana(username, password, db_name):
    """
    Adds a 'Louisiana' State object to the specified database.
    """

    # Construct database connection string
    engine_str = f"mysql+myisqldb://{username}:{password} \
            @localhost:3306/{db_name}"

    # Create a database engine
    engine = create_engine(engine_str, pool_pre_ping=True)
    # Create a session factory to interact with the database
    Session = sessionmaker(bind=engine)
    isession = Session()
    # Create the Louisiana state object
    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()

    print(f"{louisiana.id}")

    session.close()


if __name__ == "__main__":
    # Argument parsing for username, password, and database name
    parser = argparse \
            .ArgumentParser(description='Add Louisiana state to database.')
    parser.add_argument('username', help='MySQL username')
    parser.add_argument('password', help='MySQL password')
    parser.add_argument('database_name', help='Database name')
    args = parser.parse_args()

    # Call the function to add the state
    add_louisiana(args.username, args.password, args.database_name)
