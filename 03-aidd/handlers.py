from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

async def start_command_handler(message: Message):
    await message.answer("Привет! Я ваш личный сомелье, готов помочь с выбором вина.")

def register_handlers(dp: Dispatcher):
    dp.message.register(start_command_handler, CommandStart())
