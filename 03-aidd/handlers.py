from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from llm_service import llm_service

# Словарь для хранения истории диалогов
user_chat_history: dict[int, list[dict]] = {}

async def start_command_handler(message: Message):
    # При команде /start очищаем историю для текущего пользователя
    user_chat_history[message.from_user.id] = []
    await message.answer("Привет! Я ваш личный сомелье, готов помочь с выбором вина.")

async def text_message_handler(message: Message):
    if message.text:
        user_id = message.from_user.id
        if user_id not in user_chat_history:
            user_chat_history[user_id] = []
        
        # Сохраняем сообщение пользователя в историю перед отправкой в LLM
        user_chat_history[user_id].append({"role": "user", "content": message.text})

        # Передаем только содержимое сообщения и историю
        response_from_llm = await llm_service.get_completion(
            user_message_content=message.text,
            chat_history=user_chat_history[user_id]
        )

        # Сохраняем ответ LLM в историю
        user_chat_history[user_id].append({"role": "assistant", "content": response_from_llm})

        await message.answer(response_from_llm)

# Функция регистрации хэндлеров теперь принимает user_chat_history
def register_handlers(dp: Dispatcher, chat_history: dict[int, list[dict]]):
    global user_chat_history
    user_chat_history = chat_history
    dp.message.register(start_command_handler, CommandStart())
    dp.message.register(text_message_handler)
