from typing import TYPE_CHECKING, List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from wordcards.database import Base

from .deck_card import DeckCard

if TYPE_CHECKING:
    from .deck import Deck


class Card(Base):

    __tablename__ = "card"

    pk: Mapped[int] = mapped_column("id", primary_key=True, index=True)
    word: Mapped[str]
    meaning: Mapped[str]
    decks: Mapped[List["Deck"]] = relationship(
        secondary=DeckCard, back_populates="cards"
    )
