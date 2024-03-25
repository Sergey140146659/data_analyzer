from fastapi import APIRouter, Response, Request

router = APIRouter(
    prefix="/first_part",
    tags=["first part"]
)


@router.post("/data_processing")
async def data_processing(response: Response):
    try:
        return "Засунул проект акос"
    except Exception as e:
        response.status_code = 500
        return {"status": "error", "message": str(e)}