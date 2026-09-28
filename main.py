from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="app/templates")
from fastapi import Request

import os

from app.routes import (
    home,
    party,
    jewelry,
    auth,
    session,
    recommendations,
    history,
    startup
)

app = FastAPI(title="PocketSmart: AI Budget Planner")
templates = Jinja2Templates(directory="app/templates")

SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")


app.include_router(home.router)
app.include_router(party.router)
app.include_router(jewelry.router)
app.include_router(auth.router)
app.include_router(session.router)
app.include_router(recommendations.router)
app.include_router(history.router)
app.include_router(startup.router)

@app.get("/")
def home_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )

