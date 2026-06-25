"""CRUD operations for the Owner resource."""

from sqlalchemy.orm import Session

from app.models.owner_model import Owner
from app.schemas.owner_schema import OwnerCreate


def create_owner(db: Session, owner_data: OwnerCreate) -> Owner:
    """Create a new owner and persist it in the database."""
    owner = Owner(
        first_name=owner_data.first_name,
        last_name=owner_data.last_name,
        email=owner_data.email,
        phone=owner_data.phone,
    )
    db.add(owner)
    db.commit()
    db.refresh(owner)
    return owner