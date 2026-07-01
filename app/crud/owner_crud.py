"""CRUD operations for the Owner resource."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.exceptions import ConflictError, NotFoundError
from app.models.owner_model import Owner
from app.schemas.owner_schema import OwnerCreate, OwnerUpdate


def get_owner_by_email(db: Session, email: str) -> Owner | None:
    """Return the owner with the given email, or None."""
    return db.scalars(select(Owner).where(Owner.email == email)).first()


def get_owner_by_phone(db: Session, phone: str) -> Owner | None:
    """Return the owner with the given phone, or None."""
    return db.scalars(select(Owner).where(Owner.phone == phone)).first()


def get_owners(db: Session) -> list[Owner]:
    """Return all owners."""
    return list(db.scalars(select(Owner)).all())


def get_owner(db: Session, owner_id: int) -> Owner:
    """Return a single owner by id, or raise NotFoundError."""
    owner = db.get(Owner, owner_id)
    if owner is None:
        raise NotFoundError(f"Owner {owner_id} not found")
    return owner


def create_owner(db: Session, owner_data: OwnerCreate) -> Owner:
    """Create a new owner, ensuring email and phone are unique."""
    if get_owner_by_email(db, owner_data.email):
        raise ConflictError(f"Email {owner_data.email} already registered")
    if get_owner_by_phone(db, owner_data.phone):
        raise ConflictError(f"Phone {owner_data.phone} already registered")

    owner = Owner(**owner_data.model_dump())
    db.add(owner)
    db.commit()
    db.refresh(owner)
    return owner


def update_owner(db: Session, owner_id: int, owner_data: OwnerUpdate) -> Owner:
    """Update an existing owner, or raise NotFoundError."""
    owner = get_owner(db, owner_id)  # raises NotFoundError if missing

    existing_email = get_owner_by_email(db, owner_data.email)
    if existing_email and existing_email.id != owner_id:
        raise ConflictError(f"Email {owner_data.email} already registered")
    existing_phone = get_owner_by_phone(db, owner_data.phone)
    if existing_phone and existing_phone.id != owner_id:
        raise ConflictError(f"Phone {owner_data.phone} already registered")

    owner.first_name = owner_data.first_name
    owner.last_name = owner_data.last_name
    owner.email = owner_data.email
    owner.phone = owner_data.phone
    db.commit()
    db.refresh(owner)
    return owner


def delete_owner(db: Session, owner_id: int) -> None:
    """Delete an owner by id, or raise NotFoundError."""
    owner = get_owner(db, owner_id)  # raises NotFoundError if missing
    db.delete(owner)
    db.commit()