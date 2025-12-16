from ..model.user import User
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from fastapi import Depends
from typing import Annotated
from app.core import get_async_session

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def getAllUsers(self) -> list[User]:
        statement = select(User)
        result = await self.session.exec(statement)
        return result.all()

def get_user_repository(session: Annotated[AsyncSession, Depends(get_async_session)]) -> UserRepository:
    return UserRepository(session)
