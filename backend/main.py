from fastapi import FastAPI
from app.routes.auth import router as authRouter

app = FastAPI()

app.include_router(authRouter, prefix="/auth")

@app.get("/")
def home():
    return{"message": "Telegram Automatizer"}