from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional,List

app = FastAPI()


class User(BaseModel):
    email: str
    is_active: bool
    bio:Optional[str]

@app.get("/users")
async def get_users():
    return {"message": "Hi"}


@app.post("/users")
async def create_user():
    return {"message": "Hi"}
