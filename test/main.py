from fastapi import FastAPI, Depends, HTTPException, status
from inmemory_db import get_store
from uuid import UUID,uuid4
from request import TaskRead, TaskCreate, ErrorResponse, UserProfile
from typing import Annotated
import uvicorn
from auth import get_current_user, create_jwt_token
from logger import setup_logger
from database import get_session, init_db
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from model import Task
from contextlib import asynccontextmanager

app = FastAPI()

logger = setup_logger(__name__)

@app.get("/")
async def home():
    return {"message":"Welcome to home page"}

@app.get("/tasks", dependencies=[Depends(get_current_user)])
async def getTasks(session: Annotated[AsyncSession, Depends(get_session)]) -> list[Task]:
    logger.info("fetching all tasks")
    result = await session.exec(select(Task))
    return result.all()

@app.post("/tasks", dependencies=[Depends(get_current_user)])
async def addTask(task: TaskCreate, data_store: Annotated[dict[UUID, TaskRead], Depends(get_store)]) -> TaskRead:
    logger.info(f"Adding taks to data store {task}")
    id = uuid4()
    if task.title is not None and len(task.title) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title cannot be empty. Please try again")
    task_toadd = TaskRead(id=id, completed=False, title=task.title)
    data_store[id]=task_toadd
    return task_toadd

@app.get("/task/{task_id}")
async def getTaskByID(task_id:UUID, data_store: Annotated[dict[UUID, TaskRead], Depends(get_store)]) -> TaskRead | ErrorResponse:
    logger.info(f"Fetching task for id - {task_id}")
    if task_id not in data_store:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="No Data found. Please try with valid ID")
    try:
        return data_store[task_id]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Bad data sent")
    
@app.post("/token")
async def get_access_token(data:dict) -> str:
    return create_jwt_token(data)

#@app.on_event("startup")
async def create_tables():
    await init_db()
    print("created tables")

@asynccontextmanager
async def lifespan(app:FastAPI):
    await create_tables()

if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True)