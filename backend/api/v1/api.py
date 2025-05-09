from fastapi import APIRouter
from backend.api.v1.endpoints import auth, users

api_router = APIRouter()
api_router.include_router(auth.router, tags=["auth"])
api_router.include_router(users.router, tags=["users"])
