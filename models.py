from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.now)

class ShortLink(Base):
    __tablename__ = 'short_links'

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(Text)
    short_code = Column(String, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)

    user = relationship("User", back_populates="short_links")

class Visit(Base):
    __tablename__ = 'visits'

    id = Column(Integer, primary_key=True, index=True)
    short_link_id = Column(Integer, ForeignKey('short_links.id'))
    visited_at = Column(DateTime, default=datetime.now)
    visitor_info = Column(Text)  # Это примерное поле, можно добавить детальнее посетителя.

    short_link = relationship("ShortLink", back_populates="visits")

# Добавим связи в класс User и ShortLink
User.short_links = relationship("ShortLink", back_populates="user", cascade="all, delete")
ShortLink.visits = relationship("Visit", back_populates="short_link", cascade="all, delete")
