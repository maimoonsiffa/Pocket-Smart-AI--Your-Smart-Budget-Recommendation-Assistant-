from fastapi import APIRouter

router = APIRouter()


@router.get("/startup")
def startup():
    return {
        "message": "PocketSmart AI backend started successfully",
        "status": "success"
    }