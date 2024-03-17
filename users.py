from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from typing import List

import crud, models, schemas
from database import get_db

router = APIRouter()

@router.post("/users/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    # Проверка, существует ли уже пользователь с таким email
    db_user = await crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    # Хэширование пароля перед сохранением
    hashed_password = bcrypt.hash(user.password)
    # Создание пользователя
    return await crud.create_user(db=db, user=user, hashed_password=hashed_password)
