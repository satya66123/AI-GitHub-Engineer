# src/ai/streaming.py

import time

from src.ai.provider import AIProvider
from src.ai.ollama_client import OllamaClient
from src.ai.openai_client import OpenAIClient


class StreamingAI:

    def __init__(self):

        self.ollama = OllamaClient()

        self.openai = OpenAIClient()

    # --------------------------------------------------------
    # Generate Complete Response
    # --------------------------------------------------------

    def generate(
        self,
        provider,
        model,
        prompt,
    ):

        if provider == AIProvider.OPENAI.value:

            return self.openai.generate(
                prompt=prompt,
                model=model,
            )

        return self.ollama.generate(
            prompt=prompt,
            model=model,
        )

    # --------------------------------------------------------
    # Simulated Streaming
    # --------------------------------------------------------

    def stream(
        self,
        provider,
        model,
        prompt,
    ):

        response = self.generate(
            provider,
            model,
            prompt,
        )

        words = response.split()

        partial = ""

        for word in words:

            partial += word + " "

            yield partial

            time.sleep(0.01)

    # --------------------------------------------------------
    # Character Streaming
    # --------------------------------------------------------

    def stream_characters(
        self,
        provider,
        model,
        prompt,
    ):

        response = self.generate(
            provider,
            model,
            prompt,
        )

        partial = ""

        for character in response:

            partial += character

            yield partial

            time.sleep(0.002)

    # --------------------------------------------------------
    # Generator
    # --------------------------------------------------------

    def stream_generator(
        self,
        provider,
        model,
        prompt,
    ):

        for chunk in self.stream(
            provider,
            model,
            prompt,
        ):

            yield chunk