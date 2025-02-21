from pydantic import BaseModel, Field
from typing import Optional
from .category import CategoryPublic
from .store import StorePublic
from .discount import DiscountPublic


class ProductBase(BaseModel):
    name: str = Field(max_length=128)
    price: float = Field(ge=0)
    image_url: str = Field(max_length=256)


class ProductCreate(ProductBase):
    current_discount_id: int
    store_id: int
    category_id: int


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(max_length=128)
    price:  Optional[float] = Field(ge=0)
    image_url: Optional[str] = Field(max_length=256)
    current_discount_id: Optional[int]
    store_id: Optional[int]
    category_id: Optional[int]


class ProductPublic(ProductBase):
    id: int
    discount: DiscountPublic
    category: CategoryPublic
    store: StorePublic