"""This module contains the queries that are used to interact with the database."""

from models import engine, Base, Student, Subject
from sqlalchemy.orm import Session
from sqlalchemy import select


def getTablesNames() -> list:
    """Return the capitalized names of the tables in the database."""
    return [table.capitalize() for table in Base.metadata.tables.keys()]


@classmethod
def getRows(cls) -> list:
    """Return all the records of the table."""
    query = select(cls)
    with engine.connect() as conn:
        return conn.execute(query)


@classmethod
def getColumnNames(cls) -> list:
    """Return the names of the columns of the table."""
    return cls.__table__.columns.keys()


@classmethod
def deleteRecord(cls, recordId: int) -> None:
    """Delete the record with the given id."""
    with Session(engine) as session:
        recordToDelete = session.get(cls, recordId)
        session.delete(recordToDelete)
        session.commit()


@classmethod
def addRecord(cls, **kwargs: dict) -> None:
    """Add a record to the table."""
    record = cls(**kwargs)
    with Session(engine) as session:
        session.add(record)
        session.commit()


Base.getRows = getRows
Base.getColumnNames = getColumnNames
Base.deleteRecord = deleteRecord
Base.addRecord = addRecord
