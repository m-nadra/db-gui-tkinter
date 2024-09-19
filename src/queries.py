from models import engine, Student, Subject, Base
from sqlalchemy.orm import Session
from sqlalchemy import select 


@classmethod
def get(cls) -> list: 
    query = select(cls)
    with engine.connect() as conn:
        return conn.execute(query)

@classmethod
def getColumnNames(cls) -> list:
    return cls.__table__.columns.keys()    

Base.get = get
Base.getColumnNames = getColumnNames
