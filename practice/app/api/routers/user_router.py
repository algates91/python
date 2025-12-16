from fastapi import APIRouter, Depends
from ..service.user_service import UserService,get_user_service
from typing import Annotated
from app.core import get_current_user, setup_logger

user_router = APIRouter()
logger = setup_logger(__name__)

@user_router.get("/")
async def home():
    return {"message":"User API is running"} 

@user_router.get("/allusers", dependencies=[Depends(get_current_user)])
async def get_users(service:Annotated[UserService, Depends(get_user_service)]):
    logger.info("Fetching all users from database")
    return await service.getAllUsersFromDB()