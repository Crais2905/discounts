from fastapi import Depends
from sqlalchemy.future import select
from sqlalchemy import update, insert, delete
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