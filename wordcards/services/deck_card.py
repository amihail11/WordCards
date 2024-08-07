from fastapi import HTTPException
from sqlalchemy.orm import Session

from wordcards.models.deck_card import DeckCard
from wordcards.schemas.deck_card import DeckCardData


def create_deck_card(db: Session, data: DeckCardData):
    deck_card = DeckCard(deck_id=data.deck_id, card_id=data.card_id)
    db.flush()
    db.add(deck_card)
    db.commit()
    return deck_card


def find_all_decks_cards(db: Session):
    return db.query(DeckCard).all()


def find_deck_card(db: Session, pk: int):
    deck_card = db.query(DeckCard).filter(DeckCard.pk == pk).first()
    if not deck_card:
        raise HTTPException(status_code=404, detail="Deck card not found")
    return deck_card


def replace_deck_card(db: Session, pk: int, data: DeckCardData):
    deck_card = db.query(DeckCard).filter(DeckCard.pk == pk).first()
    if not deck_card:
        raise HTTPException(status_code=404, detail="Deck card not found")
    deck_card.deck_id = data.deck_id
    deck_card.card_id = data.card_id
    db.commit()
    return deck_card


def update_deck_card(db: Session, pk: int, data: DeckCardData):
    deck_card = db.query(DeckCard).filter(DeckCard.pk == pk).first()
    if not deck_card:
        raise HTTPException(status_code=404, detail="Deck card not found")
    if data.deck_id:
        deck_card.deck_id = data.deck_id
    if data.card_id:
        deck_card.card_id = data.card_id
    db.commit()
    return deck_card


def delete_deck_card(db: Session, pk: int):
    result = db.query(DeckCard).filter(DeckCard.pk == pk).delete()
    if not result:
        raise HTTPException(status_code=404, detail="Deck card not found")
    return {"success": True}
