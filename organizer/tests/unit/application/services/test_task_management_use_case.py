# import pytest
from uuid import UUID

from organizer.task_planner.application.services import (
    task_management_use_case as use_case,
)
from organizer.task_planner.domain.models.task import Task


def test_create_task_stores_task():
    # Arrange
    title = "Write tests"
    description = "Create unit tests for task planner"
    priority = 1

    # Act
    task = use_case.create_task(title, description, priority)

    # Assert
    assert isinstance(task, Task)
    assert task.title == title
    assert task.description == description
    assert task.priority == priority
    assert task.id in use_case.task_store
    assert not task.completed
    assert isinstance(task.id, UUID)
