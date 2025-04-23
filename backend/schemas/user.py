from pydantic import BaseModel, EmailStr, Field
from enum import Enum
from datetime import datetime

class Role(str, Enum):
    admin = "admin"
    responder = "responder"
    technician = "technician"

class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None
    role: Role = Role.responder
    is_active: bool = True

class UserCreate(UserBase):
    password: str = Field(min_length=8)

class UserRead(UserBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}
