# DE가 QP에 맞춰 데이터를 넘겨주는 API

from fastapi import APIRouter   

router = APIRouter(
    prefix="/data_check",
    tags=["Data Check"]
)

@router.get("/")
async def data_check():
    return {"data": "check"}