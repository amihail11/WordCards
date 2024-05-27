"""
The module for creating modes routes
"""

from fastapi import HTTPException
from sqlalchemy.sql.expression import func

from wordcards.api.app import app
from wordcards.api.services.modes_methods import check_meaning
from wordcards.database import DbSession
from wordcards.models.card import Card
from wordcards.schemas.answer import UserAnswer


@app.get("/learn/random-card")
async def get_random_card(db: DbSession):
    """get a random card card from the database for learning"""
    random_card = db.query(Card).order_by(func.random()).first()
    if not random_card:
        raise HTTPException(status_code=404, detail="No card found")
    return random_card


@app.get("/card/check-mode")
async def check_answer(db: DbSession, user_input: UserAnswer):
    """check the user's input meaning of a random  foreign word"""
    random_card = db.query(Card).order_by(func.random()).first()
    if not random_card:
        raise HTTPException(status_code=404, detail="No card found")
    random_word = random_card.word
    return check_meaning(db, random_word, user_input.answer)
