import logging

from openai import AsyncOpenAI
from openai.types.chat import ChatCompletion
from config import settings

logger = logging.getLogger(__name__)

class LLMService:
    def __init__(self):
        self.client = AsyncOpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=settings.OPENROUTER_API_KEY,
        )
        self.model = settings.LLM_MODEL
        self.system_prompt = {"role": "system", "content": settings.LLM_SYSTEM_PROMPT}
        logger.info(f"LLMService initialized with model: {self.model}")

    async def get_completion(self, user_message_content: str, chat_history: list[dict]) -> str:
        messages = [self.system_prompt]
        messages.extend(chat_history[-settings.CHAT_HISTORY_LENGTH:])
        messages.append({"role": "user", "content": user_message_content})

        logger.info(f"Sending request to LLM with {len(messages)} messages.")
        try:
            chat_completion: ChatCompletion = await self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            logger.error(f"Error calling LLM: {e}")
            return "Извините, произошла ошибка при обработке вашего запроса."

llm_service = LLMService()
