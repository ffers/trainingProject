


from pydantic import BaseModel


class Message(BaseModel):
    first_name: str | None = None
    chat_id: int | None = None
    text: str | None = None