from time import localtime, mktime, strftime

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from wordcards.models.user_card import UserCard
from wordcards.schemas.user_card import UserCardData


def create_user_card(db: Session, data: UserCardData):
    user_card = UserCard(
        user_id=data.user_id,
        card_id=data.card_id,
        demo_time=data.demo_time,
        study_day=data.study_day,
        status=data.status,
    )
    try:
        db.flush()
        db.add(user_card)
        db.commit()
        return user_card
    except IntegrityError as e:
        raise HTTPException(
            status_code=400, detail="Integrity constraint violation"
        ) from e


def find_all_user_cards(db: Session):
    return db.query(UserCard).order_by(UserCard.pk).all()


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


def grade_answer(db: Session, pk: int, grade: str):
    answer_time = localtime()
    user_card = db.query(UserCard).filter(UserCard.pk == pk).first()
    if grade == "dont_know":
        if user_card.status == "learn":
            interval = 60
            next_demo = interval + mktime(answer_time)
            user_card.demo_time = strftime("%Y-%m-%d %H:%M:%S", localtime(next_demo))
        elif user_card.status == "revise":
            interval = 360
            next_demo = interval + mktime(answer_time)
            user_card.demo_time = strftime("%Y-%m-%d %H:%M:%S", localtime(next_demo))
            user_card.status = "learn"
        else:
            interval = 60
            next_demo = interval + mktime(answer_time)
            user_card.demo_time = strftime("%Y-%m-%d %H:%M:%S", localtime(next_demo))
            user_card.status = "learn"
    elif grade == "difficult":
        if user_card.status == "revise":
            interval = (2.5 * user_card.study_day + 1) * 86400 / 1.5
            next_demo = interval + mktime(answer_time)
            user_card.demo_time = strftime("%Y-%m-%d %H:%M:%S", localtime(next_demo))
            user_card.study_day += 1
        elif user_card.status == "learn":
            interval = (2.5 * user_card.study_day + 1) * 86400 / 2
            next_demo = interval + mktime(answer_time)
            user_card.demo_time = strftime("%Y-%m-%d %H:%M:%S", localtime(next_demo))
            user_card.study_day += 1
        else:
            interval = 300
            next_demo = interval + mktime(answer_time)
            user_card.demo_time = strftime("%Y-%m-%d %H:%M:%S", localtime(next_demo))
            user_card.status = "learn"
    elif grade == "good":
        if user_card.status == "revise":
            interval = (2.5 * user_card.study_day + 1) * 86400
            next_demo = interval + mktime(answer_time)
            user_card.demo_time = strftime("%Y-%m-%d %H:%M:%S", localtime(next_demo))
            user_card.study_day += 1
        elif user_card.status == "learn":
            interval = (2.5 * user_card.study_day + 1) * 86400
            next_demo = interval + mktime(answer_time)
            user_card.demo_time = strftime("%Y-%m-%d %H:%M:%S", localtime(next_demo))
            user_card.study_day += 1
        else:
            interval = 300
            next_demo = (2.5 * user_card.study_day + 1) * 86400
            user_card.demo_time = strftime("%Y-%m-%d %H:%M:%S", localtime(next_demo))
            user_card.status = "learn"
    else:
        if user_card.status == "revise":
            interval = (2.5 * user_card.study_day + 1) * 86400 * 1.3
            next_demo = interval + mktime(answer_time)
            user_card.demo_time = strftime("%Y-%m-%d %H:%M:%S", localtime(next_demo))
            user_card.study_day += 1
        elif user_card.status == "learn":
            interval = (2.5 * user_card.study_day + 1) * 86400 * 1.3
            next_demo = interval + mktime(answer_time)
            user_card.demo_time = strftime("%Y-%m-%d %H:%M:%S", localtime(next_demo))
            user_card.study_day += 1
        else:
            interval = 300
            next_demo = (2.5 * user_card.study_day + 1) * 86400 * 1.3
            user_card.demo_time = strftime("%Y-%m-%d %H:%M:%S", localtime(next_demo))
            user_card.status = "learn"
    db.commit()
    return user_card
