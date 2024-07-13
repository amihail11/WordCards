from fastapi import APIRouter

from wordcards.database import DbSession
from wordcards.schemas.deck import DeckData
from wordcards.services import decks

deck_router = APIRouter(prefix="/decks", tags=["decks"])


@deck_router.post("")
async def create_deck(db: DbSession, data: DeckData):
    return decks.create_deck(db=db, data=data)


@deck_router.get("")
async def find_all_decks(db: DbSession):
    return decks.find_all_decks(db=db)


@deck_router.get("/{pk}")
async def find_deck(db: DbSession, pk: int):
    return decks.find_deck(db=db, pk=pk)


@deck_router.put("/{pk}")
async def replace_deck(db: DbSession, pk: int, data: DeckData):
    return decks.replace_deck(db=db, pk=pk, data=data)


@deck_router.patch("/{pk}")
async def update_deck(db: DbSession, pk: int, data: DeckData):
    return decks.update_deck(db=db, pk=pk, data=data)


@deck_router.delete("/{pk}")
async def delete_deck(db: DbSession, pk: int):
    return decks.delete_deck(db=db, pk=pk)
