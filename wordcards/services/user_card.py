from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from wordcards.models.user_card import UserCard
from wordcards.schemas.user_card import UserCardData


def create_user_card(db: Session, data: UserCardData):
    user_card = UserCard(user_id=data.user_id, card_id=data.card_id)
    try:
        db.flush()
        db.add(user_card)
        db.commit()
    except IntegrityError as e:
        raise HTTPException(
            status_code=400, detail="Integrity constraint violation"
        ) from e


def find_all_users_cards(db: Session):
    return db.query(UserCard).order_by(UserCard.pk).all


def find_user_card(db: Session, pk: int):
    user_card = db.query(UserCard).filter(UserCard.pk == pk).first()
    if not user_card:
        raise HTTPException(status_code=404, detail="User card not found")
    return user_card


def replace_user_card(db: Session, pk: int, data: UserCardData):
    user_card = db.query(UserCard).filter(UserCard.pk == pk).first()
    if not user_card:
        raise HTTPException(status_code=404, detail="User card not found")
    user_card.user_id = data.user_id
    user_card.card_id = data.card_id
    db.commit()
    return user_card


def update_user_card(db: Session, pk: int, data: UserCardData):
    user_card = db.query(UserCard).filter(UserCard.pk == pk).first()
    if not user_card:
        raise HTTPException(status_code=404, detail="User card not found")
    if data.user_id:
        user_card.user_id = data.user_id
    if data.card_id:
        user_card.card_id = data.card_id
    db.commit()
    return user_card


def delete_user_card(db: Session, pk: int):
    result = db.query(UserCard).filter(UserCard.pk == pk).delete()
    if not result:
        raise HTTPException(status_code=404, detail="User card not found")
    db.commit()
    return {"success": True}
