from .gemini_service import generate_recommendation


def get_recommendation(category: str, details: str):
    prompt = f"""
You are PocketSmart AI, a budget planning and recommendation assistant.

Category: {category}
User details: {details}

Give practical recommendations that match the user's budget and preferences.
Include estimated prices where possible.
Keep the response simple and organized.
"""

    return generate_recommendation(prompt)
    