from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base

class Building(Base):
    __tablename__ = "buildings"

    id: Mapped[int] = mapped_column(
            primary_key = True
    )

    name: Mapped[str] = mapped_column(
            String(100),
            nullable = False
    )

    address: Mapped[str] = mapped_column(
            String(255),
            nullable = False
    )

    created_at: Mapped[datetime] = mapped_column(
            DateTime,
            default = datetime.utcnow
    )
