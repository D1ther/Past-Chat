from sqlalchemy import (
    Integer,
    String,
    LargeBinary
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.backend.db.base import (
    Base
)

class Person(Base):
    __tablename__ = 'history_persons'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String)
    prompt: Mapped[str] = mapped_column(String)
    avatar: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)

    def __repr__(self) -> str:
        return f"<Person(id={self.id}, name='{self.name}', description='{self.description}', prompt='{self.prompt}')>"