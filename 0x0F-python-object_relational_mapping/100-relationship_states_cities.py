#!/usr/bin/python3
"""create state california with city as francisco"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_city import City
from relationship_state import State


if __name__ == "__main__":
    engine = create_engine(
                            'mysql+mysqldb://{}:{}@localhost/{}'
                            .format(
                                        sys.argv[1],
                                        sys.argv[2],
                                        sys.argv[3]
                                            ),
                            pool_pre_ping=True
                                )
    session = Session(engine)
    state = State(name="California")
    city = City(
        name="San Francisco",
        state=state)
    session.add(city)
    session.commit()
