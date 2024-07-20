from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from wordcards.database import Base
from wordcards.models.card import Card

from .card_deck import card_deck


class Deck(Base):
    __tablename__ = "decks"

    pk: Mapped[int] = mapped_column("id", primary_key=True, index=True)
    name: Mapped[str]
    cards: Mapped[List[Card]] = relationship(
        secondary=card_deck, back_populates="decks"
    )
