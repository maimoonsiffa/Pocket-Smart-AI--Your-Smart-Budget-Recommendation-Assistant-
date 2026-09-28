history = []


def save_history(user_id: str, category: str, details: str, result: str):
    history.append({
        "user_id": user_id,
        "category": category,
        "details": details,
        "result": result
    })


def get_history(user_id: str):
    return [
        item for item in history
        if item["user_id"] == user_id
    ]
    