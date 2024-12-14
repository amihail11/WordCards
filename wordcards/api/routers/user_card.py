from fastapi import APIRouter

from wordcards.database import DbSession
from wordcards.schemas.user_card import UserCardData
from wordcards.services import user_card

user_card_router = APIRouter(prefix="/user_card", tags=["user_card"])


@user_card_router.post("", status_code=201)
async def create_user_card(db: DbSession, data: UserCardData):
    return user_card.create_user_card(db=db, data=data)


@user_card_router.get("")
async def find_all_user_cards(db: DbSession):
    return user_card.find_all_user_cards(db=db)


@user_card_router.get("/{pk}")
async def find_user_card(db: DbSession, pk: int):
    return user_card.find_user_card(db=db, pk=pk)


@user_card_router.put("/{pk}")
async def replace_user_card(db: DbSession, pk, data: UserCardData):
    return user_card.replace_user_card(db=db, pk=pk, data=data)


@user_card_router.patch("/{pk}")
async def update_user_card(db: DbSession, pk: int, data: UserCardData):
    return user_card.replace_user_card(db=db, pk=pk, data=data)


@user_card_router.delete("/{pk}")
async def delete_user_card(db: DbSession, pk: int):
    return user_card.delete_user_card(db=db, pk=pk)


# @user_card_router.post("/{pk}")
# async def set_demo_time(db: DbSession, pk: int, grade: str):
#     return user_card.set_demo_time(db=db, pk=pk, grade=grade)
