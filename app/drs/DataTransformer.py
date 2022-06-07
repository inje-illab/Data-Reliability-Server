from fastapi import APIRouter

router = APIRouter(
    prefix="/data_transformer",
    tags=["Data Transformer"]
)

@router.get("/")
async def data_transformer():
    return {"data": "transformer"}