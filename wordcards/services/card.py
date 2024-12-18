from time import localtime, strftime

from fastapi import HTTPException
from sqlalchemy.orm import Session, load_only
from sqlalchemy.sql.expression import func

from wordcards.models.card import Card
from wordcards.models.user_card import UserCard
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


def find_random_card(db: Session):
    current_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
    # pylint: disable=E1102
    user_card = (
        db.query(UserCard)
        .filter(UserCard.demo_time <= current_time)
        .order_by(func.random())
        .first()
    )
    card = db.query(Card).filter(Card.pk == user_card.card_id).first()
    return card


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


def check_answer(db: Session, pk: int, data: CardData):
    card = db.query(Card).filter(Card.pk == pk).first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    if data.meaning:
        if data.meaning == card.meaning:
            return {"success": True}, card
        return {"success": False}, card
    raise HTTPException(status_code=400, detail="No data")


def get_card_side(db: Session, pk: int):
    card_side = (
        db.query(Card).filter(Card.pk == pk).options(load_only(Card.word)).first()
    )
    if not card_side:
        raise HTTPException(status_code=404, detail="Card side not found")
    return card_side
