from fastapi import APIRouter, Response, Request

router = APIRouter(
    prefix="/default",
    tags=["Default"]
)


@router.get("/default")
async def deafult(response: Response):
    try:
        return "Засунул проект акос"
    except Exception as e:
        response.status_code = 500
        return {"status": "error", "message": str(e)}