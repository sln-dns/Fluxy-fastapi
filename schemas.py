from pydantic import BaseModel, EmailStr, Field
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

# Схема для обновления данных пользователя
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=3)

    class Config:
        orm_mode = True


class GtinQuery(BaseModel):
    gtin: str  # Простой пример, где GTIN - это просто строка

class GtinResponse(BaseModel):
    gtin: str
    name: str  # Название продукта
    description: str  # Описание продукта
    # Добавь другие поля по мере необходимости