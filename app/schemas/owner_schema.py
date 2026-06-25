"""Pydantic schemas for the Owner resource (API validation)."""

from datetime import datetime
from pydantic import BaseModel, EmailStr


class OwnerBase(BaseModel):
    """Shared owner fields."""
    first_name: str
    last_name: str
    email: EmailStr
    phone: str


class OwnerCreate(OwnerBase):
    """Data required to create an owner (the client sends this)."""
    pass


class OwnerUpdate(OwnerBase):
    """Data to update an existing owner."""
    pass


class OwnerRead(OwnerBase):
    """Data returned to the client (includes the generated id)."""
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}