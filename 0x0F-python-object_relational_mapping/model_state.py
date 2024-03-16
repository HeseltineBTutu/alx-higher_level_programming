#!/usr/bin/python3
"""Define State class and create Base instance."""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of declarative_base
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return f"<State(id={self.id}, name={self.name})>"


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    connection_string = 'mysql+mysqldb://{}:{}@localhost/{}'\
        .format(username, password, database_name)
    # Connect to MySQL server
    engine = create_engine(connection_string, pool_pre_ping=True)

    # Create all tables defined in Base subclass
    Base.metadata.create_all(engine)
