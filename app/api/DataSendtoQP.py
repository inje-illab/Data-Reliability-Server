# DQM이 QP로 데이터 체크

from fastapi import APIRouter

router = APIRouter(
    prefix="/data_send_to_qp",
    tags=["Data Send to QP"]
)

@router.get("/")
async def data_send_to_qp():
    return {"data": "send_to_qp"}