from fastapi import FastAPI
from api.category.category import router as category_router
from api.store.store import router as store_router
from db.session import engine
from db.models import Base


app = FastAPI(title='Discounts', version='1.0.0')

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(category_router, tags=['category'], prefix='/categories')
app.include_router(store_router, tags=['store'], prefix='/stories')


