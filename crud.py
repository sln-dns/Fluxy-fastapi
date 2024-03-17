from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete, update
import models
import schemas
from passlib.hash import bcrypt
from sqlalchemy.orm import sessionmaker

# Асинхронные CRUD операции

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(models.User).where(models.User.email == email))
    return result.scalars().first()

async def create_user(db: AsyncSession, user: schemas.UserCreate, hashed_password: str):
    db_user = models.User(email=user.email, username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(models.User).where(models.User.id == user_id))
    return result.scalars().first()

async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(models.User).offset(skip).limit(limit))
    return result.scalars().all()

async def update_user(db: AsyncSession, user_id: int, update_data: dict):
    await db.execute(update(models.User).where(models.User.id == user_id).values(**update_data))
    await db.commit()

async def delete_user(db: AsyncSession, user_id: int):
    await db.execute(delete(models.User).where(models.User.id == user_id))
    await db.commit()
