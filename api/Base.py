from fastapi import APIRouter, Request
router = APIRouter()


@router.get("/home/{item_id}")
async def home(item_id: int):
    return {'item_id': item_id}