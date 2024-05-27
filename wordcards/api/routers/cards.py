"""
The module for creating cards routers
"""

from fastapi import APIRouter

from wordcards.api.services import crud
from wordcards.database import DbSession
from wordcards.schemas.card import CardData

router = APIRouter(prefix="/cards", tags=["cards"])


@router.post("/new")
async def create_card(db: DbSession, card: CardData):
    """create a new card in the database"""
    return crud.create_card(db=db, card=card)


@router.get("/")
async def read_all_cards(db: DbSession):
    """show all cards from the database"""
    return crud.read_all_cards(db=db)


@router.get("/{card_id}/")
async def read_card(db: DbSession, card_id: int):
    """get a card from the database using its ID"""
    return crud.read_card(db=db, card_id=card_id)


@router.delete("/{card_id}")
async def delete_card(db: DbSession, card_id: int):
    """delete the card with the given ID from the database"""
    return crud.delete_card(db=db, card_id=card_id)
