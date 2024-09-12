from random import choice

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from wordcards.models.card import Card
from wordcards.schemas.card import CardData


def create_card(db: Session, data: CardData):
    card = Card(word=data.word, meaning=data.meaning)
    db.flush()
    db.add(card)
    db.commit()
    return card


def find_card(db: Session, pk: int):
    card = db.query(Card).filter(Card.pk == pk).first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    return card


def find_all_cards(db: Session):
    all_cards = db.query(Card).order_by(Card.pk).all()
    return all_cards


def replace_card(db: Session, pk, data: CardData):
    card = db.query(Card).filter(Card.pk == pk).first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    card.word = data.word
    card.meaning = data.meaning
    db.commit()
    return card


def update_card(db: Session, pk, data: CardData):
    card = db.query(Card).filter(Card.pk == pk).first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    if data.word:
        card.word = data.word
    if data.meaning:
        card.meaning = data.meaning
    db.commit()
    return card


def delete_card(db: Session, pk: int):
    result = db.query(Card).filter(Card.pk == pk).delete()
    if not result:
        raise HTTPException(status_code=404, detail="Card not found")
    db.commit()
    return {"success": True}


def find_random_word(db: Session):
    cards = db.execute(select(Card.word, Card.meaning)).all()
    return cards
