from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

if __name__ == '__main__':

    bot = Bot(TELEGRAM_TOKEN)
    dp = Dispatcher(bot)

    @dp.message_handler()
    async def echo(message: types.message):
        await message.answer(text='кто-то потрогал api')

    executor.start_polling(dp)

