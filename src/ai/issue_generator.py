from src.ai.provider import AIProvider
from src.ai.ollama_client import OllamaClient
from src.ai.openai_client import OpenAIClient


class IssueGenerator:

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
    # Bug Report
    # ----------------------------------------------------

    def bug_report(
        self,
        provider,
        model,
        repository,
        bug_description,
    ):

        prompt = f"""
You are an experienced GitHub Maintainer.

Generate a professional GitHub Bug Report.

Repository

{repository}

Bug Description

{bug_description}

Generate

Title

Summary

Environment

Steps to Reproduce

Expected Behavior

Actual Behavior

Screenshots Placeholder

Logs Placeholder

Root Cause

Suggested Fix

Priority

Severity

Labels

Milestone

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Feature Request
    # ----------------------------------------------------

    def feature_request(
        self,
        provider,
        model,
        repository,
        feature,
    ):

        prompt = f"""
Generate a professional GitHub Feature Request.

Repository

{repository}

Feature

{feature}

Generate

Title

Problem Statement

Proposed Solution

Benefits

Alternatives

Acceptance Criteria

Priority

Labels

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Enhancement
    # ----------------------------------------------------

    def enhancement(
        self,
        provider,
        model,
        repository,
        enhancement,
    ):

        prompt = f"""
Generate a GitHub Enhancement Issue.

Repository

{repository}

Enhancement

{enhancement}

Include

Title

Current Situation

Improvement

Benefits

Implementation Notes

Priority

Labels

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Documentation Issue
    # ----------------------------------------------------

    def documentation_issue(
        self,
        provider,
        model,
        repository,
        documentation_problem,
    ):

        prompt = f"""
Generate a Documentation Issue.

Repository

{repository}

Problem

{documentation_problem}

Generate

Title

Missing Documentation

Required Changes

Expected Outcome

Priority

Labels

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Security Issue
    # ----------------------------------------------------

    def security_issue(
        self,
        provider,
        model,
        repository,
        vulnerability,
    ):

        prompt = f"""
Generate a Security Issue.

Repository

{repository}

Security Finding

{vulnerability}

Generate

Title

Description

Impact

Severity

Affected Components

Suggested Fix

Priority

Labels

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Performance Issue
    # ----------------------------------------------------

    def performance_issue(
        self,
        provider,
        model,
        repository,
        performance_problem,
    ):

        prompt = f"""
Generate a Performance Improvement Issue.

Repository

{repository}

Performance Problem

{performance_problem}

Generate

Title

Current Performance

Expected Performance

Suggested Improvements

Acceptance Criteria

Priority

Labels

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Refactoring Task
    # ----------------------------------------------------

    def refactoring_task(
        self,
        provider,
        model,
        repository,
        refactoring_details,
    ):

        prompt = f"""
Generate a Refactoring Task.

Repository

{repository}

Task

{refactoring_details}

Generate

Title

Description

Scope

Benefits

Checklist

Priority

Labels

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Testing Task
    # ----------------------------------------------------

    def testing_task(
        self,
        provider,
        model,
        repository,
        testing_requirement,
    ):

        prompt = f"""
Generate a Testing Task.

Repository

{repository}

Requirement

{testing_requirement}

Generate

Title

Objective

Test Cases

Acceptance Criteria

Priority

Labels

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )