
import os

import uvicorn
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from fastapi import FastAPI

import My_bot

load_dotenv()

app = FastAPI()


NGROK_TUNNEL = "https://8e27-90-154-73-138.ngrok.io"
WEBHOOK_PATH = f"/bot/{My_bot.TELEGRAM_TOKEN}"
WEBHOOK_URL = f"{NGROK_TUNNEL}{WEBHOOK_PATH}"

    
@app.on_event("startup")
async def on_startup():
    webhook_info = await My_bot.bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await My_bot.bot.set_webhook(
            url=WEBHOOK_URL
        )


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(My_bot.dp)
    Bot.set_current(My_bot.bot)
    print ('fast API получил обновление:', update)
    await My_bot.dp.process_update(telegram_update)


@app.on_event("shutdown")
async def on_shutdown():
    await My_bot.bot.session.close()
    


@app.get('/')
async def hello():
    print ('Get на на fast api')
    return 'Это обычный ответ FAST API"'


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
