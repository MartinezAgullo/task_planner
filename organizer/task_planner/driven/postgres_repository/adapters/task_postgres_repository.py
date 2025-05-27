"""
PostgreSQL adapter that implements the TaskStoragePort interface.
"""

from organizer.task_planner.application.ports.driven.task_storage_port import (
    TaskStoragePort,
)
from organizer.task_planner.domain.models.task import Task
from organizer.task_planner.driven.postgres_repository.config.db_config import (
    DATABASE_URL,
)  # Configuración de conexión base de datos
from organizer.task_planner.driven.postgres_repository.models.task_db_model import (
    TaskDBModel,
)  # TaskDBModel: representación de la entidad Task en la base de datos
from organizer.task_planner.driven.postgres_repository.mappers.task_mapper import (
    to_domain,
    to_db,
)

from sqlalchemy import (
    create_engine,
)  # create_engine: crea la conexión a la base de datos.
from sqlalchemy.orm import sessionmaker  # sessionmaker: fábrica de sesiones.
from uuid import UUID


class TaskPostgresRepository(TaskStoragePort):
    def __init__(self) -> None:
        self._engine = create_engine(DATABASE_URL)
        self._Session = sessionmaker(bind=self._engine)

    def save(self, task: Task) -> None:
        with self._Session() as session:
            db_task = to_db(task)  # Convertimos objeto de dominio a objeto TaskDBModel.
            session.merge(db_task)  # merge actualiza si ya existe o inserta si no.
            session.commit()  # commit guarda los cambios.

    def get_by_id(self, task_id: UUID) -> Task:
        with self._Session() as session:
            db_task = session.query(TaskDBModel).get(
                task_id
            )  # session.query(TaskDBModel): Crea una consulta SQL sobre TaskDBMode y get recupera una fila usando la clave primaria.
            if db_task is None:
                raise ValueError(f"Task {task_id} not found")
            return to_domain(db_task)  # Devolvemos objeto de dominio

    def delete(self, task_id: UUID) -> None:
        with self._Session() as session:
            db_task = session.query(TaskDBModel).get(task_id)
            if db_task:
                session.delete(db_task)
                session.commit()

    def get_all_ready(self) -> list[Task]:
        with self._Session() as session:
            tasks = session.query(TaskDBModel).all()
            ready = [t for t in tasks if all(d.completed for d in t.dependencies)]
            return [to_domain(t) for t in ready]  # Devolvemos objeto de dominio

    def list_all(self) -> list[Task]:
        with self._Session() as session:
            tasks = session.query(TaskDBModel).all()
            return [to_domain(t) for t in tasks]  # Devolvemos objeto de dominio
