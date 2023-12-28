from sqlalchemy.orm import Session

from models import models
from schemas import schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.userid == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserBase):

    db_user = models.User(username= user.username,
                          email=user.email,
                          password=user.password,
                          registrationdate=user.registrationdate,
                          )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).get(user_id)
    if db_user is None:
        raise ValueError(f"User with ID {user_id} does not exist.")
    db.delete(db_user)
    db.commit()

def update_user(db: Session, user: schemas.UserBase, user_id:int):
    db_user = db.query(models.User).get(user_id)
    if db_user is None:
        raise ValueError(f"User with ID {user.id} does not exist.")
    db_user.username = user.username or db_user.username
    db_user.email = user.email or db_user.email
    db_user.password = user.password or db_user.password
    db_user.registrationdate = user.registrationdate or db_user.registrationdate
    db.commit()
    db.refresh(db_user)
    return db_user