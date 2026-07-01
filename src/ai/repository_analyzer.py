import json

from src.ai.provider import AIProvider
from src.ai.ollama_client import OllamaClient
from src.ai.openai_client import OpenAIClient
from src.ai.prompts import RepositoryPrompts


class RepositoryAnalyzer:

    def __init__(self):

        self.ollama = OllamaClient()
        self.openai = OpenAIClient()

    def _generate(
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

    def summarize(
        self,
        provider,
        model,
        repository_name,
        repository_data,
    ):

        prompt = RepositoryPrompts.repository_summary(
            repository_name,
            json.dumps(
                repository_data,
                indent=2,
            ),
        )

        return self._generate(
            provider,
            model,
            prompt,
        )

    def architecture(
        self,
        provider,
        model,
        repository_name,
        repository_data,
    ):

        prompt = RepositoryPrompts.architecture(
            repository_name,
            json.dumps(
                repository_data,
                indent=2,
            ),
        )

        return self._generate(
            provider,
            model,
            prompt,
        )

    def dependency_analysis(
        self,
        provider,
        model,
        repository_name,
        dependencies,
    ):

        prompt = RepositoryPrompts.dependency_analysis(
            repository_name,
            dependencies,
        )

        return self._generate(
            provider,
            model,
            prompt,
        )

    def readme_analysis(
        self,
        provider,
        model,
        repository_name,
        readme,
    ):

        prompt = RepositoryPrompts.readme_analysis(
            repository_name,
            readme,
        )

        return self._generate(
            provider,
            model,
            prompt,
        )

    def explain_code(
        self,
        provider,
        model,
        file_name,
        code,
    ):

        prompt = RepositoryPrompts.explain_code(
            file_name,
            code,
        )

        return self._generate(
            provider,
            model,
            prompt,
        )

    def bug_analysis(
        self,
        provider,
        model,
        file_name,
        code,
    ):

        prompt = RepositoryPrompts.bug_analysis(
            file_name,
            code,
        )

        return self._generate(
            provider,
            model,
            prompt,
        )

    def refactor(
        self,
        provider,
        model,
        file_name,
        code,
    ):

        prompt = RepositoryPrompts.refactor(
            file_name,
            code,
        )

        return self._generate(
            provider,
            model,
            prompt,
        )

    def documentation(
        self,
        provider,
        model,
        file_name,
        code,
    ):

        prompt = RepositoryPrompts.documentation(
            file_name,
            code,
        )

        return self._generate(
            provider,
            model,
            prompt,
        )

    def ask(
        self,
        provider,
        model,
        repository_context,
        question,
    ):

        prompt = RepositoryPrompts.ask(
            repository_context,
            question,
        )

        return self._generate(
            provider,
            model,
            prompt,
        )