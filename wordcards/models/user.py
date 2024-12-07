from typing import TYPE_CHECKING, List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from wordcards.database import Base

if TYPE_CHECKING:
    from .card import Card
    from .deck import Deck


class User(Base):
    __tablename__ = "user"
    pk: Mapped[int] = mapped_column("id", primary_key=True, index=True)
    name: Mapped[str]
    login: Mapped[str]
    password: Mapped[str]
    decks: Mapped[List["Deck"]] = relationship(
        secondary="user_deck", back_populates="users", cascade="all, delete"
    )
    cards: Mapped[List["Card"]] = relationship(
        secondary="user_card", back_populates="users", cascade="all, delete"
    )
