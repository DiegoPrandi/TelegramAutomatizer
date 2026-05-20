from fastapi import APIRouter
from app.services.message_service import create_message

router = APIRouter()

@router.post("/")
def create(data: dict):

    result = create_message(data)

    return result