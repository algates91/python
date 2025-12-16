from datetime import datetime, timedelta
from jose import jwt, JWTError


SECRET_KEY="changeme"
ALGORITHM="HS256"
EXPIRY_TIME_IN_MINUTES=300

def create_access_token(data:dict) -> str:
    to_encode = data.copy()
    expiry_time = datetime.utcnow() + timedelta(minutes=EXPIRY_TIME_IN_MINUTES)
    to_encode.update({'exp':expiry_time})
    return jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token:str) -> dict:
    try:
        return jwt.decode(token=token,key=SECRET_KEY,algorithms=[ALGORITHM])
    except JWTError as e:
        raise e
    

if __name__ == '__main__':
    data = {"user":"anand"}
    token = create_access_token(data)
    print(token)
    print(decode_token(token))
