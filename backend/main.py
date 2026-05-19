from fastapi import FastAPI
from app.routes.auth import router as authRouter
from app.routes.accounts import router as accountsRouter

app = FastAPI()

app.include_router(authRouter, prefix="/auth")
app.include_router(accountsRouter, prefix="/accounts")

@app.get("/")
def home():
    return{"message": "Telegram Automatizer"}