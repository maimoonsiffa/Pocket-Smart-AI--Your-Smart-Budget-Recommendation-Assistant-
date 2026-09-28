from fastapi import APIRouter
from app.services.recommendation_service import get_recommendation

router = APIRouter()


@router.post("/generate-party")
def generate_party(details: str):
    result = get_recommendation("Party Planning", details)
    return {
        "category": "Party Planning",
        "recommendation": result
    }
    