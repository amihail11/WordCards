"""
The module for creating card schema
"""

from pydantic import BaseModel


class CardData(BaseModel):
    """Represents Cards data types for valcard_idation"""

    pk: int | None = None
    word: str
    meaning: str
