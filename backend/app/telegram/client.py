from telethon import TelegramClient
from dotenv import load_dotenv
import os

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

def criarClient(sessionNome: str):

    return TelegramClient(
        f"sessions/{sessionNome}",
        api_id,
        api_hash
    )