#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

def get_states_with_a(session):
    ''' gets state that starts with a'''
    if not session:
        return None
    for id, name in session.query(State.id, State.name).where(State.name.contains('a')):
        print(f'{id}: {name}')

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    get_states_with_a(session)
