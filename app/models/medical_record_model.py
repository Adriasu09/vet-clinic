"""Medical record model: a clinical entry for a pet visit."""

from datetime import date
from decimal import Decimal

from sqlalchemy import Date, ForeignKey, Identity, Numeric, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.pet_model import Pet


class MedicalRecord(Base):
    """A clinical record entry that belongs to a pet (one per visit)."""

    __tablename__ = "medical_records"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    pet_id: Mapped[int] = mapped_column(ForeignKey("pets.id"), nullable=False)
    record_date: Mapped[date] = mapped_column(Date, nullable=False)
    weight: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    notes: Mapped[str | None] = mapped_column(Text)
    pet: Mapped["Pet"] = relationship(back_populates="medical_records")