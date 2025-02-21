from pydantic import BaseModel, Field
from typing import Optional



class CategoryCreate(BaseModel):
    title: str = Field(max_length=128)


class CategoryUpdate(BaseModel):
    title: Optional[str] =  Field(max_length=128)


class CategoryPublic(CategoryCreate):
    id: int