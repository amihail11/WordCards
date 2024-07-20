from sqlalchemy import Column, ForeignKey, Integer, Table

from wordcards.database import Base

card_deck = Table(
    "cards_decks",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("card_id", ForeignKey("cards.id")),
    Column("deck_id", ForeignKey("decks.id")),
)
