import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
MESSAGE = 'Кто-то трогает API!'
bot = Bot(TELEGRAM_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def echo(message: types.message):
    await bot.send_message(CHAT_ID, 'FFF FFF')
    
# @dp.message_handler()
# async def send_message():
#     await bot.send_message(CHAT_ID, MESSAGE)