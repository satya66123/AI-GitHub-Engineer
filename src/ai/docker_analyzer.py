from src.ai.provider import AIProvider
from src.ai.ollama_client import OllamaClient
from src.ai.openai_client import OpenAIClient


class DockerAnalyzer:

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
    # Dockerfile Analysis
    # ----------------------------------------------------

    def analyze_dockerfile(
        self,
        provider,
        model,
        repository,
        dockerfile,
    ):

        prompt = f"""
You are a Senior DevOps Engineer.

Analyze the following Dockerfile.

Repository

{repository}

Dockerfile

{dockerfile}

Generate

Overview

Base Image Review

Layers

Caching

Security

Performance

Best Practices

Recommendations

Overall Score

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Docker Compose Analysis
    # ----------------------------------------------------

    def analyze_compose(
        self,
        provider,
        model,
        compose_file,
    ):

        prompt = f"""
Review the following docker-compose.yml.

Compose File

{compose_file}

Analyze

Services

Networks

Volumes

Environment Variables

Dependencies

Security

Recommendations

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Container Security
    # ----------------------------------------------------

    def security_review(
        self,
        provider,
        model,
        dockerfile,
    ):

        prompt = f"""
Perform a Docker security review.

Dockerfile

{dockerfile}

Check

Root User

Privileges

Secrets

Image Vulnerabilities

Package Installation

Permissions

Recommendations

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Image Optimization
    # ----------------------------------------------------

    def optimize_image(
        self,
        provider,
        model,
        dockerfile,
    ):

        prompt = f"""
Optimize this Dockerfile.

Dockerfile

{dockerfile}

Improve

Image Size

Layer Caching

Performance

Security

Multi-stage Builds

Best Practices

Return optimized Dockerfile and explanation.

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Kubernetes Readiness
    # ----------------------------------------------------

    def kubernetes_readiness(
        self,
        provider,
        model,
        dockerfile,
    ):

        prompt = f"""
Evaluate Kubernetes readiness.

Dockerfile

{dockerfile}

Analyze

Health Checks

Resource Usage

Configuration

Environment Variables

Persistent Storage

Deployment Readiness

Recommendations

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Production Readiness
    # ----------------------------------------------------

    def production_report(
        self,
        provider,
        model,
        repository,
        dockerfile,
    ):

        prompt = f"""
Generate a Docker production readiness report.

Repository

{repository}

Dockerfile

{dockerfile}

Evaluate

Security

Performance

Scalability

Maintainability

Deployment

Monitoring

Logging

Overall Score

Improvement Roadmap

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )