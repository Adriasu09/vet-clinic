"""API routes for the Owner resource."""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.crud import owner_crud
from app.database import get_db
from app.schemas.owner_schema import OwnerCreate, OwnerRead

router = APIRouter(prefix="/owners", tags=["Owners"])


@router.post("/", response_model=OwnerRead, status_code=status.HTTP_201_CREATED)
def create_owner(owner_data: OwnerCreate, db: Session = Depends(get_db)):
    """Create a new owner."""
    return owner_crud.create_owner(db=db, owner_data=owner_data)