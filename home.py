from fastapi import APIRouter
from app.services.recommendation_service import get_recommendation

router = APIRouter()


@router.post("/generate-home")
def generate_home(details: str):
    result = get_recommendation("Home Interior", details)
    return {
        "category": "Home Interior",
        "recommendation": result
    }