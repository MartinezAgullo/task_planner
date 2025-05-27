from abc import ABC, abstractmethod
from uuid import UUID
from organizer.task_planner.domain.models.task import Task


class TaskStoragePort(ABC):
    """Defines the interface that any task storage adapter must implement."""

    @abstractmethod
    def save(self, task: Task) -> None:
        """Persist a task."""
        pass

    @abstractmethod
    def get_by_id(self, task_id: UUID) -> Task:
        """Retrieve a task by its unique identifier."""
        pass

    @abstractmethod
    def delete(self, task_id: UUID) -> None:
        """Delete a task by its unique identifier."""
        pass

    @abstractmethod
    def get_all_ready(self) -> list[Task]:
        """Return tasks that have no incomplete dependencies."""
        pass

    @abstractmethod
    def list_all(self) -> list[Task]:
        """Return all tasks."""
        pass
