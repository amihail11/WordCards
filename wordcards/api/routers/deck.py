from fastapi import APIRouter

from wordcards.database import DbSession
from wordcards.schemas.deck import DeckData
from wordcards.services import deck

deck_router = APIRouter(prefix="/deck", tags=["deck"])


@deck_router.post("", status_code=201)
async def create_deck(db: DbSession, data: DeckData):
    return deck.create_deck(db=db, data=data)


@deck_router.get("")
async def find_all_decks(db: DbSession):
    return deck.find_all_decks(db=db)


@deck_router.get("/{pk}")
async def find_deck(db: DbSession, pk: int):
    return deck.find_deck(db=db, pk=pk)


@deck_router.put("/{pk}")
async def replace_deck(db: DbSession, pk: int, data: DeckData):
    return deck.replace_deck(db=db, pk=pk, data=data)


@deck_router.patch("/{pk}")
async def update_deck(db: DbSession, pk: int, data: DeckData):
    return deck.update_deck(db=db, pk=pk, data=data)


@deck_router.delete("/{pk}", status_code=204)
async def delete_deck(db: DbSession, pk: int):
    return deck.delete_deck(db=db, pk=pk)
