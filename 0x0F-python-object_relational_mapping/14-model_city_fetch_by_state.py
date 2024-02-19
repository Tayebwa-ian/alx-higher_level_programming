#!/usr/bin/python3
"""Query all states"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


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
    cities = session.query(City).join(State).all()
    for city in cities:
        state = session.query(State).filter(
            State.id == city.state_id).first()
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
