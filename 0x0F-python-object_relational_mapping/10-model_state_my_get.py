#!/mnt/MB/sharedPartition/py_envs/alx/bin/python
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

def get_state_id(session, state):
    if not session:
        return None
    res = None
    for res in session.query(State.id).filter(State.name == state):
        print(res[0])
    if not res or not res[0]:
        print('Not found')

if __name__ == "__main__":
    if (sys.argv.__len__() == 5):
        _, username, password, dbname, state = sys.argv
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, dbname), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        get_state_id(session, state)
