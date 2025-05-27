from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase

from sqlalchemy.dialects.postgresql import UUID as PG_UUID

# from sqlalchemy.orm import declarative_base
from datetime import datetime, timezone
import uuid

# Base = declarative_base()


class Base(DeclarativeBase):
    pass


# Tabla interna que modela modela una relación muchos-a-muchos entre tareas (TaskDBModel).
task_dependencies = Table(
    "task_dependencies",
    Base.metadata,
    Column("task_id", PG_UUID(as_uuid=True), ForeignKey("tasks.id"), primary_key=True),
    Column(
        "dependency_id", PG_UUID(as_uuid=True), ForeignKey("tasks.id"), primary_key=True
    ),
)


class TaskDBModel(Base):
    __tablename__ = "tasks"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(String)
    priority = Column(Integer, nullable=False)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    dependencies = relationship(
        "TaskDBModel",
        secondary=task_dependencies,
        primaryjoin=id == task_dependencies.c.task_id,
        secondaryjoin=id == task_dependencies.c.dependency_id,
        backref="dependents",  # si también quieres saber qué tareas dependen de esta
    )
