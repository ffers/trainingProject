import pytest

sqlalchemy = pytest.importorskip("sqlalchemy")

from infrastructure.database import engine as engine_module
from infrastructure.database import base as base_module
from infrastructure.database import session as session_module
from domain.models.user import User


def test_engine_instance():
    assert isinstance(engine_module.engine, sqlalchemy.engine.Engine)


def test_session_local():
    session = session_module.SessionLocal()
    try:
        assert session.bind is engine_module.engine
    finally:
        session.close()


def test_user_model_metadata():
    assert User.__tablename__ == "users"
    column_names = {column.name for column in User.__table__.columns}
    assert {"id", "name"} <= column_names

