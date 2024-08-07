from pydantic import BaseModel


class DeckCardData(BaseModel):
    pk: int | None = None
    deck_id: int
    card_id: int
