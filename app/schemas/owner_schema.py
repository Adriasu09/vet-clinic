"""Pydantic schemas for the Owner resource (API validation)."""

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


class OwnerRead(OwnerBase):
    """Data returned to the client (includes the generated id)."""
    id: int

    model_config = {"from_attributes": True}