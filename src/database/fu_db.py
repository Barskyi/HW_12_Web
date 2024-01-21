from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase

from src.database.db import sessionmanamger
from src.entity.models import User


async def get_db() -> AsyncGenerator[AsyncSession, None]:  # Асинхронна функція для отримання сесії бази даних
    async with sessionmanamger.session() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_db)):
    yield SQLAlchemyUserDatabase(session, User)
