from fastapi import Depends
from dependency_injector.wiring import inject, Provide
from organizer.task_planner.api_rest.dto.create_task_dto import (
    CreateTaskRequestDTO,
    CreateTaskResponseDTO,
)
from organizer.task_planner.boot.injectors.app.injector import AppContainer
from organizer.task_planner.api_rest.mappers.task_mapper import from_domain, to_domain


@inject
async def create_task_controller(
    task_data: CreateTaskRequestDTO,
    create_task=Depends(Provide[AppContainer.create_task_use_case]),
) -> CreateTaskResponseDTO:
    domain_task = to_domain(task_data)
    created_task = await create_task(domain_task)
    return from_domain(created_task)
