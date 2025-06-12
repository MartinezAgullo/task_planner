from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide

from organizer.task_planner.boot.injectors.app.injector import AppContainer
from organizer.task_planner.driving.http_client.controllers.task_controller import (
    create_task_controller,
    get_task_controller,
    update_task_controller,
    delete_task_controller,
)
from organizer.task_planner.driving.http_client.dto.create_task_dto import (
    CreateTaskRequestDTO,
    CreateTaskResponseDTO,
)
from organizer.task_planner.driving.http_client.dto.update_task_dto import (
    UpdateTaskRequestDTO,
)
from uuid import UUID

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post(
    "",
    response_model=CreateTaskResponseDTO,
    status_code=status.HTTP_201_CREATED,
)
@inject
async def create_task_endpoint(
    task_data: CreateTaskRequestDTO,
    create_task=Depends(Provide[AppContainer.create_task_use_case]),
) -> CreateTaskResponseDTO:
    return await create_task_controller(task_data, create_task)


@router.get(
    "/{task_id}",
    response_model=CreateTaskResponseDTO,
    status_code=status.HTTP_200_OK,
)
@inject
async def get_task_endpoint(
    task_id: UUID,
    get_task=Depends(Provide[AppContainer.get_task_use_case]),
) -> CreateTaskResponseDTO:
    return await get_task_controller(task_id, get_task)


@router.put(
    "/{task_id}",
    response_model=CreateTaskResponseDTO,
    status_code=status.HTTP_200_OK,
)
@inject
async def update_task_endpoint(
    task_id: UUID,
    task_data: UpdateTaskRequestDTO,
    update_task=Depends(Provide[AppContainer.update_task_use_case]),
) -> CreateTaskResponseDTO:
    return await update_task_controller(task_id, task_data, update_task)


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
@inject
async def delete_task_endpoint(
    task_id: UUID,
    delete_task=Depends(Provide[AppContainer.delete_task_use_case]),
) -> None:
    await delete_task_controller(task_id, delete_task)
