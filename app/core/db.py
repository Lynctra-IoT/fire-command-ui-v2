from databases import Database
from sqlalchemy import create_engine, MetaData
from app.core.config import settings

database = Database(settings.DATABASE_URL)
metadata = MetaData()
engine = create_engine(str(settings.DATABASE_URL).replace('+aiosqlite', ''), connect_args={"check_same_thread": False})
