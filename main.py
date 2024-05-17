"""
Main module for WordCards application with routes.

This module contains the main FastAPI application setup, routes, and dependencies for
the application.

"""

from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func

from database import LocalSession, engine
import models


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


class CardData(BaseModel):
    """Represents Cards data types for validation"""

    word: str
    meaning: str


class UserAnswer(BaseModel):
    """Represents user's answer data types for validation"""

    answer: str


def get_db():
    """get database connection"""
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()


DbSession = Annotated[Session, Depends(get_db)]


@app.post("/new_card")
async def create_card(db: DbSession, card: CardData = Depends()):
    """create a new card in the database"""
    db_card = models.Card(foreign_word=card.word, translation=card.meaning)
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return {"message": "Card created"}


@app.get("/all_cards")
async def show_all_cards(db: DbSession):
    """show all cards from the database"""
    cards_from_db = db.query(models.Card).order_by(models.Card.id).all()
    if not cards_from_db:
        raise HTTPException(status_code=404, detail="No card found")
    return cards_from_db


@app.get("/learn/random-card")
async def get_random_card(db: DbSession):
    """get a random card card from the database for learning"""
    random_card = db.query(models.Card).order_by(func.random()).first()
    if not random_card:
        raise HTTPException(status_code=404, detail="No card found")
    return random_card


def check_translation(db: DbSession, a_word: str, user_answer: str):
    """check the user's translation of a random foreign word from a random database card"""
    word_card = db.query(models.Card).filter(models.Card.foreign_word == a_word).first()
    if not word_card:
        raise HTTPException(
            status_code=404, detail="No card with this foreign word found."
        )
    if user_answer.lower() == word_card.translation.lower():
        return {"message": "Correct!"}
    return {"message": f"The word '{a_word}' means '{word_card.translation}'"}


@app.get("/card/check-mode")
async def check_answer(db: DbSession, user_input: UserAnswer = Depends()):
    """check the user's input translation of a random  foreign word"""
    random_card = db.query(models.Card).order_by(func.random()).first()
    if not random_card:
        raise HTTPException(status_code=404, detail="No card found")
    random_word = random_card.foreign_word
    return check_translation(db, random_word, user_input.answer)


@app.put("/card/{id}")
async def update_card(db: DbSession, card_id: int, new_card: CardData = Depends()):
    """update if necessary a foreign word or the meaning of it in the database using its ID"""
    actual_card = db.query(models.Card).filter(models.Card.id == card_id).first()
    if not actual_card:
        raise HTTPException(status_code=404, detail="No card found")
    if actual_card.foreign_word != new_card.word:
        actual_card.foreign_word = new_card.word
    if actual_card.translation != new_card.meaning:
        actual_card.translation = new_card.meaning
    db.commit()
    db.refresh(actual_card)
    return {"message": "The card was updated"}


@app.delete("/card/{card_id}")
async def delete_card(db: DbSession, card_id: int):
    """delete one chosen card from the database using its ID"""
    chosen_card = db.query(models.Card).filter(models.Card.id == card_id).first()
    if not chosen_card:
        raise HTTPException(status_code=404, detail="No card found")
    db.delete(chosen_card)
    db.commit()
    return {"message": "The card was deleted"}


@app.delete("/cards/delete_all")
async def delete_all_cards(db: DbSession):
    """delete all cards from the database"""
    table = db.query(models.Card).all()
    if not table:
        raise HTTPException(status_code=404, detail="No cards in the table found")
    for card in table:
        db.delete(card)
        db.commit()
    return {"message": "All cards deleted"}
