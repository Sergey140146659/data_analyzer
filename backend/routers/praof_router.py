from fastapi import APIRouter, Response, Request

router = APIRouter(
    prefix="/praof",
    tags=["praof"]
)


@router.post("/praof")
async def praof(response: Response, obj: dict):
    try:
        return obj["data"]
    except Exception as e:
        response.status_code = 500
        return {"status": "error", "message": str(e)}