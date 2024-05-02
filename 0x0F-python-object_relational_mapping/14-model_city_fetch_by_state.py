#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Collect command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine_str = f"mysql+mysqldb://{username}:{password} \
            @localhost:3306/{db_name}"

    engine = create_engine(engine_str, pool_pre_ping=True)
    # Establish connection and start a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for states and associated cities, ordered by city id
    results = session.query(State, City) \
        .join(City, City.state_id == State.id).order_by(City.id).all()

    # Display results
    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
