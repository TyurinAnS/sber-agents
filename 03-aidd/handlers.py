import logging

from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, ErrorEvent

from llm_service import llm_service

logger = logging.getLogger(__name__)

# Словарь для хранения истории диалогов
user_chat_history: dict[int, list[dict]] = {}

async def start_command_handler(message: Message):
    # При команде /start очищаем историю для текущего пользователя
    user_chat_history[message.from_user.id] = []
    logger.info(f"User {message.from_user.id} started conversation.")
    try:
        await message.answer("Привет! Я ваш личный сомелье, готов помочь с выбором вина.")
    except Exception as e:
        logger.error(f"Error sending start message to user {message.from_user.id}: {e}")

async def text_message_handler(message: Message):
    if message.text:
        user_id = message.from_user.id
        logger.info(f"User {user_id} sent message: {message.text}")

        if user_id not in user_chat_history:
            user_chat_history[user_id] = []
        
        # Сохраняем сообщение пользователя в историю перед отправкой в LLM
        user_chat_history[user_id].append({"role": "user", "content": message.text})

        try:
            # Передаем только содержимое сообщения и историю
            response_from_llm = await llm_service.get_completion(
                user_message_content=message.text,
                chat_history=user_chat_history[user_id]
            )
            logger.info(f"Received response from LLM for user {user_id}.")

            # Сохраняем ответ LLM в историю
            user_chat_history[user_id].append({"role": "assistant", "content": response_from_llm})

            await message.answer(response_from_llm)
            logger.info(f"Sent response to user {user_id}.")
        except Exception as e:
            logger.error(f"Error processing message for user {user_id}: {e}")
            try:
                await message.answer("Извините, произошла внутренняя ошибка. Пожалуйста, попробуйте еще раз.")
            except Exception as e_send:
                logger.error(f"Error sending error message to user {user_id}: {e_send}")

async def error_handler(event: ErrorEvent):
    logger.error(f"Exception in handler: {event.exception}", exc_info=True)

# Функция регистрации хэндлеров теперь принимает user_chat_history
def register_handlers(dp: Dispatcher, chat_history: dict[int, list[dict]]):
    global user_chat_history
    user_chat_history = chat_history
    dp.message.register(start_command_handler, CommandStart())
    dp.message.register(text_message_handler)
    dp.errors.register(error_handler)
