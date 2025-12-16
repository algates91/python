from fastapi import Depends, HTTPException, APIRouter
from core.security.auth import create_access_token


auth_router = APIRouter()

user_info_ldap = {
    "sub":"test_123",
    "role":"test user",
    "permissions":"read"
}

@auth_router.post("/token")
async def get_token():
    access_token = create_access_token(
        data=user_info_ldap
    )

    return {
        "auth_token":access_token,
        "type":"Bearer"
    }
