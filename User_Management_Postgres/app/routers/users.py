from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, database
from fastapi import Depends
from app.auth import get_current_user

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[schemas.UserResponse])
def list_users(
    skip: int = 0, limit: int = 10,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserResponse = Depends(get_current_user),
):
    return crud.get_users(db, skip, limit)

@router.get("/{user_id}", response_model=schemas.UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserResponse = Depends(get_current_user),
):
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)

@router.put("/{username}", response_model=schemas.UserResponse)
def update_user(
    username: str,
    user_update: schemas.UserUpdate,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserResponse = Depends(get_current_user),
):
    user = crud.update_user(db, username, user_update)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}", response_model=schemas.UserResponse)
def delete_user(
    user_id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserResponse = Depends(get_current_user)
):
    user = crud.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
