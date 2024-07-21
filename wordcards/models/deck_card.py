from sqlalchemy import Column, ForeignKey, Integer, Table

from wordcards.database import Base

deck_card = Table(
    "deck_card",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("card_id", ForeignKey("card.id")),
    Column("deck_id", ForeignKey("deck.id")),
)
