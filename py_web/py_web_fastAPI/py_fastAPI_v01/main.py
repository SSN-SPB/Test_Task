from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Dict

app = FastAPI(
    title="User Service",
    version="1.0.0"
)

# Simulated database
users: Dict[int, dict] = {}


class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserResponse(UserCreate):
    id: int


@app.get("/health")
def health():
    return {"status": "ok", "message": "User Service is running"}


@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    user_id = len(users) + 1

    users[user_id] = {
        "id": user_id,
        "name": user.name,
        "email": user.email,
    }

    return users[user_id]


@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    user = users.get(user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@app.get("/users")
def list_users():
    return list(users.values())