from typing import TYPE_CHECKING, List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from wordcards.database import Base

from .deck_card import DeckCard

if TYPE_CHECKING:
    from .card import Card


class Deck(Base):
    __tablename__ = "deck"

    pk: Mapped[int] = mapped_column("id", primary_key=True, index=True)
    name: Mapped[str]
    cards: Mapped[List["Card"]] = relationship(
        secondary=DeckCard, back_populates="decks"
    )
