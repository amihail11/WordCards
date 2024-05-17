"""Module for creating a database connection"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

import config

engine = create_engine(config.DATABASE_URL)

LocalSession = sessionmaker(autocommit=False, autoflush=False,bind=engine)

class Base(DeclarativeBase):
    """Represents a base model for the database"""
