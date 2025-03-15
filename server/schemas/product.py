from datetime import datetime

from pydantic import BaseModel, Field, field_validator
from typing import Optional
from .category import CategoryPublic
from .store import StorePublic


class ProductBase(BaseModel):
    name: str = Field(max_length=128)
    description: str
    image_url: Optional[str] = Field(None, max_length=256)
    old_price: int = Field(gt=0)
    new_price: int = Field(ge=0)
    discount_percent: int
    url_in_store: str
    


class ProductCreate(ProductBase):
    store_id: int
    category_id: int
    start_date: str
    end_date: str

    @field_validator("start_date", "end_date")
    def parse_custom_date(cls, value):
        try:
            return datetime.strptime(str(value), f"%d-%m-%Y")
        except ValueError:
            raise ValueError("Дата повинна бути у форматі DD-MM-YYYY")


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(default=None,max_length=128)
    price:  Optional[float] = Field(default=None,ge=0)
    image_url: Optional[str] = Field(default=None, max_length=256)
    current_discount_id: Optional[int] = None
    url_in_store: Optional[str] = None
    store_id: Optional[int] = None
    category_id: Optional[int] = None


class ProductPublic(ProductBase):
    id: int
    category: CategoryPublic
    store: StorePublic
    start_date: datetime
    end_date: datetime