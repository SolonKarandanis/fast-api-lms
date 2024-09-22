import fastapi
from pydantic import BaseModel
from typing import Optional,List

router = fastapi.APIRouter()

class User(BaseModel):
    email: str
    is_active: bool
    bio:Optional[str]

@router.get("/users")
async def get_users():
    return {"message": "Hi"}


@router.get("/users/{id}")
async def get_user(id: int):
    return {"message": "Hi"}

@router.post("/users")
async def create_user():
    return {"message": "Hi"}