from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql+asyncpg://localhost/my_fastapi_project_db"

engine = create_async_engine(DATABASE_URL, echo=True)
# Здесь нам необходимо использовать `AsyncSession`, чтобы работать с асинхронной сессией.
AsyncSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

Base = declarative_base()

# Асинхронная функция для получения сессии базы данных.
# Это зависимость, которую ты будешь использовать в твоих путях FastAPI.
async def get_db():
    async with AsyncSessionLocal() as db:
        yield db