from fastapi import APIRouter
from app.services.history_service import save_history, get_history

router = APIRouter()


@router.post("/save-history")
def save_user_history(
    user_id: str,
    category: str,
    details: str,
    result: str
):
    save_history(user_id, category, details, result)

    return {
        "message": "History saved successfully"
    }


@router.get("/history")
def user_history(user_id: str):
    return {
        "user_id": user_id,
        "history": get_history(user_id)
    }