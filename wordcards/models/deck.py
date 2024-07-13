from sqlalchemy.orm import Mapped, mapped_column

from wordcards.database import Base


class Deck(Base):
    __tablename__ = "decks"

    pk: Mapped[int] = mapped_column("id", primary_key=True, index=True)
    name: Mapped[str]
