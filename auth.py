from fastapi import APIRouter
from app.services.auth_service import hash_password, verify_password

router = APIRouter()

users = {}


@router.post("/register")
def register(username: str, password: str):
    if username in users:
        return {"message": "User already exists"}

    users[username] = hash_password(password)

    return {"message": "Registration successful"}


@router.post("/login")
def login(username: str, password: str):
    if username not in users:
        return {"message": "User not found"}

    if not verify_password(password, users[username]):
        return {"message": "Invalid password"}

    return {"message": "Login successful"}