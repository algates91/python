from jose import jwt, JWTError
from fastapi import HTTPException, status, Depends
from datetime import datetime, timedelta, UTC
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
import asyncio



SECRET="testsecret"
ALGORITHM="HS256"
TOKEN_EXPIRY_TIME_IN_MINS = 30



def create_jwt_token(data: dict) -> str | None:
    to_encode = data.copy()
    expiry = datetime.now(UTC)+timedelta(TOKEN_EXPIRY_TIME_IN_MINS)
    to_encode.update({"exp":expiry})
    try:
        token = jwt.encode(to_encode,key=SECRET, algorithm=ALGORITHM)
    except JWTError as e:
        print(f"Exception while generating JWT: {str(e)}")
        return None
    return token

def decode_token(token: str) -> dict:
    try:
        return jwt.decode(key=SECRET, algorithms=[ALGORITHM], token=token)
    except JWTError as e:
        print(f"Exception while generating JWT: {str(e)}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> dict:
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token / Token is missing in header")
    return payload
    

if __name__=="__main__":
    data={"name":"Anand","role":"interviewee"}
    token = create_jwt_token(data=data)
    print(token)
    print(decode_token(token))
    test = asyncio.run(get_current_user(token))
    print(test)