from uuid import UUID
from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide

from organizer.task_planner.boot.injectors.app.injector import AppContainer
from organizer.task_planner.driving.api_rest.adapters.task_controller_adapter import (
    create_task_controller,
    get_task_controller,
    update_task_controller,
    delete_task_controller,
)
from organizer.task_planner.driving.api_rest.dto.create_task_dto import (
    CreateTaskRequestDTO,
    CreateTaskResponseDTO,
)
from organizer.task_planner.driving.api_rest.dto.update_task_dto import (
    UpdateTaskRequestDTO,
)

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post(
    "", response_model=CreateTaskResponseDTO, status_code=status.HTTP_201_CREATED
)
@inject
async def create_task(
    task_data: CreateTaskRequestDTO,
    create=Depends(Provide[AppContainer.create_task_use_case]),
) -> CreateTaskResponseDTO:
    return await create_task_controller(task_data, create)


@router.get(
    "/{task_id}", response_model=CreateTaskResponseDTO, status_code=status.HTTP_200_OK
)
@inject
async def get_task(
    task_id: UUID,
    get=Depends(Provide[AppContainer.get_task_use_case]),
) -> CreateTaskResponseDTO:
    return await get_task_controller(task_id, get)


@router.put(
    "/{task_id}", response_model=CreateTaskResponseDTO, status_code=status.HTTP_200_OK
)
@inject
async def update_task(
    task_id: UUID,
    task_data: UpdateTaskRequestDTO,
    update=Depends(Provide[AppContainer.update_task_use_case]),
) -> CreateTaskResponseDTO:
    return await update_task_controller(task_id, task_data, update)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
async def delete_task(
    task_id: UUID,
    delete=Depends(Provide[AppContainer.delete_task_use_case]),
) -> None:
    await delete_task_controller(task_id, delete)
