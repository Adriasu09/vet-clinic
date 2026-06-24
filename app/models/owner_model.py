"""Owner model: a pet owner / clinic client."""

from sqlalchemy import Identity, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Owner(Base):
    """A person who owns one or more pets."""

    __tablename__ = "owners"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=False)