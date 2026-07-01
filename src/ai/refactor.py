from src.ai.provider import AIProvider
from src.ai.ollama_client import OllamaClient
from src.ai.openai_client import OpenAIClient


class RefactorEngine:

    def __init__(self):
        self.ollama = OllamaClient()
        self.openai = OpenAIClient()

    # -----------------------------------------------------
    # Provider
    # -----------------------------------------------------

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

    # -----------------------------------------------------
    # Refactor Code
    # -----------------------------------------------------

    def refactor_code(
        self,
        provider,
        model,
        filename,
        code,
    ):

        prompt = f"""
You are an Expert Software Engineer.

Refactor the following code.

Filename

{filename}

Code

{code}

Improve

- Readability

- Performance

- Maintainability

- Naming

- Structure

- Documentation

Return

1. Improved Code

2. Explanation

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # -----------------------------------------------------
    # Clean Code
    # -----------------------------------------------------

    def clean_code(
        self,
        provider,
        model,
        filename,
        code,
    ):

        prompt = f"""
Rewrite the following code using clean code principles.

Filename

{filename}

Code

{code}

Apply

- SOLID

- DRY

- KISS

- Separation of Concerns

- Better Naming

Return improved code.

Explain changes.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # -----------------------------------------------------
    # Optimize Code
    # -----------------------------------------------------

    def optimize(
        self,
        provider,
        model,
        filename,
        code,
    ):

        prompt = f"""
Optimize the following code.

Filename

{filename}

Code

{code}

Improve

Performance

Memory

Complexity

Scalability

Return optimized code.

Explain improvements.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # -----------------------------------------------------
    # Modernize
    # -----------------------------------------------------

    def modernize(
        self,
        provider,
        model,
        filename,
        code,
    ):

        prompt = f"""
Modernize the following code.

Filename

{filename}

Code

{code}

Use

Latest language features

Modern libraries

Best practices

Return improved source code.

Explain improvements.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # -----------------------------------------------------
    # Improve Project
    # -----------------------------------------------------

    def improve_project(
        self,
        provider,
        model,
        repository_information,
    ):

        prompt = f"""
You are an Expert Software Architect.

Repository

{repository_information}

Suggest improvements.

Include

Architecture

Folder Structure

Code Organization

Performance

Security

Testing

Documentation

CI/CD

Future Scope

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )