from fastapi import FastAPI
from app.core.config import settings
from app.core.db import database

app = FastAPI(title="🔥 Fire Command Center API v2")

@app.on_event("startup")
async def startup_event():
    await database.connect()

@app.on_event("shutdown")
async def shutdown_event():
    await database.disconnect()

@app.get("/")
async def root():
    return {"message": "🔥 Fire Command Center API v2 Running!"}
