"""Appointment model: a scheduled visit of a pet with a veterinarian."""

from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, Identity, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.enums import AppointmentStatus
from app.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.pet_model import Pet
    from app.models.veterinarian_model import Veterinarian


class Appointment(Base, TimestampMixin):
    """A scheduled appointment between a pet and a veterinarian."""

    __tablename__ = "appointments"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    pet_id: Mapped[int] = mapped_column(ForeignKey("pets.id"), nullable=False)
    veterinarian_id: Mapped[int] = mapped_column(ForeignKey("veterinarians.id"), nullable=False)
    appointment_date: Mapped[date] = mapped_column(Date, nullable=False)
    status: Mapped[AppointmentStatus] = mapped_column(
        Enum(
            AppointmentStatus,
            name="appointment_status",
            values_callable=lambda enum_cls: [member.value for member in enum_cls],
        ),
        default=AppointmentStatus.SCHEDULED,
        nullable=False,
    )

    pet: Mapped["Pet"] = relationship(back_populates="appointments")
    veterinarian: Mapped["Veterinarian"] = relationship(back_populates="appointments")