"""Import all models so SQLAlchemy registers them on Base.metadata."""

from app.models.owner_model import Owner
from app.models.pet_model import Pet
from app.models.treatment_model import Treatment
from app.models.veterinarian_model import Veterinarian
from app.models.medical_record_model import MedicalRecord

__all__ = ["Owner", "Treatment", "Veterinarian", "Pet", "MedicalRecord"]
