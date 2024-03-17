from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Схема для создания пользователя (регистрации)
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Схема для представления пользователя без пароля
class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

# Схема для ответов аутентификации, может включать токен доступа и тип токена
class Token(BaseModel):
    access_token: str
    token_type: str

# Схема для данных пользователя при аутентификации
class TokenData(BaseModel):
    email: Optional[EmailStr] = None
