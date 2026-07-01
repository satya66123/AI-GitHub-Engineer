from src.ai.provider import (
    AIProvider,
    OLLAMA_MODELS,
    OPENAI_MODELS,
)


class AIModels:

    @staticmethod
    def providers():

        return [
            AIProvider.OLLAMA.value,
            AIProvider.OPENAI.value,
        ]

    @staticmethod
    def ollama():

        return OLLAMA_MODELS

    @staticmethod
    def openai():

        return OPENAI_MODELS

    @staticmethod
    def models(provider):

        if provider == AIProvider.OPENAI.value:
            return OPENAI_MODELS

        return OLLAMA_MODELS

    @staticmethod
    def default(provider):

        if provider == AIProvider.OPENAI.value:

            if OPENAI_MODELS:
                return OPENAI_MODELS[0]

            return "gpt-4.1-mini"

        if OLLAMA_MODELS:
            return OLLAMA_MODELS[0]

        return "qwen2.5:1.5b"

    @staticmethod
    def exists(provider, model):

        return model in AIModels.models(provider)