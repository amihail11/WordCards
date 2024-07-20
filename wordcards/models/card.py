from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from wordcards.database import Base
from wordcards.models.deck import Deck

from .card_deck import card_deck


class Card(Base):

    __tablename__ = "cards"

    pk: Mapped[int] = mapped_column("id", primary_key=True, index=True)
    word: Mapped[str]
    meaning: Mapped[str]
    decks: Mapped[List[Deck]] = relationship(
        secondary=card_deck, back_populates="cards"
    )
