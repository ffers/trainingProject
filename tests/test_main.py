import pytest

pytest.importorskip("dotenv")
from main import first_func


def test_first_func_output(capsys):
    first_func()
    captured = capsys.readouterr()
    assert "Hello it`s bot for Telegram and CRM" in captured.out

