from typing import List
from fastapi import Depends
from sqlalchemy.future import select
from sqlalchemy import update, insert, delete, desc
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_session
from db.models import Product
from schemas.product import ProductCreate, ProductUpdate


class ProductCrud:
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session


    async def create_product(self, product_data: ProductCreate):
        stmt = insert(Product).values(product_data.model_dump()).returning(Product)
        result = await self.session.execute(stmt)
        await self.session.commit()     
        inserted_product = result.scalar()
        return inserted_product
    

    async def get_products(self, offset: int, limit: int, sorted_by_time: bool,  filters: List = []):
        stmt = select(Product)
        if filters:
            stmt = stmt.where(*filters)
        if sorted_by_time:
            stmt = stmt.order_by(Product.end_date)
        stmt = stmt.offset(offset).limit(limit)
        return await self.session.scalars(stmt)
    

    async def get_product(self, product_id: int):
        stmt = select(Product).where(Product.id == product_id)
        return await self.session.scalar(stmt)


    async def delete_product(self, product_id: int):
        stmt = delete(Product).where(Product.id == product_id).returning(Product)
        result = await self.session.execute(stmt)
        await self.session.commit()     
        deleted_product = result.scalar()
        return deleted_product