from sqlmodel.ext.asyncio.session import AsyncSession
from ..model.user import User
from typing import Annotated
from fastapi import Depends
from ..repository.user_repository import UserRepository, get_user_repository

class UserService:
    def __init__(self, repo:UserRepository):
        self.repo = repo
    
    async def getAllUsersFromDB(self) -> list[User]:
        return await self.repo.getAllUsers()
    
def get_user_service(user_repo: Annotated[UserRepository, Depends(get_user_repository)]) -> UserService:
    return UserService(user_repo)
