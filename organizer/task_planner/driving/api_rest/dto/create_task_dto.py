from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID


class CreateTaskRequestDTO(BaseModel):
    name: str = Field(..., example="Buy groceries")
    description: Optional[str] = Field(None, example="Milk, eggs, bread")
    due_date: Optional[str] = Field(None, example="2025-06-10T12:00:00Z")  # ISO 8601
    priority: Optional[int] = Field(None, example=2)


class CreateTaskResponseDTO(BaseModel):
    id: UUID
    name: str
    description: Optional[str]
    due_date: Optional[str]
    priority: Optional[int]
    completed: bool
