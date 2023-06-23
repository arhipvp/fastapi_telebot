from fastapi import FastAPI
import httpx
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
MESSAGE = 'YOUR_MESSAGE'

@app.get('/')
def hello():
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': MESSAGE}

    client = httpx.AsyncClient()
    response = client.post(url, data=data)
    response.send(data)
    return 'jj'
