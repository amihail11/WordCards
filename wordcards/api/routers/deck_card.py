from fastapi import APIRouter

from wordcards.database import DbSession
from wordcards.services import deck_card

card_deck_router = APIRouter(prefix="/deck_card", tags=["deck_card"])


@card_deck_router.get("")
async def find_all_decks_cards(db: DbSession):
    return deck_card.find_all_decks_cards(db=db)
