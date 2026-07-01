from src.ai.provider import AIProvider
from src.ai.ollama_client import OllamaClient
from src.ai.openai_client import OpenAIClient


class TestGenerator:

    def __init__(self):

        self.ollama = OllamaClient()
        self.openai = OpenAIClient()

    # ----------------------------------------------------
    # AI Provider
    # ----------------------------------------------------

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

    # ----------------------------------------------------
    # Python Tests (PyTest)
    # ----------------------------------------------------

    def pytest(
        self,
        provider,
        model,
        filename,
        code,
    ):

        prompt = f"""
You are a Senior Python Test Engineer.

Generate comprehensive PyTest test cases.

Filename

{filename}

Source Code

{code}

Generate

- Unit Tests
- Edge Cases
- Exception Tests
- Mock Tests
- Fixtures
- Assertions

Return complete executable Python code.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Java Tests (JUnit)
    # ----------------------------------------------------

    def junit(
        self,
        provider,
        model,
        filename,
        code,
    ):

        prompt = f"""
Generate professional JUnit tests.

Filename

{filename}

Source Code

{code}

Generate complete JUnit test class.

Return Java code only.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # JavaScript Tests (Jest)
    # ----------------------------------------------------

    def jest(
        self,
        provider,
        model,
        filename,
        code,
    ):

        prompt = f"""
Generate Jest unit tests.

Filename

{filename}

Code

{code}

Return executable Jest code.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # PHP Tests (PHPUnit)
    # ----------------------------------------------------

    def phpunit(
        self,
        provider,
        model,
        filename,
        code,
    ):

        prompt = f"""
Generate PHPUnit tests.

Filename

{filename}

Code

{code}

Return executable PHPUnit code.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Integration Tests
    # ----------------------------------------------------

    def integration_tests(
        self,
        provider,
        model,
        project_name,
        project_context,
    ):

        prompt = f"""
Generate integration tests.

Project

{project_name}

Context

{project_context}

Generate

- Integration Tests
- API Tests
- Database Tests
- Service Tests

Return executable code.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Test Coverage Report
    # ----------------------------------------------------

    def coverage_report(
        self,
        provider,
        model,
        project_name,
        source_code,
    ):

        prompt = f"""
Analyze test coverage.

Project

{project_name}

Code

{source_code}

Generate

Coverage Report

Missing Tests

Critical Paths

Recommendations

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )