from fastapi import HTTPException
from sqlalchemy.orm import Session

from wordcards.models.deck import Deck
from wordcards.schemas.deck import DeckData


def create_deck(db: Session, data: DeckData):
    deck = Deck(name=data.name)
    db.flush()
    db.add(deck)
    db.commit()
    return deck


def find_all_decks(db: Session):
    return db.query(Deck).order_by(Deck.pk).all()


def find_deck(db: Session, pk: int):
    deck = db.query(Deck).filter(Deck.pk == pk).first()
    if not deck:
        raise HTTPException(status_code=404, detail="Deck not found")
    return deck


def replace_deck(db: Session, pk: int, data: DeckData):
    deck = db.query(Deck).filter(Deck.pk == pk).first()
    if not deck:
        raise HTTPException(status_code=404, detail="Deck not found")
    deck.name = data.name
    db.commit()
    return deck


def update_deck(db: Session, pk: int, data: DeckData):
    deck = db.query(Deck).filter(Deck.pk == pk).first()
    if not deck:
        raise HTTPException(status_code=404, detail="Deck not found")
    if data.name:
        deck.name = data.name
    db.commit()
    return deck


def delete_deck(db: Session, pk: int):
    result = db.query(Deck).filter(Deck.pk == pk).delete()
    if not result:
        raise HTTPException(status_code=404, detail="Deck not found")
    db.commit()
    return {"success": True}
