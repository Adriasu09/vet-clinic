"""Pet-treatment model: links a pet with a treatment (association object)."""

from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, Identity, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.pet_model import Pet
    from app.models.treatment_model import Treatment


class PetTreatment(Base, TimestampMixin):
    """A treatment applied to a pet, with its own dates and dosage."""

    __tablename__ = "pet_treatments"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    pet_id: Mapped[int] = mapped_column(ForeignKey("pets.id"), nullable=False)
    treatment_id: Mapped[int] = mapped_column(ForeignKey("treatments.id"), nullable=False)
    start_date: Mapped[date] = mapped_column(Date, nullable=False)
    end_date: Mapped[date] = mapped_column(Date, nullable=False)
    dosage: Mapped[str | None] = mapped_column(String(100))

    pet: Mapped["Pet"] = relationship(back_populates="pet_treatments")
    treatment: Mapped["Treatment"] = relationship(back_populates="pet_treatments")