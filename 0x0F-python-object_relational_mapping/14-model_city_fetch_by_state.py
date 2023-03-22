#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


def change_state_2(session):
    ''' change details of state '''
    if not session:
        return None
    try:
        for city_id, city_name, state_name in session.query(
                City.id, City.name, State.name).join(State).order_by(City.id):
            print(f'{state_name}: {city_id} {city_name}')
    except Exception:
        print('err occured')


if __name__ == "__main__":
    if (sys.argv.__len__() == 4):
        _, username, password, dbname = sys.argv
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                username, password, dbname), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        change_state_2(session)
