"""Module for creating CRUD functions"""

from fastapi import HTTPException
from sqlalchemy.orm import Session

from wordcards.models.card import Card
from wordcards.schemas.card import CardData


def create_card(db: Session, card: CardData):
    db_card = Card(word=card.word, meaning=card.meaning)
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card


def find_card(db: Session, card_id: int):
    db_card = db.query(Card).filter(Card.card_id == card_id).first()
    if not db_card:
        raise HTTPException(status_code=404, detail="Card not found")
    return db_card


def find_all_cards(db: Session):
    all_cards = db.query(Card).order_by(Card.card_id).all()
    return all_cards


def replace_card(db: Session, card_id, card: CardData):
    db_card = db.query(Card).filter(Card.card_id == card_id).first()
    if not db_card:
        raise HTTPException(status_code=404, detail="Card not found")
    db_card.word = card.word
    db_card.meaning = card.meaning
    db.commit()
    return db_card


def update_card(db: Session, card_id, card: CardData):
    db_card = db.query(Card).filter(Card.card_id == card_id).first()
    if not db_card:
        raise (HTTPException(status_code=404, detail="Card not found"))
    if card.word:
        db_card.word = card.word
    if card.meaning:
        db_card.meaning = card.meaning
    db.commit()
    return db_card


def delete_card(db: Session, card_id: int):
    result = db.query(Card).filter(Card.card_id == card_id).delete()
    if not result:
        raise HTTPException(status_code=404, detail="Card not found")
    db.commit(result)
    return {"success": True}
