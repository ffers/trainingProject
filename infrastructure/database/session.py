

from sqlalchemy.orm import sessionmaker
from .engine import engine

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
