from fastapi import FastAPI
from api.category.category import router as category_router


app = FastAPI(title='Discounts', version='1.0.0')

app.include_router(category_router, tags=['category'], prefix='/categories')