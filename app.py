from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes.mentor import router

app = FastAPI(title="AI Mentor")

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

app.include_router(router)