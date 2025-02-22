from pydantic import BaseModel, Field
from typing import Optional


class CategoryBase(BaseModel):
    title: str = Field(max_length=128)

class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    title: Optional[str] =  Field(None, max_length=128)


class CategoryPublic(CategoryCreate):
    id: int