#!/usr/bin/python3
"""
Prints the State object with a given name from the database.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    conn_str = 'mysql+mysqldb://{}:{}@localhost/{}' \
        .format(username, password, db_name)
    engine = create_engine(conn_str, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Parameterized query to prevent SQL injection
    result = session.query(State).filter(State.name == state_name).first()

    if result:
        print(result.id)
    else:
        print("Not found")
    
    session.close()
