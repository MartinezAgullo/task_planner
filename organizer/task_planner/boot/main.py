from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from organizer.task_planner.boot.injectors.app.injector import AppContainer
from organizer.task_planner.driving.http_client.routes import add_routers
from organizer.task_planner.boot.handlers.exception_handlers import add_handlers

# Resolve the base path of the current file
base_path = Path(__file__).resolve().parent

# Set the path where config and i18n files are located
yaml_path = base_path / "resources"
# If you implement a GlobalContext, you can store the YAML path here
# GlobalContext().set_var("yaml_files_path", str(yaml_path))

# Create FastAPI app
app = FastAPI()


# Enable CORS for allowed origins (adapt to your frontend URLs)
origins = [
    "http://localhost",
    "http://localhost:3000",  # React por defecto
    "http://localhost:4200",  # Angular por defecto
    "http://localhost:5173",  # Vite (Vue/React moderno)
    "http://127.0.0.1",
    "http://127.0.0.1:8000",  # Por si accedes al backend directamente en navegador
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize and attach the DI container
app_container = AppContainer()
app.app_container = app_container


# Attach use cases to the app context if needed
app.task_use_case = app_container.task_use_case()

# Register exception handlers and routers
add_handlers(app)
add_routers(app)
