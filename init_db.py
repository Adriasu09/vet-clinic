"""Create all database tables defined by the SQLAlchemy models."""

import app.models  # noqa: F401  -> importing registers the models on Base.metadata
from app.database import Base, engine


def init_db() -> None:
    """Create all tables in the database."""
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("Tables created successfully.")