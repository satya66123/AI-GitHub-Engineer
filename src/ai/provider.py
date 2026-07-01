from enum import Enum


class AIProvider(Enum):
    OLLAMA = "Ollama"
    OPENAI = "OpenAI"


OLLAMA_MODELS = [
    "qwen2.5:1.5b",
    "phi3:latest",
    "gemma2:2b",
    "gemma3:4b",
    "deepseek-coder:latest",
    "llama3:8b",
    "llama3:latest",
    "llama3.1:8b",
    "mistral:latest",
    "qwen3:latest",
    "qwen3:8b",
]

OPENAI_MODELS = [
    "gpt-4.1-mini",
    "gpt-4.1",
    "gpt-4o-mini",
    "gpt-4o",
]


def get_models(provider: str):

    if provider == AIProvider.OPENAI.value:
        return OPENAI_MODELS

    return OLLAMA_MODELS