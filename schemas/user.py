from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: str
    username: str
    password: str
    role: int


class UserCreate(UserBase):
    ...


class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str