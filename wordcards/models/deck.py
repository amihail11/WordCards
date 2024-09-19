from typing import TYPE_CHECKING, List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from wordcards.database import Base

if TYPE_CHECKING:
    from .card import Card
    from .user import User


class Deck(Base):
    __tablename__ = "deck"

    pk: Mapped[int] = mapped_column("id", primary_key=True, index=True)
    name: Mapped[str]
    cards: Mapped[List["Card"]] = relationship(
        secondary="deck_card", back_populates="decks", cascade="all, delete"
    )
    users: Mapped[List["User"]] = relationship(
        secondary="user_deck", back_populates="decks"
    )
