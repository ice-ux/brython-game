from pydantic import ValidationError
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:123456@127.0.0.1:3306/codeschl"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = sqlalchemy.orm.declarative_base()

from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from crud import crud
from schemas import schemas
from fastapi import APIRouter

# Base.metadata.create_all(bind=engine)已经创建数据库注释掉

# app = FastAPI()换用apirouter
userrouter = APIRouter(
    prefix="/user",
    tags=["user"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@userrouter.post("/", response_model=schemas.UserBase)
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@userrouter.get("/", response_model=List[schemas.UserBase])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@userrouter.get("{user_id}", response_model=schemas.UserBase)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@userrouter.delete("{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    crud.delete_user(db, user_id=user_id)
    return {"message": "User deleted successfully"}

@userrouter.put("{user_id}")
async def update_user(user_id: int, user:schemas.UserBase, db: Session = Depends(get_db)):
    try:
        existing_user = crud.get_user(db, user_id=user_id)
        if not existing_user:
            raise HTTPException(status_code=404, detail="User not found")
        updated_user = crud.update_user(db, user=user,user_id=user_id)
        return updated_user
    except ValidationError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
