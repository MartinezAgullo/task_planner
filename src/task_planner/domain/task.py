from dataclasses import dataclass
from uuid import UUID, uuid4
from datetime import datetime


@dataclass
class Task:
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
        dependencies: list[UUID] | None = None,
    ) -> "Task":
        now = datetime.utcnow()
        return Task(
            id=uuid4(),
            title=title,
            description=description,
            priority=priority,
            completed=False,
            dependencies=dependencies or [],
            created_at=now,
            updated_at=now,
        )

    def mark_as_completed(self) -> None:
        self.completed = True
        self.updated_at = datetime.utcnow()

    def add_dependency(self, task_id: UUID) -> None:
        if task_id not in self.dependencies:
            self.dependencies.append(task_id)
            self.updated_at = datetime.utcnow()

    def remove_dependency(self, task_id: UUID) -> None:
        if task_id in self.dependencies:
            self.dependencies.remove(task_id)
            self.updated_at = datetime.utcnow()
