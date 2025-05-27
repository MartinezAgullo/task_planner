from organizer.task_planner.domain.models.task import Task
from organizer.task_planner.driven.postgres_repository.models.task_db_model import (
    TaskDBModel,
)


def to_db(task: Task) -> TaskDBModel:  # To persist domain objects in DB
    return TaskDBModel(
        id=task.id,
        title=task.title,
        description=task.description,
        priority=task.priority,
        completed=task.completed,
        created_at=task.created_at,
        updated_at=task.updated_at,
        dependencies=[dep for dep in task.dependencies],
    )


def to_domain(
    task_db: TaskDBModel,
) -> Task:  # To load task from DB an use it in application logic
    return Task(
        id=task_db.id,
        title=task_db.title,
        description=task_db.description,
        priority=task_db.priority,
        completed=task_db.completed,
        created_at=task_db.created_at,
        updated_at=task_db.updated_at,
        dependencies=[dep.id for dep in task_db.dependencies],
    )
