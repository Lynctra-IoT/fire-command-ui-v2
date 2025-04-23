from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.api.deps import get_db
from backend.schemas.user import UserCreate, UserRead
from backend.crud.user import create as create_user
from backend.models.user import User

router = APIRouter(prefix="/users")

@router.post("/", response_model=UserRead)
async def register(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user_in)
