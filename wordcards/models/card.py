from typing import TYPE_CHECKING, List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from wordcards.database import Base

if TYPE_CHECKING:
    from .deck import Deck
    from .user import User


class Card(Base):

    __tablename__ = "card"

    pk: Mapped[int] = mapped_column("id", primary_key=True, index=True)
    word: Mapped[str]
    meaning: Mapped[str]
    decks: Mapped[List["Deck"]] = relationship(
        secondary="deck_card", back_populates="cards"
    )
    users: Mapped[List["User"]] = relationship(
        secondary="user_card", back_populates="cards"
    )
