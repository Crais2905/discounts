from fastapi import APIRouter, Depends, HTTPException, status, UploadFile
from ..services.product_crud import ProductCrud
from schemas.product import ProductCreate, ProductPublic, ProductUpdate
from utils.filters import product_filters

router = APIRouter()


@router.post("/", response_model=ProductPublic)
async def create_product(
    product_data: ProductCreate,
    product_crud: ProductCrud = Depends(ProductCrud)
):
    return await product_crud.create_product(product_data)


@router.get("/", response_model=list[ProductPublic])
async def get_products(
    offset: int = 0,
    limit: int = 10,
    sorted_by_date: bool = False,
    filters: dict = Depends(product_filters),
    product_crud: ProductCrud = Depends(ProductCrud)
):  
    if offset < 0 or limit < 0: 
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="offset and limit must be greater than 0")
    return await product_crud.get_products(offset, limit, sorted_by_date, filters)


@router.get('/{product_id}', response_model=ProductPublic)
async def get_product(
    product_id: int,
    product_crud: ProductCrud = Depends(ProductCrud)
):
    product = await product_crud.get_product(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product


# @router.patch("/{procduct_id}", response_model=ProductPublic)
# async def add_product_image(
#     product_id: int,
#     image: UploadFile, 
#     product_crud: ProductCrud = Depends(ProductCrud)
# ):
#     product = await product_crud.get_item(product_id)
#     if not product:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
