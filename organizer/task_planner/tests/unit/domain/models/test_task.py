from uuid import UUID
from organizer.task_planner.application.services.task_management_use_case import (
    create_task,
)


def test_create_task_returns_valid_task():
    task = create_task(title="Test Task", description="A test", priority=3)

    assert isinstance(task.id, UUID)
    assert task.title == "Test Task"
    assert task.description == "A test"
    assert task.priority == 3
    assert task.completed is False
    assert task.dependencies == []
    assert task.created_at is not None
    assert task.updated_at is not None


# def test_add_dependency():
#     task = Task.create(title="Test", description="Desc", priority=1)
#     dep_id = UUID("12345678-1234-5678-1234-567812345678")

#     task.add_dependency(dep_id)

#     assert dep_id in task.dependencies


# def test_add_dependency_does_not_duplicate():
#     task = Task.create(title="Test", description="Desc", priority=1)
#     dep_id = UUID("12345678-1234-5678-1234-567812345678")

#     task.add_dependency(dep_id)
#     task.add_dependency(dep_id)  # Second attempt should be ignored

#     assert task.dependencies.count(dep_id) == 1


# def test_mark_as_completed():
#     task = Task.create(title="Test", description="Desc", priority=1)
#     task.mark_as_completed()
#     assert task.completed is True


# def test_remove_dependency():
#     task = Task.create(title="Test", description="Desc", priority=1)
#     dep_id = UUID("12345678-1234-5678-1234-567812345678")

#     task.add_dependency(dep_id)
#     task.remove_dependency(dep_id)

#     assert dep_id not in task.dependencies
