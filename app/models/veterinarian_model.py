"""Veterinarian model: a clinic veterinarian."""

from sqlalchemy import Identity, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Veterinarian(Base):
    """A veterinarian cares for one or more pets."""

    __tablename__ = "veterinarians"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    specialty: Mapped[str] = mapped_column(String(100), nullable=False)