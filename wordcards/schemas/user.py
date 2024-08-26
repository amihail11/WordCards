from pydantic import BaseModel


class UserData(BaseModel):
    pk: int | None = None
    name: str
    password: str
