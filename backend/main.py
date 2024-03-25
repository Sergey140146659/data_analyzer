from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from routers.default_router import router as router_def
from routers.praof_router import router as router_praof
from routers.first_part_router import router as router_first_part

app = FastAPI(
    title="Data Analyzer"
)

app.mount("/static", StaticFiles(directory="static", html=True), name="static")
app.mount("/PRAOF/praof_pics", StaticFiles(directory="static", html=True), name="praof_pics")

app.include_router(router_def)
app.include_router(router_praof)
app.include_router(router_first_part)

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
