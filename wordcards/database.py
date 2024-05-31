"""Module for creating a database connection"""

from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from config import DATABASE_URL

engine = create_engine(DATABASE_URL)

SessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    """Represents a base model for the database"""


def get_db():
    """get database connection"""
    db = SessionMaker()
    try:
        yield db
    finally:
        db.close()


DbSession = Annotated[Session, Depends(get_db)]
