from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

router = APIRouter(
    prefix="/pages",
    tags=["Page"]
)

templates = Jinja2Templates(directory="templates")


@router.get("/main")
def get_main_page(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

