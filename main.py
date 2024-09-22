from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
async def get_users():
    return {"message": "Hi"}


@app.post("/users")
async def create_user():
    return {"message": "Hi"}
