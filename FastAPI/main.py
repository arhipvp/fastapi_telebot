import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from fastapi import FastAPI

load_dotenv()

app = FastAPI()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
MESSAGE = 'Кто-то трогает API!'
bot = Bot(TELEGRAM_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def send_message():
    await bot.send_message(CHAT_ID, MESSAGE)



@app.get('/')
async def hello():
    asyncio.get_running_loop().create_task(send_message())
    return MESSAGE
