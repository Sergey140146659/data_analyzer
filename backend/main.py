from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from routers.pages_router import router as router_page
from routers.default_router import router as router_def
from routers.praof_router import router as router_praof

app = FastAPI(
    title="Smart Manual"
)

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

app.include_router(router_page)
app.include_router(router_def)
app.include_router(router_praof)

origins = [
    "http://localhost:8000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)
