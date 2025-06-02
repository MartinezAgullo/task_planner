from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class Task(BaseModel):
    id: UUID
    title: str
    description: str
    priority: int
    completed: bool
    dependencies: list[UUID]
    created_at: datetime
    updated_at: datetime
