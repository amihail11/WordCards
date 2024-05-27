"""
The module for creating modes methods"""

from fastapi import HTTPException

from wordcards.database import DbSession
from wordcards.models.card import Card


def check_meaning(db: DbSession, a_word: str, user_answer: str):
    """check the user's input meaning of a random foreign word from a random database card"""
    word_card = db.query(Card).filter(Card.word == a_word).first()
    if not word_card:
        raise HTTPException(
            status_code=404, detail="No card with this foreign word found."
        )
    if user_answer.lower() == word_card.meaning.lower():
        return {"message": "Correct!"}
    return {"message": f"The word '{a_word}' means '{word_card.meaning}'"}
