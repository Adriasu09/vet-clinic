"""API routes for the Owner resource."""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.crud import owner_crud
from app.database import get_db
from app.schemas.owner_schema import OwnerCreate, OwnerRead, OwnerUpdate

router = APIRouter(prefix="/owners", tags=["Owners"])


@router.post("/", response_model=OwnerRead, status_code=status.HTTP_201_CREATED)
def create_owner(owner_data: OwnerCreate, db: Session = Depends(get_db)):
    """Create a new owner."""
    return owner_crud.create_owner(db, owner_data)


@router.get("/", response_model=list[OwnerRead])
def list_owners(db: Session = Depends(get_db)):
    """Return all owners."""
    return owner_crud.get_owners(db)


@router.get("/{owner_id}", response_model=OwnerRead)
def get_owner(owner_id: int, db: Session = Depends(get_db)):
    """Return a single owner by id."""
    return owner_crud.get_owner(db, owner_id)


@router.put("/{owner_id}", response_model=OwnerRead)
def update_owner(owner_id: int, owner_data: OwnerUpdate, db: Session = Depends(get_db)):
    """Update an existing owner."""
    return owner_crud.update_owner(db, owner_id, owner_data)


@router.delete("/{owner_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_owner(owner_id: int, db: Session = Depends(get_db)):
    """Delete an owner by id."""
    owner_crud.delete_owner(db, owner_id)