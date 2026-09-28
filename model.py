from pydantic import BaseModel


class RecommendationRequest(BaseModel):
    category: str
    details: str


class RecommendationResponse(BaseModel):
    category: str
    recommendation: str
