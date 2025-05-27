from sqlalchemy import create_engine
from organizer.task_planner.driven.postgres_repository.models.task_db_model import Base

DATABASE_URL = "postgresql+asyncpg://user:password@localhost:5432/taskdb"

engine = create_engine(DATABASE_URL)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("✅ Tables created successfully.")
