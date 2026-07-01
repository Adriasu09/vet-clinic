"""CRUD operations for the Pet resource."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.crud import owner_crud
from app.exceptions import ConflictError, NotFoundError
from app.models.pet_model import Pet
from app.schemas.pet_schema import PetCreate, PetUpdate


def get_pets(db: Session) -> list[Pet]:
    """Return all pets."""
    return list(db.scalars(select(Pet)).all())


def get_pet(db: Session, pet_id: int) -> Pet:
    """Return a single pet by id, or raise NotFoundError."""
    pet = db.get(Pet, pet_id)
    if pet is None:
        raise NotFoundError(f"Pet {pet_id} not found")
    return pet


def create_pet(db: Session, pet_data: PetCreate) -> Pet:
    """Create a new pet, ensuring its owner exists."""
    owner_crud.get_owner(db, pet_data.owner_id)

    pet = Pet(**pet_data.model_dump())
    db.add(pet)
    db.commit()
    db.refresh(pet)
    return pet


def update_pet(db: Session, pet_id: int, pet_data: PetUpdate) -> Pet:
    """Update an existing pet, ensuring the pet and its owner exist."""
    pet = get_pet(db, pet_id)
    owner_crud.get_owner(db, pet_data.owner_id)

    pet.name = pet_data.name
    pet.species = pet_data.species
    pet.breed = pet_data.breed
    pet.birth_date = pet_data.birth_date
    pet.owner_id = pet_data.owner_id
    db.commit()
    db.refresh(pet)
    return pet


def delete_pet(db: Session, pet_id: int) -> None:
    """Delete a pet by id, or raise NotFoundError."""
    pet = get_pet(db, pet_id)
    if pet.medical_records or pet.appointments or pet.pet_treatments:
        raise ConflictError("Cannot delete a pet with medical records, appointments or treatments")
    db.delete(pet)
    db.commit()