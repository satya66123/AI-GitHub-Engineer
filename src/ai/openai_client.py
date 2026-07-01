from openai import OpenAI

from src.config.settings import settings
from src.utils.logger import logger


class OpenAIClient:

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    def generate(
        self,
        prompt: str,
        model: str = "gpt-4.1-mini",
        temperature: float = 0.2,
        max_tokens: int = 2048,
    ):

        try:

            response = self.client.responses.create(
                model=model,
                input=prompt,
                temperature=temperature,
                max_output_tokens=max_tokens,
            )

            return response.output_text

        except Exception as e:

            logger.error(f"OpenAI Error : {e}")

            return f"Error : {e}"

    def health_check(self):

        try:

            self.client.models.list()

            return True

        except Exception:

            return False

    def get_models(self):

        try:

            models = self.client.models.list()

            available = []

            for model in models.data:

                if model.id.startswith("gpt"):

                    available.append(model.id)

            return sorted(available)

        except Exception:

            return []