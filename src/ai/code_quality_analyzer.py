from src.ai.provider import AIProvider
from src.ai.ollama_client import OllamaClient
from src.ai.openai_client import OpenAIClient


class CodeQualityAnalyzer:

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
    # Code Quality Analysis
    # ----------------------------------------------------

    def analyze(
        self,
        provider,
        model,
        filename,
        code,
    ):

        prompt = f"""
You are a Principal Software Engineer.

Perform a professional code quality review.

Filename

{filename}

Source Code

{code}

Evaluate

Readability

Maintainability

Naming Conventions

Modularity

Documentation

Exception Handling

Logging

Performance

Security

Overall Quality Score

Recommendations

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Coding Standards
    # ----------------------------------------------------

    def coding_standards(
        self,
        provider,
        model,
        filename,
        code,
    ):

        prompt = f"""
Review coding standards.

Filename

{filename}

Code

{code}

Check

PEP8 / Language Standards

Formatting

Naming

Imports

Comments

Best Practices

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Duplicate Code Detection
    # ----------------------------------------------------

    def duplicate_code(
        self,
        provider,
        model,
        repository_files,
    ):

        prompt = f"""
Analyze repository files.

Files

{repository_files}

Identify

Duplicate Logic

Repeated Functions

Repeated Classes

Refactoring Opportunities

Recommendations

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Dead Code Detection
    # ----------------------------------------------------

    def dead_code(
        self,
        provider,
        model,
        repository_files,
    ):

        prompt = f"""
Detect dead code.

Repository Files

{repository_files}

Identify

Unused Functions

Unused Classes

Unused Variables

Unused Imports

Deprecated Logic

Recommendations

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Maintainability
    # ----------------------------------------------------

    def maintainability(
        self,
        provider,
        model,
        repository_information,
    ):

        prompt = f"""
Evaluate maintainability.

Repository

{repository_information}

Analyze

Complexity

Coupling

Cohesion

Reusability

Scalability

Technical Debt

Maintainability Score

Recommendations

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Overall Repository Quality
    # ----------------------------------------------------

    def repository_quality(
        self,
        provider,
        model,
        repository,
        repository_information,
    ):

        prompt = f"""
Generate a repository quality report.

Repository

{repository}

Repository Information

{repository_information}

Evaluate

Architecture

Documentation

Security

Performance

Testing

Maintainability

Code Quality

Overall Grade

Improvement Roadmap

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )