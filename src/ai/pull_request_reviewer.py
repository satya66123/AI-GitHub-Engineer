from src.ai.provider import AIProvider
from src.ai.ollama_client import OllamaClient
from src.ai.openai_client import OpenAIClient


class PullRequestReviewer:

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
    # Review Pull Request
    # ----------------------------------------------------

    def review(
        self,
        provider,
        model,
        repository,
        pull_request,
    ):

        prompt = f"""
You are a Principal Software Engineer.

Review the following GitHub Pull Request.

Repository

{repository}

Pull Request

{pull_request}

Generate a professional review.

Include

Summary

Changed Components

Architecture Impact

Possible Bugs

Security Review

Performance Review

Code Quality

Maintainability

Suggested Improvements

Final Recommendation

Approve

Request Changes

Comment

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Review Changed Files
    # ----------------------------------------------------

    def changed_files(
        self,
        provider,
        model,
        files,
    ):

        prompt = f"""
Review the following changed files.

Files

{files}

Explain

Purpose

Risk

Code Quality

Suggestions

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Review Diff
    # ----------------------------------------------------

    def review_diff(
        self,
        provider,
        model,
        diff,
    ):

        prompt = f"""
Review this git diff.

Diff

{diff}

Find

Logic Problems

Performance Issues

Security Risks

Best Practices

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Generate Review Comments
    # ----------------------------------------------------

    def review_comments(
        self,
        provider,
        model,
        code,
    ):

        prompt = f"""
Generate GitHub review comments.

Code

{code}

Generate

Inline comments

Suggestions

Requested changes

Praise

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )