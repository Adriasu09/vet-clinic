"""Pytest fixtures: test database and API client."""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import app.models  # noqa: F401  -> register models
from app.core.config import settings
from app.database import Base, get_db
from main import app

# Test DB URL: same settings, but pointing to vet_clinic_test_db
TEST_DATABASE_URL = (
    f"postgresql+psycopg2://{settings.db_user}:{settings.db_password}"
    f"@{settings.db_host}:{settings.db_port}/vet_clinic_test_db"
)

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def client():
    """Provide a TestClient backed by a fresh test database."""
    Base.metadata.create_all(bind=engine)   # tables before each test

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db   # use the TEST db
    yield TestClient(app)
    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)     # clean tables after each test