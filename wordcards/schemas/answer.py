"""
The module for creating answer schema
"""

from pydantic import BaseModel


class UserAnswer(BaseModel):
    """Represents user's answer data types for validation"""

    answer: str
