from fastapi import APIRouter, Depends, HTTPException, status
from ..services.store_crud import StoreCrud
from schemas.store import StoreCreate, StorePublic, StoreUpdate

router = APIRouter()


@router.post("/", response_model=StorePublic)
async def create_store(
    store_data: StoreCreate,
    store_crud: StoreCrud = Depends(StoreCrud)
):
    return await store_crud.create_store(store_data)


@router.get("/", response_model=list[StorePublic])
async def get_stories(
    offset: int = 0,
    limit: int = 5,
    store_crud: StoreCrud = Depends(StoreCrud)
):
    return await store_crud.get_stores(offset, limit)


@router.get("/{store_id}", response_model=StorePublic)
async def get_store(
    store_id: int,
    store_crud: StoreCrud = Depends(StoreCrud)
):
    return await store_crud.get_store(store_id)