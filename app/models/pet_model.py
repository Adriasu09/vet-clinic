"""Pet model: an animal that belongs to an owner."""

from datetime import date

from sqlalchemy import Identity, ForeignKey, String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.mixins import TimestampMixin

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.owner_model import Owner
    from app.models.medical_record_model import MedicalRecord
    from app.models.appointment_model import Appointment
    from app.models.pet_treatment_model import PetTreatment


class Pet(Base, TimestampMixin):
    """A pet that belongs to an owner."""

    __tablename__ = "pets"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("owners.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    species: Mapped[str] = mapped_column(String(50), nullable=False)
    breed: Mapped[str] = mapped_column(String(50), nullable=False)
    birth_date: Mapped[date] = mapped_column(Date, nullable=False)

    owner: Mapped["Owner"] = relationship(back_populates="pets")
    medical_records: Mapped[list["MedicalRecord"]] = relationship(back_populates="pet")
    appointments: Mapped[list["Appointment"]] = relationship(back_populates="pet")
    pet_treatments: Mapped[list["PetTreatment"]] = relationship(back_populates="pet")