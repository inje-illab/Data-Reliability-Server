from fastapi import APIRouter
from ..api import DataSendtoQP
from ..api import DataSendtoST

router = APIRouter(
    prefix="/data_quality_manager",
    tags=["Data Quality Manager"]
)

@router.get("/")
async def data_quality_manager():
    return {"data": "quality_manager"}