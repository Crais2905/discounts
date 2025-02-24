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
    store = await store_crud.get_store(store_id)
    if not store:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Store not found')
    return await store_crud.get_store(store_id)


@router.patch("/{store_id}", response_model=StorePublic)
async def part_update_store(
    store_id: int,
    store_data: StoreUpdate,
    store_crud: StoreCrud = Depends(StoreCrud)
):
    store = await store_crud.get_store(store_id)
    if not store:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Store not found')
    return await store_crud.update_store(store_id, store_data)