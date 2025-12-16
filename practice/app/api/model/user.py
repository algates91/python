from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id:int = Field(primary_key=True, index=True)
    name: str | None
    email: str | None
    password: str
