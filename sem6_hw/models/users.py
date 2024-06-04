import datetime

from pydantic import BaseModel, Field, EmailStr


class UserIn(BaseModel):
    first_name: str = Field(...,min_length=2, max_length=20)
    last_name: str = Field(...,min_length=2, max_length=20)
    # email: str = Field(..., max_length=50, regex='/^\S+@\S+\.\S+$/')
    email: EmailStr
    password: str = Field(..., min_length=8)


class User(UserIn):
    user_id: int
