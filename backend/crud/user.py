from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.models.user import User
from backend.schemas.user import UserCreate
from backend.core.security import get_password_hash

async def get_by_email(session: AsyncSession, email: str):
    res = await session.execute(select(User).where(User.email == email))
    return res.scalar_one_or_none()

async def create(session: AsyncSession, obj_in: UserCreate):
    db_obj = User(
        email=obj_in.email,
        hashed_password=get_password_hash(obj_in.password),
        full_name=obj_in.full_name,
        role=obj_in.role,
    )
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj
