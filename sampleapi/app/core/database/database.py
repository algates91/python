from core import config
from sqlmodel import create_engine, Session, SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = config.database.database_url

args = {"check_same_thread" : False}

print(f"Database URL {DATABASE_URL}")

async_engine = create_async_engine(DATABASE_URL, echo=True, future=True)

async def init_db() -> None:
    """
    Create database tables for all SQLModel models registered in SQLModel.metadata.
    Call this once at app startup.
    """
    # Ensure models are imported before this is called, e.g. import app.model.user
    async with async_engine.begin() as conn:
        # run_sync runs the synchronous metadata.create_all on the async connection
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_async_session():
    async_session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session