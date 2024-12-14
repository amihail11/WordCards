from fastapi import HTTPException
from sqlalchemy.orm import Session

from wordcards.models.user import User
from wordcards.schemas.user import UserData


def create_user(db: Session, data: UserData):
    user = User(name=data.name, password=data.password, login=data.login)
    db.flush()
    db.add(user)
    db.commit()
    return user


def find_all_users(db: Session):
    return db.query(User).order_by(User.pk).all()


def find_user(db: Session, pk: int):
    user = db.query(User).filter(User.pk == pk).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def replace_user(db: Session, pk: int, data: UserData):
    user = db.query(User).filter(User.pk == pk).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.name = data.name
    user.password = data.password
    db.commit()
    return user


def update_user(db: Session, pk: int, data: UserData):
    user = db.query(User).filter(User.pk == pk).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if data.name:
        user.name = data.name
    if data.password:
        user.password = data.password
    db.commit()
    return user


def delete_user(db: Session, pk: int):
    result = db.query(User).filter(User.pk == pk).delete()
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    db.commit()
    return {"success": True}
