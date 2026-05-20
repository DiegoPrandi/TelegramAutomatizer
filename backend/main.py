from fastapi import FastAPI
from app.routes.auth import router as authRouter
from app.routes.accounts import router as accountsRouter
from app.database.initializeDb import init_db
from app.routes.messages import router as messagesRouter

app = FastAPI()
init_db()

app.include_router(authRouter, prefix="/auth")
app.include_router(accountsRouter, prefix="/accounts")
app.include_router(messagesRouter, prefix="/messages")

@app.get("/")
def home():
    return{"message": "Telegram Automatizer"}