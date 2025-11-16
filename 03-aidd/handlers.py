from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from llm_service import llm_service

async def start_command_handler(message: Message):
    await message.answer("Привет! Я ваш личный сомелье, готов помочь с выбором вина.")

async def text_message_handler(message: Message):
    if message.text:
        response_from_llm = await llm_service.get_completion(message.text)
        await message.answer(response_from_llm)

def register_handlers(dp: Dispatcher):
    dp.message.register(start_command_handler, CommandStart())
    dp.message.register(text_message_handler)
