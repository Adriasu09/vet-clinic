"""API routes for the Pet resource."""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.crud import pet_crud
from app.database import get_db
from app.schemas.pet_schema import PetCreate, PetRead, PetUpdate

router = APIRouter(prefix="/pets", tags=["Pets"])


@router.post("/", response_model=PetRead, status_code=status.HTTP_201_CREATED)
def create_pet(pet_data: PetCreate, db: Session = Depends(get_db)):
    """Create a new pet."""
    return pet_crud.create_pet(db, pet_data)


@router.get("/", response_model=list[PetRead])
def list_pets(db: Session = Depends(get_db)):
    """Return all pets."""
    return pet_crud.get_pets(db)


@router.get("/{pet_id}", response_model=PetRead)
def get_pet(pet_id: int, db: Session = Depends(get_db)):
    """Return a single pet by id."""
    return pet_crud.get_pet(db, pet_id)


@router.put("/{pet_id}", response_model=PetRead)
def update_pet(pet_id: int, pet_data: PetUpdate, db: Session = Depends(get_db)):
    """Update an existing pet."""
    return pet_crud.update_pet(db, pet_id, pet_data)


@router.delete("/{pet_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pet(pet_id: int, db: Session = Depends(get_db)):
    """Delete a pet by id."""
    pet_crud.delete_pet(db, pet_id)