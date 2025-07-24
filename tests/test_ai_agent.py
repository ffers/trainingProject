import sys
import types

from domain.dto.tg_message import Message


def test_agent_logs_exception(tmp_path, monkeypatch):
    # Provide dummy together module before importing the agent
    fake_together = types.ModuleType("together")
    fake_together.Together = lambda: None
    sys.modules.setdefault("together", fake_together)

    from domain.services.ai_agent import TestAIAgent

    log_file = tmp_path / "agent.log"
    monkeypatch.setenv("AI_AGENT_LOG_PATH", str(log_file))

    def fake_send_promt(message: Message):
        raise RuntimeError("boom")

    class FakeTelegram:
        def sendMessage(self, text='Тест', chat_id=1):
            return text

    monkeypatch.setattr(
        'infrastructure.api_clients.ai_agents.together.send_promt',
        fake_send_promt
    )
    monkeypatch.setattr('domain.services.ai_agent.Telegram', FakeTelegram)

    agent = TestAIAgent()
    result = agent.respond(Message(first_name='a', chat_id=1, text='hi'))
    assert result == 'Can not respond'
    assert 'Failed to respond' in log_file.read_text()
