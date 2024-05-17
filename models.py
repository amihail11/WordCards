"""Module for creating a card model"""

from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Card(Base):
    """Represents a card model with a foreign word, its translation and id"""
    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    foreign_word: Mapped[str]
    translation: Mapped[str]
    