from src.ai.provider import AIProvider
from src.ai.ollama_client import OllamaClient
from src.ai.openai_client import OpenAIClient


class WorkflowAnalyzer:

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
    # GitHub Workflow Analysis
    # ----------------------------------------------------

    def analyze_workflow(
        self,
        provider,
        model,
        repository,
        workflow,
    ):

        prompt = f"""
You are a Senior DevOps Engineer.

Analyze the following GitHub Actions workflow.

Repository

{repository}

Workflow

{workflow}

Generate

Workflow Summary

CI/CD Pipeline

Jobs

Steps

Triggers

Deployment Strategy

Performance

Security

Best Practices

Recommendations

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # YAML Review
    # ----------------------------------------------------

    def yaml_review(
        self,
        provider,
        model,
        yaml_content,
    ):

        prompt = f"""
Review the following GitHub Actions YAML.

YAML

{yaml_content}

Evaluate

Syntax

Readability

Maintainability

Best Practices

Security

Performance

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Security Review
    # ----------------------------------------------------

    def security_review(
        self,
        provider,
        model,
        workflow,
    ):

        prompt = f"""
Perform a security audit.

Workflow

{workflow}

Find

Secrets Exposure

Token Permissions

Unsafe Actions

Supply Chain Risks

Recommendations

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Performance Optimization
    # ----------------------------------------------------

    def optimize_workflow(
        self,
        provider,
        model,
        workflow,
    ):

        prompt = f"""
Optimize this GitHub Actions workflow.

Workflow

{workflow}

Improve

Execution Time

Caching

Parallel Jobs

Artifacts

Resource Usage

Recommendations

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Deployment Review
    # ----------------------------------------------------

    def deployment_review(
        self,
        provider,
        model,
        workflow,
    ):

        prompt = f"""
Review deployment workflow.

Workflow

{workflow}

Analyze

Deployment Strategy

Rollback

Environment Variables

Approvals

Production Safety

Recommendations

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # CI/CD Report
    # ----------------------------------------------------

    def pipeline_report(
        self,
        provider,
        model,
        repository,
        workflow,
    ):

        prompt = f"""
Generate a professional CI/CD report.

Repository

{repository}

Workflow

{workflow}

Include

Pipeline Overview

Stages

Quality Gates

Security

Performance

Deployment

Overall Score

Improvement Roadmap

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )