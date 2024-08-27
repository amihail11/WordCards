from fastapi import HTTPException
from sqlalchemy import exc
from sqlalchemy.orm import Session

from wordcards.models.user_deck import UserDeck
from wordcards.schemas.user_deck import UserDeckData


def create_user_deck(db: Session, data: UserDeckData):
    user_deck = UserDeck(user_id=data.user_id, deck_id=data.deck_id)
    try:
        db.flush()
        db.add(user_deck)
        db.commit()
        return user_deck
    except exc.IntegrityError as e:
        raise HTTPException(status_code=400, detail="Bad request") from e


def find_all_users_decks(db: Session):
    return db.query(UserDeck).order_by(UserDeck.pk).all()


def find_user_deck(db: Session, pk: int):
    user_deck = db.query(UserDeck).filter(UserDeck.pk == pk).first()
    if not user_deck:
        raise HTTPException(status_code=404, detail="User deck not found")
    return user_deck


def replace_user_deck(db: Session, pk: int, data: UserDeckData):
    user_deck = db.query(UserDeck).filter(UserDeck.pk == pk).first()
    if not user_deck:
        raise HTTPException(status_code=404, detail="User deck not found")
    user_deck.user_id = data.user_id
    user_deck.deck_id = data.deck_id
    db.commit()
    return user_deck


def update_user_deck(db: Session, pk: int, data: UserDeckData):
    user_deck = db.query(UserDeck).filter(UserDeck.pk == pk).first()
    if not user_deck:
        raise HTTPException(status_code=404, detail="User deck not found")
    if data.user_id:
        user_deck.user_id = data.user_id
    if data.deck_id:
        user_deck.deck_id = data.deck_id
    db.commit()
    return user_deck


def delete_user_deck(db: Session, pk: int):
    result = db.query(UserDeck).filter(UserDeck.pk == pk).delete()
    if not result:
        raise HTTPException(status_code=404, detail="User deck not found")
    db.commit()
    return {"success": True}
