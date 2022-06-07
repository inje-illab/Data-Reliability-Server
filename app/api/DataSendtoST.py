# 체크된 데이터를 STARTrip Queue에 던지는 API

from fastapi import APIRouter

router = APIRouter(
    prefix="/data_send_to_st",
    tags=["Data Send to ST"]
)

@router.get("/")
async def data_send_to_st():
    return {"data": "send_to_st"}