import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import settings
from handlers import register_handlers, user_chat_history

# Настраиваем базовое логгирование
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

async def main():
    logger.info("Starting bot...")
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
    dp = Dispatcher()

    register_handlers(dp, user_chat_history)

    await dp.start_polling(bot)
    logger.info("Bot stopped.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped manually by KeyboardInterrupt.")
    except Exception as e:
        logger.error(f"Bot stopped with an error: {e}")
