

import logging
import os

from infrastructure.api_clients.ai_agents.together import send_promt
from infrastructure.api_clients.telegram import Telegram
from domain.dto.tg_message import Message


# Configure logger for the agent
log_path = os.getenv("AI_AGENT_LOG_PATH", "ai_agent.log")
logger = logging.getLogger("TestAIAgent")
if not logger.handlers:
    handler = logging.FileHandler(log_path)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

class TestAIAgent:
    """Simple rule-based AI agent for demonstration."""
    def __init__(self):
        self.tg = Telegram()

    def respond(self, message: Message) -> str:
        """Generate a reply for the given message."""
        try:
            if message.text and '/start' in message.text:
                logger.info("Received start command")
                return self.tg.sendMessage(
                    'Hello! I am a test AI agent. Я трохи довго думаю але я працюю',
                    message.chat_id,
                )

            logger.info("Processing message: %s", message.text)
            self.tg.sendMessage('Думаю...', message.chat_id)
            result = send_promt(message)
            return self.tg.sendMessage(result, message.chat_id)
        except Exception:
            logger.exception("Failed to respond")
            try:
                return self.tg.sendMessage('Can not respond', message.chat_id)
            except Exception:
                logger.exception("Failed to send error message")
                return 'Can not respond'
