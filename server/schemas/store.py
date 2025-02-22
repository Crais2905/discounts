from pydantic import BaseModel, Field
from typing import Optional


class StoreCreate(BaseModel):
    name: str = Field(max_length=128)
    url: str = Field(max_length=256)


class StoreUpdate(BaseModel):
    name: Optional[str] = Field(default=None, max_length=128)
    url: Optional[str] = Field(default=None, max_length=256)


class StorePublic(StoreCreate):
    id: int   