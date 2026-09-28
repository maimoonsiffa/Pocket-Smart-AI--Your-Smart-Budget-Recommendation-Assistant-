from fastapi import APIRouter
from app.services.recommendation_service import get_recommendation

router = APIRouter()


@router.get("/recommendations-details")
def recommendations_details(category: str, details: str):
    result = get_recommendation(category, details)

    return {
        "category": category,
        "recommendation": result
    }
    