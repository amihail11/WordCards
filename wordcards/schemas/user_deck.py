from pydantic import BaseModel


class UserDeckData(BaseModel):
    pk: int | None = None
    user_id: int
    deck_id: int
