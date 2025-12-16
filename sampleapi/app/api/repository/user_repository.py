
from sqlmodel.ext.asyncio.session import AsyncSession
from ..model.user import User
from sqlmodel import select, delete
from fastapi import Depends
from core.database.database import get_async_session


class UserRepo:

    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create(self, user:User):
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
    
    async def getAll(self):
        statement = select(User)
        result = await self.session.exec(statement)
        return result.all()
    
    async def delete_by_id(self, user_id:int):
        statement = select(User).where(User.id == user_id)
        result = await self.session.exec(statement=statement)
        user = result.one()
        await self.session.delete(user)
        await self.session.commit()
        return user



def get_user_repository(session: AsyncSession = Depends(get_async_session)) -> UserRepo:
    """FastAPI dependency factory that provides a `UserService` with an active session."""
    return UserRepo(session)
