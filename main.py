from fastapi import FastAPI, Request, Body
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Dict, Any

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


@app.get("/edit/{profile_id}", response_class=HTMLResponse)
async def edit_profile(request: Request, profile_id: str):
    return templates.TemplateResponse(
        "edit_profile.html", {"request": request, "profile_id": profile_id}
    )


@app.get("/view/{profile_id}", response_class=HTMLResponse)
async def view_resume(request: Request, profile_id: str):
    return templates.TemplateResponse(
        "index.html", {"request": request, "profile_id": profile_id}
    )


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
