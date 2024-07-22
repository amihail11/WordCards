from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from wordcards.database import Base

if TYPE_CHECKING:
    from .card import Card
    from .deck import Deck


class DeckCard(Base):

    __tablename__ = "deck_card"

    deck_id: Mapped[int] = mapped_column(ForeignKey("deck.id"), primary_key=True)
    card_id: Mapped[int] = mapped_column(ForeignKey("card.id"), primary_key=True)

    deck: Mapped["Deck"] = relationship(back_populates="cards")
    card: Mapped["Card"] = relationship(back_populates="decks")