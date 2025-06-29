#!/usr/bin/python3
"""
Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == '__main__':

    username = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{passwd}@localhost:3306/{db}'
        )

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State).filter(
        State.name.like('%a%')).all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()

    session.close()
