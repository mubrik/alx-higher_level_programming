#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


def create_cali(session):
    ''' change details of state '''
    if not session:
        return None
    try:
        cali = State(name='California')
        cali.cities = [
            City(name='San Francisco')
        ]
        session.add(cali)
        session.commit()
    except Exception as e:
        print('err occured', e)


if __name__ == "__main__":
    if (sys.argv.__len__() == 4):
        _, username, password, dbname = sys.argv
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                username, password, dbname), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        create_cali(session)
