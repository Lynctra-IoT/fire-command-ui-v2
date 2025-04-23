from sqlalchemy import String, Integer, Boolean, DateTime, Enum, func
from sqlalchemy.orm import Mapped, mapped_column
import enum
from backend.db.base import Base

class Role(str, enum.Enum):
    admin = "admin"
    responder = "responder"
    technician = "technician"

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    full_name: Mapped[str] = mapped_column(String, nullable=True)
    role: Mapped[Role] = mapped_column(Enum(Role), default=Role.responder)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
