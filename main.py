import asyncio
import logging

from aiogram import Bot,Dispatcher
from dotenv import load_dotenv
import os
load_dotenv()
from apps import handlers, feedback
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()

# Функция запуска бота
async def run():
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_routers(handlers.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print("exit")