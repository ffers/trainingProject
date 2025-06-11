class TestAIAgent:
    """Simple rule-based AI agent for demonstration."""

    def respond(self, message: str) -> str:
        """Return a response based on the message content."""
        text = message.lower()
        if 'hello' in text:
            return 'Hello! I am a test AI agent.'
        if 'bye' in text or 'goodbye' in text:
            return 'Goodbye!'
        return "I don't understand."
