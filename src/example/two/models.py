from datetime import datetime

from sqlalchemy import Float
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from example.enum import EnumExample


class Base(DeclarativeBase):
    pass


class Inference(Base):
    __tablename__ = "inference"
    id: Mapped[int] = mapped_column(primary_key=True)
    _class: Mapped[EnumExample] = mapped_column("class")
    correlation_id: Mapped[str]
    datetime: Mapped[datetime]
    device: Mapped[str]
    location: Mapped[str]
    logits: Mapped[list[float]] = mapped_column(ARRAY(Float))
