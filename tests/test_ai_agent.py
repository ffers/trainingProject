import os
import sys
import types
import pytest

# ``domain.services.ai_agent`` depends on the third‑party ``together``
# package which might be missing in the test environment.  Provide a
# lightweight stub before importing the agent so that the import does not
# fail when the real library is unavailable.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

sys.modules.setdefault("together", types.ModuleType("together"))
if not hasattr(sys.modules["together"], "Together"):
    sys.modules["together"].Together = lambda *a, **kw: object()
sys.modules.setdefault("pydantic", types.ModuleType("pydantic"))
if not hasattr(sys.modules["pydantic"], "BaseModel"):

    class _BM:  # simple stand-in for pydantic.BaseModel
        pass

    sys.modules["pydantic"].BaseModel = _BM
sys.modules.setdefault("requests", types.ModuleType("requests"))
if not hasattr(sys.modules["requests"], "post"):

    def _dummy(*a, **kw):
        class Resp:
            content = b"{}"

        return Resp()

    sys.modules["requests"].post = _dummy

from domain.services.ai_agent import TestAIAgent
from dataclasses import dataclass


@dataclass
class Message:
    text: str
    chat_id: int


def test_respond_start(monkeypatch):
    agent = TestAIAgent()
    calls = []

    def fake_send_message(text="Тест", chat_id=0):
        calls.append((text, chat_id))
        return text

    # replace Telegram.sendMessage method on the agent instance
    monkeypatch.setattr(
        agent, "tg", types.SimpleNamespace(sendMessage=fake_send_message)
    )

    msg = Message(text="/start", chat_id=42)
    result = agent.respond(msg)

    expected_text = "Hello! I am a test AI agent. Я трохи довго думаю але я працюю"
    assert result == expected_text
    assert calls == [(expected_text, 42)]


def test_respond_regular(monkeypatch):
    agent = TestAIAgent()
    calls = []

    def fake_send_message(text="Тест", chat_id=0):
        calls.append((text, chat_id))
        return text

    monkeypatch.setattr(
        agent, "tg", types.SimpleNamespace(sendMessage=fake_send_message)
    )
    monkeypatch.setattr(
        "domain.services.ai_agent.send_promt", lambda message: "AI RESPONSE"
    )

    msg = Message(text="Hi", chat_id=99)
    result = agent.respond(msg)

    assert result == "AI RESPONSE"
    assert calls == [("Думаю...", 99), ("AI RESPONSE", 99)]
