from dependency_injector import containers, providers

from organizer.task_planner.application.services.task_management_use_case import (
    create_task,
    get_task,
    update_task,
    delete_task,
    complete_task,
    add_dependency,
    remove_dependency,
)


class AppContainer(containers.DeclarativeContainer):
    """Dependency injection container for the Task Planner app."""

    wiring_config = containers.WiringConfiguration(
        packages=[
            "organizer.task_planner.driving.api_rest.routes",
            "organizer.task_planner.driving.api_rest.adapters",
        ]
    )

    # Use case providers
    create_task_use_case = providers.Factory(create_task)
    get_task_use_case = providers.Factory(get_task)
    update_task_use_case = providers.Factory(update_task)
    delete_task_use_case = providers.Factory(delete_task)
    complete_task_use_case = providers.Factory(complete_task)
    add_dependency_use_case = providers.Factory(add_dependency)
    remove_dependency_use_case = providers.Factory(remove_dependency)
