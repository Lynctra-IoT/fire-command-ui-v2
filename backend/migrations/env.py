from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context
import os, sys, configparser

sys.path.append(os.getcwd())
from backend.db.base import Base
from backend.models import user, client, device, alarm, device_status  # noqa: F401

config = context.config

# ── Safe logging: only call fileConfig if config has logger sections ──
if config.config_file_name and os.path.exists(config.config_file_name):
    cp = configparser.ConfigParser()
    cp.read(config.config_file_name)
    if cp.has_section("loggers"):
        fileConfig(config.config_file_name)
# ---------------------------------------------------------------------

target_metadata = Base.metadata

def _sync_url():
    url = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./fire_command.db")
    return url.replace("sqlite+aiosqlite", "sqlite").replace("postgresql+asyncpg", "postgresql")

def run_migrations_offline():
    context.configure(url=_sync_url(),
                      target_metadata=target_metadata,
                      literal_binds=True,
                      dialect_opts={"paramstyle": "named"})
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    engine = create_engine(_sync_url(), poolclass=pool.NullPool)
    with engine.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
