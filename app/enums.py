"""Domain enums shared across models and schemas."""

import enum


class AppointmentStatus(enum.Enum):
    """Possible states of an appointment."""

    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"