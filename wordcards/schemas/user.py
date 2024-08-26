from pydantic import BaseModel


class User(BaseModel):
    pk: int | None = None
    name: str
    password: str
