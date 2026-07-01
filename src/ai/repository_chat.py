from src.ai.provider import AIProvider
from src.ai.ollama_client import OllamaClient
from src.ai.openai_client import OpenAIClient


class RepositoryChat:

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
    # Ask Repository
    # ----------------------------------------------------

    def ask(
        self,
        provider,
        model,
        repository,
        repository_context,
        question,
    ):

        prompt = f"""
You are an Expert Software Architect.

Answer questions about the following GitHub repository.

Repository

{repository}

Repository Context

{repository_context}

Question

{question}

Answer using only the provided repository context.

Include

Summary

Explanation

Relevant Files

Recommendations

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Explain Architecture
    # ----------------------------------------------------

    def explain_architecture(
        self,
        provider,
        model,
        repository,
        repository_context,
    ):

        prompt = f"""
Explain the architecture.

Repository

{repository}

Repository Context

{repository_context}

Include

Architecture Overview

Layers

Components

Data Flow

Folder Responsibilities

Best Practices

Improvement Suggestions

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Explain Authentication
    # ----------------------------------------------------

    def authentication_flow(
        self,
        provider,
        model,
        repository_context,
    ):

        prompt = f"""
Analyze authentication.

Repository Context

{repository_context}

Explain

Authentication Flow

Authorization

Security

JWT

Sessions

Tokens

Recommendations

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Find API Endpoints
    # ----------------------------------------------------

    def api_endpoints(
        self,
        provider,
        model,
        repository_context,
    ):

        prompt = f"""
Identify all API endpoints.

Repository Context

{repository_context}

Generate

Endpoint

Method

Purpose

Authentication

Request

Response

Markdown Table.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Database Analysis
    # ----------------------------------------------------

    def database_analysis(
        self,
        provider,
        model,
        repository_context,
    ):

        prompt = f"""
Analyze database usage.

Repository Context

{repository_context}

Explain

Database Technology

Models

Schema

Queries

Relationships

Optimization Suggestions

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Dependency Explanation
    # ----------------------------------------------------

    def dependency_explanation(
        self,
        provider,
        model,
        dependency_files,
    ):

        prompt = f"""
Explain project dependencies.

Dependency Files

{dependency_files}

Generate

Dependency Name

Purpose

Usage

Alternatives

Security Considerations

Markdown Table.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Improvement Suggestions
    # ----------------------------------------------------

    def improvement_suggestions(
        self,
        provider,
        model,
        repository,
        repository_context,
    ):

        prompt = f"""
Suggest improvements.

Repository

{repository}

Repository Context

{repository_context}

Generate

Architecture Improvements

Performance Improvements

Security Improvements

Testing Improvements

Documentation Improvements

Scalability Improvements

Prioritized Roadmap

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Repository Summary
    # ----------------------------------------------------

    def repository_summary(
        self,
        provider,
        model,
        repository,
        repository_context,
    ):

        prompt = f"""
Create an executive repository summary.

Repository

{repository}

Repository Context

{repository_context}

Generate

Project Purpose

Key Features

Technology Stack

Architecture

Strengths

Weaknesses

Overall Assessment

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )