from fastapi import APIRouter
from . import board_item

api_router = APIRouter()
api_router.include_router(board_item.router)
