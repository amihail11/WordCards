"""Module for creating a card model"""

from sqlalchemy.orm import Mapped, mapped_column

from wordcards.database import Base


class Card(Base):
    """Represents a card model with a foreign word, its meaning and ID"""

    __tablename__ = "cards"

    pk: Mapped[int] = mapped_column("id", primary_key=True, index=True)
    word: Mapped[str]
    meaning: Mapped[str]
