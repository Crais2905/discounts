from fastapi import Depends
from sqlalchemy.future import select
from sqlalchemy import update, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_session
from db.models import Category, Product
from schemas.category import CategoryCreate, CategoryUpdate

class CategoryCrud:
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session

    
    async def create_category(self, category_data: CategoryCreate):
        stmt = insert(Category).values(category_data.model_dump()).returning(Category)
        result = await self.session.execute(stmt)
        await self.session.commit()
        inserted_category = result.scalar()
        return inserted_category


    async def get_categories(self, offset: int, limit: int):
        stmt = select(Category).offset(offset).limit(limit)
        return await self.session.scalars(stmt)
    

    async def get_category(self, category_id):
        stmt = select(Category).where(Category.id == category_id)
        return await self.session.scalar(stmt)
    

    async def update_category(self, category_data: CategoryUpdate, category_id: int):
        values = category_data.model_dump(exclude_unset=True)
        stmt = update(Category).where(Category.id == category_id).values(values).returning(Category)
        result = await self.session.execute(stmt)
        await self.session.commit()
        inserted_category = result.scalar()
        return inserted_category
    

    async def delete_category(self, category_id: int):
        stmt = delete(Category).where(Category.id == category_id).returning(Category)
        stmt_products = delete(Product).where(Product.category_id == category_id).returning(Product)

        async with self.session as conn:
            try:
                stmt_result = await conn.execute(stmt)
                stmt_products_result = await conn.execute(stmt_products)
                await conn.commit()
            except Exception as error:
                await conn.rollback()
                raise error

        result = [stmt_result.scalar(), stmt_products_result.scalars().all()]
        return result

    