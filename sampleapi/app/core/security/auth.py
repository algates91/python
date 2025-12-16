from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from core import config
from core import setup_custom_logger


SECRET_KEY = config.jwt.secret
ALGORITHM = config.jwt.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = config.jwt.expiry

logger = setup_custom_logger(__name__)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def hash_password(password: str) -> str:
#     return pwd_context.hash(password)

# def verify_password(plain:str, hashed:str) -> bool:
#     return pwd_context.verify(plain,hashed)

def create_access_token(data:dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp':expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str) -> dict:
    data={}
    error_msg = None
    try:
        data = jwt.decode(token=token, key=SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError as e:
        logger.error(f"Error: {e}")
        error_msg = str(e)
    return {"data":data, "error":error_msg}