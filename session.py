from fastapi import APIRouter

router = APIRouter()


@router.get("/session-info")
def session_info():
    return {
        "logged_in": False,
        "message": "Session information"
    }


@router.get("/session-data")
def session_data():
    return {
        "user": None,
        "data": []
    }
    