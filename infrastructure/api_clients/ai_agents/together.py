






from together import Together
from domain.dto.tg_message import Message

client = Together()

def send_promt(message: Message):
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages=[
        {
            "role": "user",
            "content": message.text
        }
        ]
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content