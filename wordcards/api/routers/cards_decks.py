from fastapi import APIRouter

from wordcards.database import DbSession
from wordcards.services import cards_decks

card_deck_router = APIRouter(prefix="/cards_decks", tags=["cards_decks"])


@card_deck_router.get("")
async def find_all_card_decks(db: DbSession):
    return cards_decks.find_all_card_decks(db=db)
