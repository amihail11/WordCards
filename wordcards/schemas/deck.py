from pydantic import BaseModel


class DeckData(BaseModel):

    pk: int | None = None
    name: str
