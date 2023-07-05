import asyncio
import sys

from dotenv import load_dotenv
from fastapi import FastAPI

# это я чтоб с командной строки запустить прокидываю путь к проекту в PYTHONPATH, без докера
sys.path.append('D:\\PyCharm_projects\\fastapi_telebot')

from bot.main import bot, CHAT_ID

load_dotenv()

app = FastAPI()

MESSAGE = 'Кто-то трогает API!'


async def send_message():
    await bot.send_message(CHAT_ID, MESSAGE)


@app.get('/')
async def hello():
    asyncio.get_running_loop().create_task(send_message())
    return MESSAGE
