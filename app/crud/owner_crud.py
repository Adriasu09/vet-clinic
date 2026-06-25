"""CRUD operations for the Owner resource."""
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.owner_model import Owner
from app.schemas.owner_schema import OwnerCreate, OwnerUpdate


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

def get_owners(db: Session) -> list[Owner]:
    """Return all owners."""
    return list(db.scalars(select(Owner)).all())

def get_owner(db: Session, owner_id: int) -> Owner | None:
    """Return a single owner by id, or None if it does not exist."""
    return db.get(Owner, owner_id)

def update_owner(db: Session, owner_id: int, owner_data: OwnerUpdate) -> Owner | None:
    """Update an existing owner and return it, or None if it does not exist."""
    owner = db.get(Owner, owner_id)
    if owner is None:
        return None
    owner.first_name = owner_data.first_name
    owner.last_name = owner_data.last_name
    owner.email = owner_data.email
    owner.phone = owner_data.phone
    db.commit()
    db.refresh(owner)
    return owner

def delete_owner(db: Session, owner_id: int) -> bool:
    """Delete an owner by id. Return True if deleted, False if not found."""
    owner = db.get(Owner, owner_id)
    if owner is None:
        return False
    db.delete(owner)
    db.commit()
    return True