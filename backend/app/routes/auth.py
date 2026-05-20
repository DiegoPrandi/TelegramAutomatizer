from fastapi import APIRouter
from app.telegram.client import criarClient

router = APIRouter()

@router.get("/")
async def auth():

    await criarClient.connect()

    if await criarClient.is_user_authorized():
        me = await criarClient.get_me()

        return {
            "status": "funfando",
            "user": me.first_name
        }

    return {
        "status": "nao nao nao aqui nao "
    }