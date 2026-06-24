"""Treatment model: a medical treatment offered by the clinic."""

from decimal import Decimal

from sqlalchemy import Identity, String, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.pet_treatment_model import PetTreatment


class Treatment(Base):
    """A medical treatment that can be applied to pets."""

    __tablename__ = "treatments"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    type: Mapped[str] = mapped_column(String(50), nullable=False)
    cost: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    pet_treatments: Mapped[list["PetTreatment"]] = relationship(back_populates="treatment")
