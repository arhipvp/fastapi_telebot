
import os
import uvicorn
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from fastapi import FastAPI

import bot

load_dotenv()

app = FastAPI()


NGROK_TUNNEL = "https://8e27-90-154-73-138.ngrok.io"
WEBHOOK_PATH = f"/bot/{bot.TELEGRAM_TOKEN}"
WEBHOOK_URL = f"{NGROK_TUNNEL}{WEBHOOK_PATH}"

    
@app.on_event("startup")
async def on_startup():
    webhook_info = await bot.bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(
            url=WEBHOOK_URL
        )


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(bot.dp)
    Bot.set_current(bot.bot)
    
    await bot.dp.process_update(telegram_update)


@app.on_event("shutdown")
async def on_shutdown():
    await bot.session.close()
    


# @app.get('/')
# async def hello():
#     loop = asyncio.get_running_loop()
#     loop.create_task(send_message())
#     return MESSAGE


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
