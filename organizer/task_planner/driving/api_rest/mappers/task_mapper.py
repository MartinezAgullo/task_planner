from organizer.task_planner.domain.models.task import Task
from organizer.task_planner.driving.api_rest.dto.create_task_dto import (
    CreateTaskRequestDTO,
    CreateTaskResponseDTO,
)


def to_domain(dto: CreateTaskRequestDTO) -> Task:
    return Task(
        name=dto.name,
        description=dto.description,
        due_date=dto.due_date,
        priority=dto.priority,
        completed=False,
    )


def from_domain(task: Task) -> CreateTaskResponseDTO:
    return CreateTaskResponseDTO(
        id=task.id,
        name=task.name,
        description=task.description,
        due_date=task.due_date,
        priority=task.priority,
        completed=task.completed,
    )
