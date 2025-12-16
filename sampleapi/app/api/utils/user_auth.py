from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from core import decode_token
from typing import Annotated


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    payload = decode_token(token)
    print(payload)
    if payload['error']:
        error_msg = payload['error']
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=payload['error']
        )
    return payload['data']

