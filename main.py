from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()
staticfiles = StaticFiles(directory="templates")
templates = Jinja2Templates(directory="templates")
app.mount("/static", staticfiles, name="static")


@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("Templates.html", {"request": request, "title": "В гугл уже пригласили", "body_content": "Ну привет! Оно живое!"})




