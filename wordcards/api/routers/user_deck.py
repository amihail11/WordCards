from fastapi import APIRouter

from wordcards.database import DbSession
from wordcards.schemas.user_deck import UserDeckData
from wordcards.services import user_deck

user_deck_router = APIRouter(prefix="/user_deck", tags=["user_deck"])


@user_deck_router.post("", status_code=201)
async def create_user_deck(db: DbSession, data: UserDeckData):
    return user_deck.create_user_deck(db=db, data=data)


@user_deck_router.get("")
async def find_all_users_decks(db: DbSession):
    return user_deck.find_all_users_decks(db=db)


@user_deck_router.get("/{pk}")
async def find_user_deck(db: DbSession, pk: int):
    return user_deck.find_user_deck(db=db, pk=pk)


@user_deck_router.put("/{pk}")
async def replace_user_deck(db: DbSession, pk: int, data: UserDeckData):
    return user_deck.replace_user_deck(db=db, pk=pk, data=data)


@user_deck_router.patch("/{pk}")
async def update_user_deck(db: DbSession, pk: int, data: UserDeckData):
    return user_deck.update_user_deck(db=db, pk=pk, data=data)


@user_deck_router.delete("/{pk}", status_code=204)
async def delete_deck_card(db: DbSession, pk: int):
    return user_deck.delete_user_deck(db=db, pk=pk)
