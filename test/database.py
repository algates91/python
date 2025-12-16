from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import text, SQLModel

DATABASE_URL="sqlite+aiosqlite:///./test.db"

async_engine = create_async_engine(url=DATABASE_URL, echo=True)
asyncSessionPool = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False)

async def get_session():
    async with asyncSessionPool() as session:
        yield session

async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)