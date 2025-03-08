from sqlalchemy import (
    create_engine,
)

from sqlalchemy.orm import (
    sessionmaker,
    DeclarativeBase
)

eng = create_engine('sqlite:///past_chat.db', echo=True)
Session = sessionmaker(eng)

class Base(DeclarativeBase):
    ...

def creat_db():
    Base.metadata.create_all(eng)

def drop_db():
    Base.metadata.drop_all(eng)