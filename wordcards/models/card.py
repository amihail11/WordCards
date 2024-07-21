from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from wordcards.database import Base
from wordcards.models.deck import Deck

from .deck_card import deck_card


class Card(Base):

    __tablename__ = "card"

    pk: Mapped[int] = mapped_column("id", primary_key=True, index=True)
    word: Mapped[str]
    meaning: Mapped[str]
    decks: Mapped[List[Deck]] = relationship(secondary=deck_card, back_populates="card")
