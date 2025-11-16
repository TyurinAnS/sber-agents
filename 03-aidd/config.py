import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.TELEGRAM_BOT_TOKEN: str = self._get_env_variable("TELEGRAM_BOT_TOKEN")
        self.OPENROUTER_API_KEY: str = self._get_env_variable("OPENROUTER_API_KEY")
        self.LLM_MODEL: str = os.getenv("LLM_MODEL", "gpt-3.5-turbo")
        self.LLM_SYSTEM_PROMPT: str = os.getenv("LLM_SYSTEM_PROMPT", "Ты - опытный сомелье, который помогает пользователям выбрать вино.")
        self.CHAT_HISTORY_LENGTH: int = int(os.getenv("CHAT_HISTORY_LENGTH", 5))

    def _get_env_variable(self, key: str) -> str:
        value = os.getenv(key)
        if not value:
            raise ValueError(f"Environment variable {key} is not set.")
        return value

settings = Settings()
