from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    username: str
    email: str
    password: str