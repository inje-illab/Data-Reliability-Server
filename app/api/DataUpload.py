# 데이터를 upload하는 API

from fastapi import APIRouter

router = APIRouter(
    prefix="/data_upload",
    tags=["Data Upload"]
)

@router.get("/")
async def data_upload():
    return {"data": "upload"}