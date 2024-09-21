from models import engine, Student, Subject, Base
from sqlalchemy.orm import Session
from sqlalchemy import select, delete 


@classmethod
def get(cls) -> list:
    query = select(cls)
    with engine.connect() as conn:
        return conn.execute(query)

@classmethod
def getColumnNames(cls) -> list:
    return cls.__table__.columns.keys()    

@classmethod
def deleteRecord(cls, recordId):
    with Session(engine) as session:
        recordToDelete = session.get(cls, recordId)
        session.delete(recordToDelete)
        session.commit()

Base.get = get
Base.getColumnNames = getColumnNames
Base.deleteRecord = deleteRecord

def addStudent(name, lastname):
    student = Student(name=name, lastname=lastname)
    with Session(engine) as session:
        session.add(student)
        session.commit()

def getTablesNames():
    return [table.capitalize() for table in Base.metadata.tables.keys()]
