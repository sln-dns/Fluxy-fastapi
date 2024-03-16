from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.orm import sessionmaker

from models import Base
from database import DATABASE_URL

async def create_tables(engine: AsyncEngine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    engine = create_async_engine(DATABASE_URL, echo=True)
    import asyncio
    asyncio.run(create_tables(engine))
