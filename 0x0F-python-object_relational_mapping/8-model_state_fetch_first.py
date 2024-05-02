#!/usr/bin/python3
"""
a script that prints the first State object from the database
"""
import sys
from sqlalchemy import create_engine
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
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    if first_state is None:
        print("Nothing")
    session.close()
