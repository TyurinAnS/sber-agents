from openai import AsyncOpenAI
from config import settings

class LLMService:
    def __init__(self):
        self.client = AsyncOpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=settings.OPENROUTER_API_KEY,
        )
        self.model = settings.LLM_MODEL

    async def get_completion(self, prompt: str) -> str:
        messages = [
            {"role": "user", "content": prompt}
        ]
        chat_completion = await self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
        )
        return chat_completion.choices[0].message.content

llm_service = LLMService()
