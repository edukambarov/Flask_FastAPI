import datetime
from typing import Dict
from pydantic import BaseModel, Field



class OrderIn(BaseModel):
    user_id: int = Field(..., gt=0)
    good_id: int = Field(..., gt=0)
    quantity: int = Field(..., gt=0)
    date: datetime.date = Field(format='%Y-%m-%d')
    status: bool = True

class Order(OrderIn):
    order_id: int
