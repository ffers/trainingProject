


import requests
import os, re, json

class Telegram:
    def __init__(self):
        pass

    def sendMessage(self, text='Тест', chat_id=196584706):
        print('відсилаю повідомленя')
        escape_text = self.escape_text(text)
        method = "sendMessage"
        token = os.getenv("TOKEN_TG_BOT_AI") 
        url = f"https://api.telegram.org/bot{token}/{method}"
        data = {"chat_id": chat_id, "text": escape_text, 'parse_mode': 'MarkdownV2'}
        resp_json = requests.post(url, data=data).content
        return json.loads(resp_json)
    
    def escape_text(self, text):
        two_slash = r"_*[]~`>#|{}.!-.()+="
        one_slash = r"-.()+="
        escape_two_slash = re.sub(f"([{re.escape(two_slash)}])", r"\\\1", text)
        escape_one_slash = re.sub(r'(?<!\\)([-.()+=])', r'\\\1', escape_two_slash)
        # return re.sub(r'\\([^\w\s])', r'\1', escape_two_slash)
        return escape_one_slash
        
