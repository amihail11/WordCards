from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from wordcards.database import Base


class UserDeck(Base):
    __tablename__ = "user_deck"

    pk: Mapped[int] = mapped_column("id", primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    deck_id: Mapped[int] = mapped_column(ForeignKey("deck.id"))

    __table_args__ = (UniqueConstraint("user_id", "deck_id", name="unique_user_deck"),)
