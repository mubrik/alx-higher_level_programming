#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import delete
from sqlalchemy import (create_engine)


def change_state_2(session):
    ''' change details of state '''
    if not session:
        return None
    try:
        states = session.query(State).filter(State.name.like("%a%")).all()
        for state in states:
            session.delete(state)
        session.commit()
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
