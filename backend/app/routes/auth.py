from fastapi import APIRouter
from app.telegram.client import client

router = APIRouter()

@router.get("/")
async def auth():

    await client.connect()

    if await client.is_user_authorized():
        me = await client.get_me()

        return {
            "status": "funfando",
            "user": me.first_name
        }

    return {
        "status": "nao nao nao aqui nao "
    }