

from domain.services.ai_agent import TestAIAgent
from domain.dto.tg_message import Message

class Cntrl:
    def __init__(self):
        self.agent = TestAIAgent()
        
    def send_promt(self, message: Message):
        return self.agent.respond(message)