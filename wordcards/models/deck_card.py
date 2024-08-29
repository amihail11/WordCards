from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from wordcards.database import Base

if TYPE_CHECKING:
    from .card import Card
    from .deck import Deck


class DeckCard(Base):

    __tablename__ = "deck_card"

    pk: Mapped[int] = mapped_column("id", primary_key=True, index=True)
    deck_id: Mapped[int] = mapped_column(ForeignKey("deck.id"))
    card_id: Mapped[int] = mapped_column(ForeignKey("card.id"))

    __table_args__ = (UniqueConstraint("deck_id", "card_id", name="unique_deck_card"),)
