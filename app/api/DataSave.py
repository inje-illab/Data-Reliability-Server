# 업로드 된 데이터 1차 저장

from fastapi import APIRouter

router = APIRouter(
    prefix="/data_save",
    tags=["Data Save"]
)

@router.get("/")
async def data_save():
    return {"data": "save"}