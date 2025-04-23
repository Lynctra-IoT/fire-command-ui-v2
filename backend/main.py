from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.db.base import Base
from backend.db.session import engine
from backend.api.v1.api import api_router
import asyncio

app = FastAPI(title="Fire Command Backend – Phase 2")

# Create tables at startup (dev only)
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {"status": "ok"}

# backend/main.py  (add just this block below the existing /health route)

@app.get("/api/health")
async def health_api():
    # identical response so the UI’s /api/health succeeds
    return {"status": "ok"}

app.include_router(api_router, prefix="/api/v1")
