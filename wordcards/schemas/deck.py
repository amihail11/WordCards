"""
The module for creating deck schema
"""

from pydantic import BaseModel


class DeckData(BaseModel):

    pk: int | None = None
    name: str
