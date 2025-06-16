from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from api.category.category import router as category_router
from api.store.store import router as store_router
from api.product.product import router as product_router

from db.session import engine
from db.models import Base


app = FastAPI(title='Discounts', version='1.0.0')

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(category_router, tags=['category'], prefix='/categories')
app.include_router(store_router, tags=['store'], prefix='/stories')
app.include_router(product_router, tags=['product'], prefix='/products')



