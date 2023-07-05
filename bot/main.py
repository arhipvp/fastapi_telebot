from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
MESSAGE = 'Кто-то пишет в телегу'

bot = Bot(TELEGRAM_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=MESSAGE)


if __name__ == '__main__':

    print('бот пошел епта')

    executor.start_polling(dp)
