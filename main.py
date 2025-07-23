



from typing import Union
import asyncio, json

from fastapi import FastAPI, Request


from flatten_json import flatten

from dotenv import load_dotenv
load_dotenv()

from application.cntrl import Cntrl
from domain.dto.tg_message import Message




app = FastAPI()



@app.post("/")
async def message_wait(request: Request):
    cntrl = Cntrl()
    try:
        data = await request.json()
        # data = data.decode("utf-8")
        print(data)
        flatten_data = flatten(data)
        message = Message(
            first_name=flatten_data.get('message_from_first_name'),
            chat_id=flatten_data.get('message_chat_id'),
            text=flatten_data.get('message_text')
        )
        print(message)
        
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(None, lambda: cntrl.send_promt(message))
        return {"response": result}
    except Exception as e:
        print(f'message_wait exception: {e}') 
        return {"response": 'Can not responce'}



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}