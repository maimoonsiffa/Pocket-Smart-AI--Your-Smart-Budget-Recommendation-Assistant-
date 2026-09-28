import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = None

if API_KEY and API_KEY != "YOUR_API_KEY_HERE":
    client = genai.Client(api_key=API_KEY)


def generate_recommendation(prompt: str):

    if client is None:
        return (
            "PocketSmart AI Recommendation\n\n"
            "Your request was received successfully.\n"
            "A budget-friendly recommendation can be prepared "
            "based on your requirements.\n\n"
            "Note: Gemini AI is not connected yet. "
            "Add a valid Gemini API key later to enable AI recommendations."
        )

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            
            contents=prompt
        )

        return response.text

    except Exception as e:
        return (
            "PocketSmart AI Recommendation\n\n"
            "Your planner request was received successfully.\n"
            "Gemini connection is currently unavailable.\n"
            "Please add a valid Gemini API key to enable AI recommendations."
        )
