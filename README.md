# 🧱 Task Planner — Hexagonal Architecture with FastAPI & PostgreSQL

This project is a clean, testable task planner built using Python 3.11, FastAPI, and PostgreSQL.  
It follows **hexagonal architecture** (also known as **Ports and Adapters**) and applies **SOLID** and **Clean Architecture** principles.

---

## 📁 Project Structure
```
organizer/
└── task_planner/
├── application/ # Core business logic
│ ├── exceptions/ # Custom domain/application exceptions
│ ├── ports/ # Interfaces for adapters
│ │ ├── driving/ # Entry-point interfaces (e.g. controller ports)
│ │ └── driven/ # Outbound interfaces (e.g. repository ports)
│ └── services/ # Use cases (business service layer)
├── domain/
│ └── models/ # Domain entities and value objects
├── driven/ # Outbound adapters (e.g. database, messaging)
│ └── postgres_repository/
│ ├── adapters/ # Concrete repository implementations
│ ├── config/ # Pydantic models for adapter config
│ ├── mappers/ # Domain ↔ Adapter mapping logic
│ └── models/ # Models for persistence layer
├── driving/ # Entry-point adapters (e.g. REST API)
│ └── api_rest/
│ ├── adapters/ # REST controller logic
│ ├── config/ # API configuration models
│ ├── mappers/ # Request/response ↔ domain model mapping
│ ├── models/ # Request/Response DTOs
│ └── postman/ # (Optional) Postman collections
├── boot/ # Application bootstrap (main entrypoint)
│ ├── config/ # Loads application.yml and env settings
│ ├── docker/ # docker-compose.yml and infra setup
│ ├── injectors/ # Dependency injection config
│ └── resources/
│ └── i18n/ # Translation files
├── main.py # Microservice entry point
└── tests/ # Unit & integration tests
└── unit/
```

---

## 📦 Dependencies

Install dependencies with [Poetry](https://python-poetry.org/):

```bash
# Core packages
poetry add fastapi "pydantic>=2.0"

# PostgreSQL & ORM
poetry add asyncpg sqlalchemy[asyncio] alembic

# Development & testing
poetry add --group dev pytest pytest-asyncio httpx uvicorn pre-commit

```
---

## 🔧 Development Setup

### 🛠 Pre-commit Hooks

To ensure code quality and consistency, this project uses [pre-commit](https://pre-commit.com/) to automatically run linters and tests before each commit.

Install and configure the hooks with:

```bash
# Install hook dependencies
poetry install

# Install pre-commit hooks locally
poetry run pre-commit install

# (Optional) Run all hooks manually
poetry run pre-commit run --all-files

```

The following checks are included:

-   ✅ `ruff` --- Linting and formatting

-   ✅ `black` --- Automatic code formatting

-   ✅ `mypy` --- Static type checking

-   ✅ `pytest` --- Runs all unit and integration tests

-   ✅ `check-yaml` --- Ensures YAML files are well-formed

-   ✅ `end-of-file-fixer` --- Ensures newline at end of files


* * * * *

🧩 Domain Objects
-----------------

### 🧱 Entity: `Task`

An **entity** represents a meaningful concept in the business domain.
It has a **unique identity** and encapsulates attributes and behavior.


#### ✅ Attributes

-   `id`: Unique identifier (e.g. `UUID`)

-   `title`: Title of the task

-   `description`: Optional description

-   `priority`: Integer or enum for ordering

-   `completed`: Boolean status

-   `dependencies`: List of IDs of other tasks

-   `created_at`, `updated_at`: Timestamps

#### ✅ Methods

-   `mark_as_completed()` --- Marks the task as complete (if allowed)

-   `add_dependency(task_id)` --- Adds a dependency

-   `remove_dependency(task_id)` --- Removes a dependency

> 💡 All entities are classes, but not all classes are entities. Entities are domain-relevant and maintain identity over time.

* * * * *

### 🔌 Port: `TaskStoragePort`

A **port** is an abstract interface that defines how the domain interacts with the outside world --- without knowing the implementation details.
It lives in the **domain layer**, and is implemented in the **driven layer**.

#### 🔍 Purpose

-   Keeps the domain logic decoupled from infrastructure

-   Allows flexibility in changing storage backends (e.g. PostgreSQL, in-memory)

-   Makes testing easier by enabling mocking or stubbing

#### ✅ Required methods

```
save(task: Task) -> None
get_by_id(task_id: UUID) -> Task
delete(task_id: UUID) -> None
get_all_ready() -> list[Task]        # Tasks with no incomplete dependencies
list_all() -> list[Task]             # Optional: returns all tasks

```

> 🧠 This port represents the contract that must be fulfilled by any adapter (e.g., a repository backed by a database).

* * * * *
