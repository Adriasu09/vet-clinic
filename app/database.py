"""Database setup: SQLAlchemy engine, session factory, Base, and get_db dependency."""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings

# The engine is the core interface to the database.
# echo=True logs every SQL statement — useful while learning (turn off later).
engine = create_engine(settings.database_url, echo=True)

# Factory that produces database sessions (each one is a unit of work).
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class that all ORM models (tables) will inherit from.
Base = declarative_base()


def get_db():
    """Provide a database session and make sure it is closed afterwards."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()