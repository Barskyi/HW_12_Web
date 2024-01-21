import uuid
from sqlite3 import Date  # 4

from fastapi_users import schemas
from typing import Optional

from pydantic import BaseModel, EmailStr, Field

from src.entity.models import Role


class UserRead(schemas.BaseUser[uuid.UUID]):
    username: str
    lastname: str  # 1
    number: str  # 2
    birthday: Date  # 3


class UserCreate(schemas.BaseUserCreate):
    username: str
    lastname: str  # 1
    number: str  # 2
    birthday: Date  # 3


class UserUpdate(schemas.BaseUserUpdate):
    username: str
    lastname: str  # 1
    number: str  # 2
    birthday: Date  # 3
