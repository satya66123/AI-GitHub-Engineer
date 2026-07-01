from src.ai.provider import AIProvider
from src.ai.ollama_client import OllamaClient
from src.ai.openai_client import OpenAIClient


class CommitAnalyzer:

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
    # Analyze Commit
    # ----------------------------------------------------

    def analyze_commit(
        self,
        provider,
        model,
        repository,
        commit,
    ):

        prompt = f"""
You are a Principal Software Engineer.

Analyze the following Git commit.

Repository

{repository}

Commit

{commit}

Generate

Executive Summary

Purpose

Files Changed

Business Impact

Architecture Impact

Performance Impact

Security Impact

Risk Level

Maintainability

Recommendations

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Commit History Analysis
    # ----------------------------------------------------

    def analyze_history(
        self,
        provider,
        model,
        repository,
        commits,
    ):

        prompt = f"""
Analyze the commit history.

Repository

{repository}

Commits

{commits}

Generate

Development Summary

Feature Timeline

Bug Fix Timeline

Developer Productivity

Repository Health

Code Churn

High Risk Areas

Recommendations

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Commit Quality
    # ----------------------------------------------------

    def quality_report(
        self,
        provider,
        model,
        commit,
    ):

        prompt = f"""
Review the following Git commit.

Commit

{commit}

Evaluate

Commit Message

Coding Standards

Best Practices

Security

Performance

Documentation

Testing

Assign a score out of 100.

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Generate Commit Message
    # ----------------------------------------------------

    def generate_commit_message(
        self,
        provider,
        model,
        changes,
    ):

        prompt = f"""
Generate professional Git commit messages.

Changes

{changes}

Generate

1. Conventional Commit

2. Short Commit

3. Detailed Commit

4. Release Commit

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Changelog Entry
    # ----------------------------------------------------

    def changelog(
        self,
        provider,
        model,
        commit,
    ):

        prompt = f"""
Generate a changelog entry.

Commit

{commit}

Return

Version

Added

Changed

Fixed

Removed

Markdown format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Release Notes
    # ----------------------------------------------------

    def release_notes(
        self,
        provider,
        model,
        commits,
    ):

        prompt = f"""
Generate professional release notes.

Commits

{commits}

Include

Overview

New Features

Bug Fixes

Improvements

Breaking Changes

Known Issues

Upgrade Notes

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )