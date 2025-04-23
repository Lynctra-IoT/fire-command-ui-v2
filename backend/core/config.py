from functools import lru_cache
from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    SECRET_KEY: str = "CHANGE_ME_SUPER_SECRET"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./fire_command.db")
    CORS_ORIGINS: list[str] = ["*"]

    class Config:
        case_sensitive = True

@lru_cache
def get_settings() -> Settings:
    return Settings()
