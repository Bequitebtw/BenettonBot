import asyncio
import logging

from aiogram import Bot,Dispatcher
from dotenv import load_dotenv
import os
load_dotenv()
from handlers.user_handlers import user_router
from handlers.admin_handlers import admin_router
from handlers.feedback_fsm import feedback_router
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()


# Функция запуска бота
async def run():
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_routers(admin_router,feedback_router,user_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print("exit")