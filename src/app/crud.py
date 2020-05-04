from sqlalchemy.orm import Session

from app.models import User
from app.schemas import UserUpdate, UserCreate


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate):
    user: User = User(**user.dict())
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def update_user(db: Session, user: User, user_schema: UserUpdate):
    if user_schema.email:
        user.email = user_schema.email
    if user_schema.first_name:
        user.first_name = user_schema.first_name
    if user_schema.last_name:
        user.last_name = user_schema.last_name
    if user_schema.middle_name:
        user.middle_name = user_schema.middle_name
    if user_schema.phone:
        user.phone = user_schema.phone

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def delete_user(db: Session, user: User):
    db.delete(user)
    db.commit()

    return
