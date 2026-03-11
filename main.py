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


@app.post("/render-form", response_class=HTMLResponse)
async def render_form(request: Request, data: Dict[str, Any] = Body(...)):
    # Render a partial template with the profile data
    return templates.TemplateResponse(
        "partials/edit_form.html", {"request": request, "profile": data}
    )


@app.get("/add-experience", response_class=HTMLResponse)
async def add_experience_block(request: Request, index: int):
    return templates.TemplateResponse(
        "partials/experience_item.html", {"request": request, "index": index}
    )


@app.get("/add-skill-category", response_class=HTMLResponse)
async def add_skill_category_block(request: Request, index: int):
    return templates.TemplateResponse(
        "partials/skill_category_item.html", {"request": request, "index": index}
    )


@app.get("/add-education", response_class=HTMLResponse)
async def add_education_block(request: Request, index: int):
    return templates.TemplateResponse(
        "partials/education_item.html", {"request": request, "index": index}
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
