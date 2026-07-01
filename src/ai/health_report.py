from src.ai.provider import AIProvider
from src.ai.ollama_client import OllamaClient
from src.ai.openai_client import OpenAIClient


class HealthReport:

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
    # Repository Health
    # -----------------------------------------------------

    def analyze(
        self,
        provider,
        model,
        repository_name,
        repository_information,
    ):

        prompt = f"""
You are an Expert Software Architect.

Analyze the following GitHub repository.

Repository:
{repository_name}

Repository Information:

{repository_information}

Generate a Repository Health Report.

Include:

# Overall Score (0-100)

# Architecture

# Code Quality

# Documentation

# Security

# Performance

# Maintainability

# Scalability

# Testability

# Dependency Management

# Strengths

# Weaknesses

# Risks

# Recommendations

Give every section a score.

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # -----------------------------------------------------
    # Architecture Score
    # -----------------------------------------------------

    def architecture(
        self,
        provider,
        model,
        repository_information,
    ):

        prompt = f"""
Analyze repository architecture.

Repository

{repository_information}

Evaluate

- Layers

- Folder Structure

- Separation of Concerns

- Modularity

- Design Pattern

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # -----------------------------------------------------
    # Maintainability
    # -----------------------------------------------------

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

Include

- Complexity

- Readability

- Documentation

- Naming

- Reusability

- Technical Debt

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # -----------------------------------------------------
    # Production Readiness
    # -----------------------------------------------------

    def production_ready(
        self,
        provider,
        model,
        repository_information,
    ):

        prompt = f"""
Is this repository production ready?

Repository

{repository_information}

Evaluate

Deployment

Security

Logging

Monitoring

Testing

Configuration

CI/CD

Docker

Documentation

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )