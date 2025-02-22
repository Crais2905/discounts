from pydantic import BaseModel, Field
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
    old_price: Optional[int] = Field(default=None, gt=0)
    new_price: Optional[int] = Field(default=None, ge=0)
    discount_percent: Optional[int] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    product_id: Optional[int] = None


class DiscountPublic(DiscountCreate):
    id: int   
