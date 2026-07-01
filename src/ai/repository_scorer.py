from src.ai.provider import AIProvider
from src.ai.ollama_client import OllamaClient
from src.ai.openai_client import OpenAIClient


class RepositoryScorer:

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
    # Overall Repository Score
    # ----------------------------------------------------

    def score_repository(
        self,
        provider,
        model,
        repository,
        repository_information,
    ):

        prompt = f"""
You are a Principal Software Architect and Senior Code Reviewer.

Your job is to evaluate ONLY the repository information provided below.

IMPORTANT RULES

1. Do NOT invent tools, frameworks, CI/CD pipelines, security scanners, or testing frameworks.
2. Do NOT assume Docker, Kubernetes, Jenkins, Redis, RabbitMQ, GitHub Actions, or any technology unless it appears in the repository information.
3. If information is missing, explicitly state:
   "Not enough information available."
4. Base every score only on the supplied repository data.
5. Keep recommendations practical and relevant to this repository.

Repository Name

{repository}

Repository Information

{repository_information}

Evaluate the repository in the following categories.

1. Architecture
- Score (0-10)
- Evidence
- Strengths
- Weaknesses
- Recommendations

2. Code Quality
- Score
- Evidence
- Strengths
- Weaknesses
- Recommendations

3. Documentation
- Score
- Evidence
- Strengths
- Weaknesses
- Recommendations

4. Security
- Score
- Evidence
- Strengths
- Weaknesses
- Recommendations

5. Performance
- Score
- Evidence
- Strengths
- Weaknesses
- Recommendations

6. Testing
- Score
- Evidence
- Strengths
- Weaknesses
- Recommendations

7. Maintainability
- Score
- Evidence
- Strengths
- Weaknesses
- Recommendations

8. Scalability
- Score
- Evidence
- Strengths
- Weaknesses
- Recommendations

9. Dependency Management
- Score
- Evidence
- Strengths
- Weaknesses
- Recommendations

10. Production Readiness
- Score
- Evidence
- Strengths
- Weaknesses
- Recommendations

Finally generate:

Overall Score (0-100)

Grade

Executive Summary

Top 5 Strengths

Top 5 Improvements

Three High-Priority Tasks

Conclusion

Return Markdown only.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Architecture Score
    # ----------------------------------------------------

    def architecture_score(
        self,
        provider,
        model,
        repository_information,
    ):

        prompt = f"""
Evaluate repository architecture.

Repository

{repository_information}

Analyze

Architecture

Folder Structure

Layer Separation

Modularity

Design Patterns

Assign a score out of 10.

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Code Quality Score
    # ----------------------------------------------------

    def code_quality(
        self,
        provider,
        model,
        source_code,
    ):

        prompt = f"""
Evaluate the following source code.

{source_code}

Score

Readability

Maintainability

Naming

Documentation

Complexity

Best Practices

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Security Score
    # ----------------------------------------------------

    def security_score(
        self,
        provider,
        model,
        repository_information,
    ):

        prompt = f"""
Analyze repository security.

Repository

{repository_information}

Evaluate

Secrets

Authentication

Authorization

Dependency Security

Configuration

Assign score out of 10.

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Documentation Score
    # ----------------------------------------------------

    def documentation_score(
        self,
        provider,
        model,
        repository_information,
    ):

        prompt = f"""
Evaluate project documentation.

Repository

{repository_information}

Analyze

README

Comments

API Docs

Examples

Installation

Assign score.

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Testing Score
    # ----------------------------------------------------

    def testing_score(
        self,
        provider,
        model,
        repository_information,
    ):

        prompt = f"""
Evaluate testing quality.

Repository

{repository_information}

Analyze

Unit Tests

Integration Tests

Coverage

Automation

Assign score.

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Production Readiness
    # ----------------------------------------------------

    def production_readiness(
        self,
        provider,
        model,
        repository_information,
    ):

        prompt = f"""
Evaluate production readiness.

Repository

{repository_information}

Analyze

Docker

CI/CD

Logging

Monitoring

Configuration

Deployment

Security

Scalability

Assign score.

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Improvement Roadmap
    # ----------------------------------------------------

    def improvement_plan(
        self,
        provider,
        model,
        repository_information,
    ):

        prompt = f"""
Create an improvement roadmap.

Repository

{repository_information}

Generate

Immediate Improvements

Short Term

Medium Term

Long Term

Priority

Estimated Difficulty

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )