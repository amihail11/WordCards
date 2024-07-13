"""
The module for creating cards routers
"""

from fastapi import APIRouter

from wordcards.database import DbSession
from wordcards.schemas.card import CardData
from wordcards.services import cards

card_router = APIRouter(prefix="/cards", tags=["cards"])


@card_router.post("")
async def create_card(db: DbSession, data: CardData):
    return cards.create_card(db=db, data=data)


@card_router.get("")
async def find_all_cards(db: DbSession):
    return cards.find_all_cards(db=db)


@card_router.get("/{pk}")
async def find_card(db: DbSession, pk: int):
    return cards.find_card(db=db, pk=pk)


@card_router.put("/{pk}")
async def replace_card(db: DbSession, pk: int, data: CardData):
    return cards.replace_card(db=db, pk=pk, data=data)


@card_router.patch("/{pk}")
async def update_card(db: DbSession, pk: int, data: CardData):
    return cards.update_card(db=db, pk=pk, data=data)


@card_router.delete("/{pk}")
async def delete_card(db: DbSession, pk: int):
    return cards.delete_card(db=db, pk=pk)
