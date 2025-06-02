from uuid import uuid4, UUID
from datetime import datetime, timezone
from typing import Optional

from organizer.task_planner.domain.models.task import Task


def create_task(
    title: str,
    description: str,
    priority: int,
    dependencies: Optional[list[UUID]] = None,
) -> Task:
    if dependencies is None:
        dependencies = []

    now = datetime.now(timezone.utc)
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


# def create_task(...): ...
# def get_task(...): ...
# def update_task(...): ...
# def delete_task(...): ...
# def complete_task(...): ...

# def add_dependency(...): ...
# def remove_dependency(...): ...
