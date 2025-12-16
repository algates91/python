from sqlmodel import SQLModel, Field
from uuid import UUID

class Task(SQLModel, table=True):
    id: UUID = Field(primary_key=True, index=True)
    title: str
    completed: bool