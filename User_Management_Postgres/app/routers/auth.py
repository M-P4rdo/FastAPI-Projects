from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from app import database, auth, schemas

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login(request: schemas.LoginRequest, db: Session = Depends(database.get_db)):
    user = auth.authenticate_user(db, email=request.email, password=request.password)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    access_token = auth.create_access_token(
        data={"sub": user.email}, expires_delta=timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}

