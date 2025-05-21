from uuid import UUID
from task_planner.domain.task import Task


def test_create_task_sets_defaults():
    task = Task.create(title="Test", description="Desc", priority=1)

    assert isinstance(task.id, UUID)
    assert task.title == "Test"
    assert task.description == "Desc"
    assert task.priority == 1
    assert task.completed is False
    assert task.dependencies == []
    assert task.created_at is not None
    assert task.updated_at is not None


def test_add_dependency():
    task = Task.create(title="Test", description="Desc", priority=1)
    dep_id = UUID("12345678-1234-5678-1234-567812345678")

    task.add_dependency(dep_id)

    assert dep_id in task.dependencies
