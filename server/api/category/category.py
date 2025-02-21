from fastapi import APIRouter



router = APIRouter()


@router.get("/")
async def first_end(q: str):
    return {"message": q}