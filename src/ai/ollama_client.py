import requests

from src.config.settings import settings
from src.utils.logger import logger


class OllamaClient:

    def __init__(self):
        self.url = settings.OLLAMA_URL

    def generate(
        self,
        prompt: str,
        model: str,
        temperature: float = 0.2,
        max_tokens: int = 2048,
    ):

        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens,
            },
        }

        try:

            response = requests.post(
                self.url,
                json=payload,
                timeout=300000,
            )

            response.raise_for_status()

            data = response.json()

            return data.get("response", "")

        except Exception as e:

            logger.error(f"Ollama Error : {e}")

            return f"Error : {e}"

    def health_check(self):

        try:

            response = requests.get(
                "http://localhost:11434/api/tags",
                timeout=10,
            )

            return response.status_code == 200

        except Exception:

            return False

    def get_models(self):

        try:

            response = requests.get(
                "http://localhost:11434/api/tags",
                timeout=10,
            )

            response.raise_for_status()

            data = response.json()

            models = []

            for model in data.get("models", []):

                models.append(model["name"])

            return models

        except Exception:

            return []