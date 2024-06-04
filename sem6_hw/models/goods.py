import datetime

from pydantic import BaseModel, Field


class GoodIn(BaseModel):
    name: str = Field(...,min_length=2, max_length=25)
    description: str = Field(...,min_length=2, max_length=100)
    price: float = Field(..., gt=0)


class Good(GoodIn):
    good_id: int
