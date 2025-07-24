

from infrastructure.api_clients.ai_agents.together import send_promt
from infrastructure.api_clients.telegram import Telegram
from domain.dto.tg_message import  Message

class TestAIAgent:
    """Simple rule-based AI agent for demonstration."""
    def __init__(self):
        self.tg = Telegram()

    def respond(self, message: Message) -> str:
        if '/start' in message.text:
            return self.tg.sendMessage('Hello! I am a test AI agent. Я трохи довго думаю але я працюю', message.chat_id)
        self.tg.sendMessage('Думаю...', message.chat_id)
        result = send_promt(message)
        """Return a response based on the message content."""
        return self.tg.sendMessage(result, message.chat_id)
