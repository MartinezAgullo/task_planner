from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from organizer.task_planner.boot.injectors.app.injector import AppContainer
from organizer.task_planner.driving.api_rest.routes.task_routes import (
    router as task_router,
)
from organizer.task_planner.boot.handlers.exception_handlers import add_handlers

base_path = Path(__file__).resolve().parent
yaml_path = base_path / "resources"

app = FastAPI(
    title="Task Planner API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None,
    openapi_tags=[
        {"name": "Tasks", "description": "Operations related to task management"}
    ],
)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:4200",
    "http://localhost:5173",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app_container = AppContainer()
app_container.init_resources()
app.app_container = app_container

logger = app_container.logger()
logger.info("Task Planner API started")


def add_routers(app: FastAPI) -> None:
    app.include_router(task_router)


add_handlers(app)
add_routers(app)
