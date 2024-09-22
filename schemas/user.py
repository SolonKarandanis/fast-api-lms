from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    role: int


class UserCreate(UserBase):
    ...


class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True