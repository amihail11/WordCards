from fastapi import APIRouter

from wordcards.database import DbSession
from wordcards.schemas.deck_card import DeckCardData
from wordcards.services import deck_card

deck_card_router = APIRouter(prefix="/deck_card", tags=["deck_card"])


@deck_card_router.post("")
async def create_deck_card(db: DbSession, data: DeckCardData):
    return deck_card.create_deck_card(db=db, data=data)


@deck_card_router.get("")
async def find_all_decks_cards(db: DbSession):
    return deck_card.find_all_decks_cards(db=db)


@deck_card_router.get("/{pk}")
async def find_deck_card(db: DbSession, pk: int):
    return deck_card.find_deck_card(db=db, pk=pk)


@deck_card_router.put("/{pk}")
async def replace_deck_card(db: DbSession, pk: int, data: DeckCardData):
    return deck_card.replace_deck_card(db=db, pk=pk, data=data)


@deck_card_router.patch("/{pk}")
async def update_deck_card(db: DbSession, pk: int, data: DeckCardData):
    return deck_card.update_deck_card(db=db, pk=pk, data=data)


@deck_card_router.delete("/{pk}")
async def delete_deck_card(db: DbSession, pk: int):
    return deck_card.delete_deck_card(db=db, pk=pk)
