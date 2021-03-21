from sqlalchemy.orm import Session

from . import models, schemas
from .helper import *


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_hashed_password(plain_text_password=user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_home_works(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.HomeWork).offset(skip).limit(limit).all()


def create_user_home_work(db: Session, home_work: schemas.HomeWorkCreate, user_id: int):
    db_home_work = models.HomeWork(**home_work.dict(), owner_id=user_id)
    db.add(db_home_work)
    db.commit()
    db.refresh(db_home_work)

    return db_home_work
