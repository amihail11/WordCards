from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from wordcards.database import Base
from wordcards.models.card import Card

from .deck_card import deck_card


class Deck(Base):
    __tablename__ = "deck"

    pk: Mapped[int] = mapped_column("id", primary_key=True, index=True)
    name: Mapped[str]
    cards: Mapped[List[Card]] = relationship(secondary=deck_card, back_populates="deck")
