from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Simple(Base):
    __tablename__ = "simple"
    id: Mapped[int] = mapped_column(primary_key=True)
    integer: Mapped[int]
