from pydantic import BaseModel


class UserData(BaseModel):
    pk: int | None = None
    name: str
    login: str
    password: str
