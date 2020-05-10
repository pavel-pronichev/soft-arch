from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette_exporter import PrometheusMiddleware, handle_metrics

from app import crud
from app.schemas import UserCreate, UserMain, UserUpdate
from database.db import SessionLocal

app = FastAPI()

app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.get("/health")
async def health():
    return {"status": "OK"}


@app.post("/users", response_model=UserMain)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return crud.create_user(db, user)


@app.get("/users", response_model=List[UserMain])
def all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip, limit)


@app.get("/users/{user_id}", response_model=UserMain)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user


@app.put("/users/{user_id}", response_model=UserMain)
def change_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.update_user(db, db_user, user)


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.delete_user(db, db_user)
