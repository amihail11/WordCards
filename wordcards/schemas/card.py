from pydantic import BaseModel


class CardData(BaseModel):

    pk: int | None = None
    word: str
    meaning: str
