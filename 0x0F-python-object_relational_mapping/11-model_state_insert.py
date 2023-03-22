#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


def insert_louisiana(session):
    ''' gets id of state'''
    if not session:
        return None
    try:
        state = State(name='Louisiana')
        session.add(state)
        session.commit()
        print(state.id)
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
        insert_louisiana(session)
