from fastapi import APIRouter

from wordcards.database import DbSession
from wordcards.schemas.user import UserData
from wordcards.services import user

user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.post("")
async def create_user(db: DbSession, data: UserData):
    return user.create_user(db=db, data=data)


@user_router.get("")
async def find_all_users(db: DbSession):
    return user.find_all_users(db=db)


@user_router.get("/{pk}")
async def find_user(db: DbSession, pk: int):
    return user.find_user(db=db, pk=pk)


@user_router.put("/{pk}")
async def replace_user(db: DbSession, pk: int, data: UserData):
    return user.replace_user(db=db, pk=pk, data=data)


@user_router.patch("/{pk}")
async def update_user(db: DbSession, pk: int, data: UserData):
    return user.update_user(db=db, pk=pk, data=data)


@user_router.delete("/{pk}")
async def delete_user(db: DbSession, pk: int):
    return user.delete_user(db=db, pk=pk)
