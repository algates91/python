#Use a SQLITE DB.
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import text, SQLModel
import asyncio


DATABASE_URL = "sqlite+aiosqlite:///./test.db"

async_engine = create_async_engine(DATABASE_URL)
AsyncSessionLocal = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False)

async def get_async_session():
    async with AsyncSessionLocal() as session:
        yield session

async def init_db() -> None:
    async with async_engine.begin() as con:
        await con.run_sync(SQLModel.metadata.create_all)
        print("loaded tables")


