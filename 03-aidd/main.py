import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import settings
from handlers import register_handlers, user_chat_history

async def main():
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
    dp = Dispatcher()

    # Передаем user_chat_history в функцию регистрации хэндлеров
    register_handlers(dp, user_chat_history)

    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
