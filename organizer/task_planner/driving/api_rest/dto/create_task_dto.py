from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID


# This model defines the expected payload from the client when creating a new task.
class CreateTaskRequestDTO(BaseModel):
    title: str = Field(..., example="Buy groceries")
    description: Optional[str] = Field(None, example="Milk, eggs, bread")
    due_date: Optional[str] = Field(None, example="2025-06-10T12:00:00Z")  # ISO 8601
    priority: Optional[int] = Field(None, example=2)


# This model defines the response returned to the client after the task is successfully created.
class CreateTaskResponseDTO(BaseModel):
    id: UUID
    title: str
    description: Optional[str]
    due_date: Optional[str]
    priority: Optional[int]
    completed: bool
