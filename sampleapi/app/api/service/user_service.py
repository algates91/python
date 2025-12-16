from ..model.user import User
from ..repository.user_repository import UserRepo, get_user_repository
from fastapi import Depends

class UserService:
    def __init__(self, user_repository:UserRepo) -> None:
        self.repo = user_repository

    async def get_users_from_db(self):
        return await self.repo.getAll()
    
    async def add_user_to_db(self, user:User):
        return await self.repo.create(user)
    
    async def delete_user_from_db(self, user_id:int):
        return await self.repo.delete_by_id(user_id)

def get_user_service(user_repository: UserRepo = Depends(get_user_repository)) -> UserService:
    return UserService(user_repository=user_repository)
