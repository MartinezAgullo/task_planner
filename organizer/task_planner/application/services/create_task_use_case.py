from uuid import UUID

from organizer.task_planner.domain.models.task import Task
from organizer.task_planner.application.ports.driven.task_storage_port import (
    TaskStoragePort,
)


class CreateTaskUseCase:
    def __init__(self, storage: TaskStoragePort):
        self._storage = storage  # Instancia de TaskStoragePort

    def execute(
        self,
        title: str,
        description: str,
        priority: int,
        dependencies: list[UUID] | None = None,
    ) -> Task:
        task = Task.create(
            title=title,
            description=description,
            priority=priority,
            dependencies=dependencies,
        )

        self._storage.save(task)
        return task
