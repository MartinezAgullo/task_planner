from uuid import uuid4, UUID
from datetime import datetime, timezone
from typing import Optional, List, Dict

from organizer.task_planner.domain.models.task import Task

# Simulated in-memory store
task_store: Dict[UUID, Task] = {}


def create_task(
    title: str,
    description: str,
    priority: int,
    dependencies: Optional[List[UUID]] = None,
) -> Task:
    if dependencies is None:
        dependencies = []

    now = datetime.now(timezone.utc)
    task = Task(
        id=uuid4(),
        title=title,
        description=description,
        priority=priority,
        completed=False,
        dependencies=dependencies,
        created_at=now,
        updated_at=now,
    )
    task_store[task.id] = task
    return task


def get_task(task_id: UUID) -> Task:
    return task_store[task_id]


def update_task(task_id: UUID, title: str, description: str, priority: int) -> Task:
    task = task_store[task_id]
    updated_task = task.copy(
        update={
            "title": title,
            "description": description,
            "priority": priority,
            "updated_at": datetime.now(timezone.utc),
        }
    )
    task_store[task_id] = updated_task
    return updated_task


def delete_task(task_id: UUID) -> None:
    task_store.pop(task_id, None)


def complete_task(task_id: UUID) -> Task:
    task = task_store[task_id]
    completed_task = task.copy(
        update={
            "completed": True,
            "updated_at": datetime.now(timezone.utc),
        }
    )
    task_store[task_id] = completed_task
    return completed_task


def add_dependency(task_id: UUID, dependency_id: UUID) -> Task:
    task = task_store[task_id]
    if dependency_id not in task.dependencies:
        updated_task = task.copy(
            update={
                "dependencies": task.dependencies + [dependency_id],
                "updated_at": datetime.now(timezone.utc),
            }
        )
        task_store[task_id] = updated_task
        return updated_task
    return task


def remove_dependency(task_id: UUID, dependency_id: UUID) -> Task:
    task = task_store[task_id]
    updated_dependencies = [dep for dep in task.dependencies if dep != dependency_id]
    updated_task = task.copy(
        update={
            "dependencies": updated_dependencies,
            "updated_at": datetime.now(timezone.utc),
        }
    )
    task_store[task_id] = updated_task
    return updated_task
