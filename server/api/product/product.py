from fastapi import APIRouter, Depends, HTTPException, status, UploadFile
from ..services.product_crud import ProductCrud
from schemas.product import ProductCreate, ProductPublic, ProductUpdate
from utils.filters import product_filters

import os
import uuid

router = APIRouter()


@router.post("/", response_model=ProductPublic, status_code=status.HTTP_201_CREATED)
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


@router.patch("/image/{product_id}", response_model=ProductPublic)
async def add_product_image(
    product_id: int,
    image: UploadFile, 
    product_crud: ProductCrud = Depends(ProductCrud)
):
    product = await product_crud.get_product(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    
    file_extension = image.filename.split('.')[-1]
    if file_extension not in ['jpg', 'png', 'jpeg']:
        raise HTTPException(status_code=400, detail="Unsupported extension")
    
    file_path = os.path.join('static/product', f'{uuid.uuid4()}.{file_extension}')
    with open(file_path, 'wb') as file:
        file.write(image.file.read())

    product.image_url = file_path
    product_crud.session.add(product)
    await product_crud.session.commit()
    await product_crud.session.refresh(product)
    return product


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: int,
    product_crud: ProductCrud = Depends(ProductCrud)
):
    product = await product_crud.get_product(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')

    return await product_crud.delete_product(product_id)