from fastapi import APIRouter, Depends, HTTPException, status
from schemas.category import CategoryCreate, CategoryUpdate, CategoryPublic
from ..services.category_crud import CategoryCrud

router = APIRouter()


@router.post('/', response_model=CategoryPublic, status_code=status.HTTP_201_CREATED)
async def create_category(
    category_data: CategoryCreate,
    category_crud: CategoryCrud = Depends(CategoryCrud)
):
    return await category_crud.create_category(category_data)


@router.get("/", response_model=list[CategoryPublic])
async def get_categories(
    offset: int = 0,
    limit: int = 10,
    category_crud: CategoryCrud = Depends(CategoryCrud)
):
    return await category_crud.get_categories(offset, limit)


@router.get("/{category_id}", response_model=CategoryPublic)
async def get_category(
    category_id: int,
    category_crud: CategoryCrud = Depends(CategoryCrud)
):
    category = await category_crud.get_category(category_id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return category


@router.put("/{category_id}", response_model=CategoryPublic)
async def full_update_category(
    category_id: int,
    category_data: CategoryCreate,
    category_crud: CategoryCrud = Depends(CategoryCrud)
):
    category = await category_crud.get_category(category_id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return  await category_crud.update_category(category_data, category_id)


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(
    category_id: int,
    category_crud: CategoryCrud = Depends(CategoryCrud)
):
    category = await category_crud.get_category(category_id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    await category_crud.delete_category(category_id)
    return