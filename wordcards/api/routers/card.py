from fastapi import APIRouter

from wordcards.database import DbSession
from wordcards.schemas.card import CardData
from wordcards.services import card

card_router = APIRouter(prefix="/card", tags=["card"])


@card_router.post("", status_code=201)
async def create_card(db: DbSession, data: CardData):
    return card.create_card(db=db, data=data)


@card_router.get("")
async def find_all_cards(db: DbSession):
    return card.find_all_cards(db=db)


@card_router.get("/random")
async def find_random_card(db: DbSession):
    return card.find_random_card(db=db)


@card_router.get("/{pk}")
async def find_card(db: DbSession, pk: int):
    return card.find_card(db=db, pk=pk)


@card_router.put("/{pk}")
async def replace_card(db: DbSession, pk: int, data: CardData):
    return card.replace_card(db=db, pk=pk, data=data)


@card_router.patch("/{pk}")
async def update_card(db: DbSession, pk: int, data: CardData):
    return card.update_card(db=db, pk=pk, data=data)


@card_router.delete("/{pk}")
async def delete_card(db: DbSession, pk: int):
    return card.delete_card(db=db, pk=pk)


@card_router.get("/{pk}/check")
async def check_answer(db: DbSession, pk: int, data: CardData):
    return card.check_answer(db=db, pk=pk, data=data)


@card_router.get("/{pk}/card_side")
async def get_card_side(db: DbSession, pk: int):
    return card.get_card_side(db=db, pk=pk)
