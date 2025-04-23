from logging.config import fileConfig
from sqlalchemy import pool
from alembic import context
import asyncio, os, sys, importlib

sys.path.append(os.getcwd())
from backend.db.base import Base
from backend.models import user, client, device, alarm, audit_log  # noqa

config = context.config
fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migrations_offline():
    url = context.get_x_argument(as_dictionary=True).get('DB_URL') or os.getenv('DATABASE_URL')
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = context.config.attributes.get("connection", None)
    if connectable is None:
        from sqlalchemy.ext.asyncio import create_async_engine
        url = os.getenv('DATABASE_URL')
        connectable = create_async_engine(url, poolclass=pool.NullPool)

    async def do_run_migrations(connection):
        context.configure(connection=connection, target_metadata=target_metadata)
        async with context.begin_transaction():
            await context.run_migrations()

    asyncio.run(do_run_migrations(connectable))

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
