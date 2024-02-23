#!/usr/bin/python3
""" lists all State objects, and corresponding City objects"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State, Base


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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    objs = session.query(State).all()
    for obj in objs:
        print(f"{obj.id}: {obj.name}")
        for city in obj.cities:
            print(f"    {city.id}: {city.name}")
