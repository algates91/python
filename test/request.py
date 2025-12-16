from pydantic import BaseModel
from uuid import UUID, uuid4

class TaskCreate(BaseModel):
    title: str

class TaskRead(BaseModel):
    id: UUID
    title: str
    completed: bool

class ErrorResponse(BaseModel):
    error_msg: str

class UserProfile(BaseModel):
    name:str
    role:str
    active:bool = True