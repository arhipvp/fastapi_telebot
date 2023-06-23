import os

import requests
from dotenv import load_dotenv

from fastapi import FastAPI

load_dotenv()

app = FastAPI()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
MESSAGE = 'Кто-то трогает API!'

@app.get('/')
def hello():
    
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': MESSAGE}
    response = requests.post(url, data=data)

    
    return response.json()
