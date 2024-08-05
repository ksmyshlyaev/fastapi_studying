from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import DBSettings

db_settings = DBSettings()

DB_URL = (
    f'postgresql+asyncpg://{db_settings.USER}:{db_settings.PASS}@{db_settings.HOST}:{db_settings.PORT}'
    f'/{db_settings.NAME}')

engine = create_async_engine(DB_URL)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
