from fastapi import Depends
from dependency_injector.wiring import inject, Provide
from uuid import UUID

from organizer.task_planner.driving.api_rest.dto.create_task_dto import (
    CreateTaskRequestDTO,
    CreateTaskResponseDTO,
)
from organizer.task_planner.driving.api_rest.dto.update_task_dto import (
    UpdateTaskRequestDTO,
)
from organizer.task_planner.boot.injectors.app.injector import AppContainer
from organizer.task_planner.driving.api_rest.mappers.task_mapper import (
    from_domain,
    to_domain,
)


@inject
async def create_task_controller(
    task_data: CreateTaskRequestDTO,
    create_task=Depends(Provide[AppContainer.create_task_use_case]),
) -> CreateTaskResponseDTO:
    domain_task = to_domain(task_data)
    created_task = await create_task(domain_task)
    return from_domain(created_task)


@inject
async def get_task_controller(
    task_id: UUID,
    get_task=Depends(Provide[AppContainer.get_task_use_case]),
) -> CreateTaskResponseDTO:
    task = await get_task(task_id)
    return from_domain(task)


@inject
async def update_task_controller(
    task_id: UUID,
    task_data: UpdateTaskRequestDTO,
    update_task=Depends(Provide[AppContainer.update_task_use_case]),
) -> CreateTaskResponseDTO:
    updated_task = await update_task(
        task_id,
        task_data.title,
        task_data.description,
        task_data.priority,
    )
    return from_domain(updated_task)


@inject
async def delete_task_controller(
    task_id: UUID,
    delete_task=Depends(Provide[AppContainer.delete_task_use_case]),
) -> None:
    await delete_task(task_id)
