import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
bot = Bot(TELEGRAM_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def echo(message: types.message):
    print('бот получил сообщение', message)
    await bot.send_message(CHAT_ID, 'Это @dp.message_handler')
