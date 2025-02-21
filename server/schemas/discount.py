from pydantic import BaseModel, Field, PastDatetime, FutureDatetime
from typing import Optional
from datetime import datetime


class DiscountCreate(BaseModel):
    old_price: int = Field(gt=0)
    new_price: int = Field(ge=0)
    discount_percent: int
    start_date: datetime
    end_date: datetime
    product_id: int 


class DiscountUpdate(BaseModel):
    old_price: Optional[int] = Field(gt=0)
    new_price: Optional[int] = Field(ge=0)
    discount_percent: Optional[int]
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    product_id: Optional[int]


class DiscountPublic(DiscountCreate):
    id: int   
