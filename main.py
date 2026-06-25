"""FastAPI application entry point."""

from fastapi import FastAPI

import app.models  # noqa: F401  -> register all models so SQLAlchemy mappers resolve
from app.core.config import settings
from app.routers.owner_router import router as owner_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description,
)

app.include_router(owner_router)