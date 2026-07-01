"""Pydantic schemas for the Pet resource (API validation)."""

from datetime import date, datetime
from pydantic import BaseModel


class PetBase(BaseModel):
    """Shared pet fields."""
    name: str
    species: str
    breed: str
    birth_date: date
    owner_id: int


class PetCreate(PetBase):
    """Data required to create a pet (the client sends this)."""
    pass


class PetUpdate(PetBase):
    """Data to update an existing pet."""
    pass


class PetRead(PetBase):
    """Data returned to the client (includes the generated id)."""
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}