import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN")
    OPENROUTER_API_KEY: str = os.getenv("OPENROUTER_API_KEY")
    LLM_MODEL: str = os.getenv("LLM_MODEL", "gpt-3.5-turbo")
    LLM_SYSTEM_PROMPT: str = os.getenv("LLM_SYSTEM_PROMPT", "Ты - опытный сомелье, который помогает пользователям выбрать вино.")
    CHAT_HISTORY_LENGTH: int = int(os.getenv("CHAT_HISTORY_LENGTH", 5))

settings = Settings()
