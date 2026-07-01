from src.ai.provider import (
    AIProvider,
    get_models,
)


def test_provider_enum():

    assert AIProvider.OLLAMA.value == "Ollama"
    assert AIProvider.OPENAI.value == "OpenAI"


def test_get_models():

    models = get_models(AIProvider.OLLAMA.value)

    assert isinstance(models, list)
    assert len(models) > 0