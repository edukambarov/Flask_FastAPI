from pydantic import BaseModel, Field


class UserIn(BaseModel):
    username: str = Field(...,max_length=50)
    email: str = Field(..., max_length=50)
    password: str = Field(..., min_length=8)


class User(BaseModel):
    id: int
    username: str = Field(..., max_length=50)
    email: str = Field(..., max_length=50)
    password: str = Field(..., min_length=8)
