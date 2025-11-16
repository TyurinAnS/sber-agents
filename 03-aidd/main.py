import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import settings
from handlers import register_handlers

async def main():
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
    dp = Dispatcher()

    register_handlers(dp)

    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
