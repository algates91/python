from fastapi import APIRouter, Depends
from ..model.user import User
from ..service.user_service import get_user_service
from core import setup_custom_logger
from ..utils.user_auth import get_current_user
from typing import Any, Annotated
from ..service.user_service import UserService

router = APIRouter()
logger=setup_custom_logger(__name__) 


@router.get("/", dependencies=[Depends(get_current_user)])
async def get_users(user_service: Annotated[UserService, Depends(get_user_service)]):
    logger.info("Fetching user details from endpoint")
    return await user_service.get_users_from_db()

@router.post("/", dependencies=[Depends(get_current_user)])
async def add_user(user:User, user_service:Annotated[UserService, Depends(get_user_service)]):
    return await user_service.add_user_to_db(user)

@router.delete("/{user_id}", dependencies=[Depends(get_current_user)])
async def delete_user(user_id:int, user_service:Annotated[UserService, Depends(get_user_service)]):
    return await user_service.delete_user_from_db(user_id)