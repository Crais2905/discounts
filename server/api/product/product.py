from fastapi import APIRouter, Depends, HTTPException, status
from ..services.product_crud import ProductCrud
from schemas.product import ProductCreate, ProductPublic, ProductUpdate

router = APIRouter()


@router.post("/", response_model=ProductPublic)
async def create_product(
    product_data: ProductCreate,
    product_crud: ProductCrud = Depends(ProductCrud)
):
    return await product_crud.create_product(product_data)