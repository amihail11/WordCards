"""Module for creating CRUD functions"""

from fastapi import HTTPException
from sqlalchemy.orm import Session

from wordcards.models.card import Card
from wordcards.schemas.card import CardData


def create_card(db: Session, card: CardData):
    """create a new card"""
    db_card = Card(word=card.word, meaning=card.meaning)
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card


def read_card(db: Session, card_id: int):
    """read the card with the given ID"""
    db_card = db.query(Card).filter(Card.card_id == card_id).first()
    if not db_card:
        raise HTTPException(status_code=404, detail="Card not found")
    return db_card


def read_all_cards(db: Session):
    """read all cards from the database"""
    all_cards = db.query(Card).order_by(Card.card_id).all()
    return all_cards


def delete_card(db: Session, card_id: int):
    """delete the card with the given ID"""
    result = db.query(Card).filter(Card.card_id == card_id).delete()
    if not result:
        raise HTTPException(status_code=404, detail="Card not found")
    db.commit(result)
    return {"success": True}
