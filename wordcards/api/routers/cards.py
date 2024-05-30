"""
The module for creating cards routers
"""

from fastapi import APIRouter

from wordcards.database import DbSession
from wordcards.schemas.card import CardData
from wordcards.services import cards

card_router = APIRouter(prefix="/cards", tags=["cards"])


@card_router.post("/")
async def create_card(db: DbSession, card: CardData):
    return cards.create_card(db=db, card=card)


@card_router.get("/")
async def find_all_cards(db: DbSession):
    return cards.find_all_cards(db=db)


@card_router.get("/{card_id}")
async def find_card(db: DbSession, card_id: int):
    return cards.find_card(db=db, card_id=card_id)


@card_router.put("/{card_id}")
async def replace_card(db: DbSession, card_id, card: CardData):
    return cards.replace_card(db=db, card_id=card_id, card=card)


@card_router.patch("/{card_id}")
async def update_card(db: DbSession, card_id, card: CardData):
    return cards.update_card(db=db, card_id=card_id, card=card)


@card_router.delete("/{card_id}")
async def delete_card(db: DbSession, card_id: int):
    return cards.delete_card(db=db, card_id=card_id)
