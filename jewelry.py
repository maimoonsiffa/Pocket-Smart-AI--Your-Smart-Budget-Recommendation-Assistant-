from fastapi import APIRouter
from app.services.recommendation_service import get_recommendation

router = APIRouter()


@router.post("/generate-jewelry")
def generate_jewelry(details: str):
    result = get_recommendation("Jewelry", details)
    return {
        "category": "Jewelry",
        "recommendation": result
    }
    