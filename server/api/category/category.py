from fastapi import APIRouter, Depends
# from schemas.category import CategoryCreate, CategoryUpdate, CategoryPublic
from ..services.category_crud import CategoryCrud

router = APIRouter()


@router.get("/")
async def get_categories(
    offset: int = 0,
    limit: int = 10,
    category_crud: CategoryCrud = Depends(CategoryCrud)
):
    return await category_crud.get_categories(offset, limit)
