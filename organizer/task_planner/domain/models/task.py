from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import datetime
from datetime import timezone
from typing import Optional


class Task(BaseModel):
    id: UUID
    title: str
    description: str
    priority: int
    completed: bool
    dependencies: list[UUID]
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def create(
        title: str,
        description: str,
        priority: int,
        dependencies: Optional[list[UUID]] = None,
    ) -> "Task":
        now = datetime.now(timezone.utc)

        if dependencies is None:
            dependencies = []

        return Task(
            id=uuid4(),
            title=title,
            description=description,
            priority=priority,
            completed=False,
            dependencies=dependencies,
            created_at=now,
            updated_at=now,
        )

    def mark_as_completed(self) -> None:
        self.completed = True
        self.updated_at = datetime.now(timezone.utc)

    def add_dependency(self, task_id: UUID) -> None:
        if task_id not in self.dependencies:
            self.dependencies.append(task_id)
            self.updated_at = datetime.now(timezone.utc)

    def remove_dependency(self, task_id: UUID) -> None:
        if task_id in self.dependencies:
            self.dependencies.remove(task_id)
            self.updated_at = datetime.now(timezone.utc)
