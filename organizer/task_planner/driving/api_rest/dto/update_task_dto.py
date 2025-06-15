from pydantic import BaseModel, Field
from typing import Optional


class UpdateTaskRequestDTO(BaseModel):
    name: str = Field(None, example="Buy groceries (updated)")
    description: Optional[str] = Field(None, example="Updated list")
    due_date: Optional[str] = Field(None, example="2025-06-15T12:00:00Z")
    priority: Optional[int] = Field(None, example=1)
    completed: Optional[bool] = Field(None, example=True)
