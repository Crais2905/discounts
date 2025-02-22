from fastapi import Depends
from sqlalchemy.future import select
from sqlalchemy import update, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_session
from db.models import Category


class CategoryCrud:
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session

    
    async def get_categories(self, offset: int, limit: int):
        stmt = select(Category).offset(offset).limit(limit)
        return await self.session.scalars(stmt)
    

    