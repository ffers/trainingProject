from infrastructure.database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


'''

add model
connect db with alembic
make alembic.ini url db

'''