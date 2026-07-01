from src.ai.provider import AIProvider
from src.ai.ollama_client import OllamaClient
from src.ai.openai_client import OpenAIClient


class ChangelogGenerator:

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
    # CHANGELOG.md
    # ----------------------------------------------------

    def changelog(
        self,
        provider,
        model,
        repository,
        commits,
    ):

        prompt = f"""
You are a Senior Release Engineer.

Generate a professional CHANGELOG.md.

Repository

{repository}

Commits

{commits}

Generate

# Version

## Added

## Changed

## Fixed

## Removed

## Deprecated

## Security

Markdown Format.
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
        repository,
        commits,
    ):

        prompt = f"""
Generate GitHub Release Notes.

Repository

{repository}

Commits

{commits}

Include

Overview

Features

Bug Fixes

Performance

Security

Known Issues

Upgrade Notes

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Semantic Version
    # ----------------------------------------------------

    def semantic_version(
        self,
        provider,
        model,
        commits,
    ):

        prompt = f"""
Analyze the following commits.

Commits

{commits}

Recommend

Major

Minor

Patch

Explain why.

Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Migration Guide
    # ----------------------------------------------------

    def migration_guide(
        self,
        provider,
        model,
        old_version,
        new_version,
        commits,
    ):

        prompt = f"""
Generate a migration guide.

Old Version

{old_version}

New Version

{new_version}

Commits

{commits}

Include

Breaking Changes

Migration Steps

Configuration Changes

Deprecated APIs

Examples

Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Breaking Changes
    # ----------------------------------------------------

    def breaking_changes(
        self,
        provider,
        model,
        commits,
    ):

        prompt = f"""
Identify breaking changes.

Commits

{commits}

Generate

Breaking Changes

Affected Modules

Migration Advice

Risk Level

Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Release Summary
    # ----------------------------------------------------

    def release_summary(
        self,
        provider,
        model,
        repository,
        commits,
    ):

        prompt = f"""
Generate an executive release summary.

Repository

{repository}

Commits

{commits}

Include

Business Summary

Developer Summary

Technical Highlights

Security Improvements

Performance Improvements

Overall Recommendation

Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )