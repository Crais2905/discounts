from fastapi import Depends
from sqlalchemy.future import select
from sqlalchemy import update, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_session
from schemas.store import StoreCreate, StoreUpdate
from db.models import Store

class StoreCrud():
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session

    
    async def create_store(self, store_data: StoreCreate):
        stmt = insert(Store).values(store_data.model_dump()).returning(Store)
        result = await self.session.execute(stmt)
        await self.session.commit()     
        inserted_store = result.scalar()
        return inserted_store
    

    async def get_stores(self, offset: int, limit: int):
        stmt = select(Store).offset(offset).limit(limit)
        return await self.session.scalars(stmt)
    

    async def get_store(self, store_id: int):
        stmt = select(Store).where(Store.id == store_id)
        return await self.session.scalar(stmt)