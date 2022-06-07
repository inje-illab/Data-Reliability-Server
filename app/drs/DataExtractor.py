from fastapi import APIRouter
from ..api import DataSave

router = APIRouter(
    prefix="/data_extractor",
    tags=["Data Extractor"]
)

@router.get("/")
async def data_extractor():
    return {"data": "extractor"}