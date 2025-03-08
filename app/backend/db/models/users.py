from sqlalchemy import (
    Integer,
    String,
    LargeBinary
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from app.backend.db.base import (
    Base
)

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    avatar: Mapped[bytes] = mapped_column(LargeBinary, nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"
    
    def hashed_password(self):
        return generate_password_hash(self.password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)