from src.ai.provider import AIProvider
from src.ai.ollama_client import OllamaClient
from src.ai.openai_client import OpenAIClient


class SecurityAnalyzer:

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
    # Source Code Security
    # -----------------------------------------------------

    def analyze_code(
        self,
        provider,
        model,
        filename,
        code,
    ):

        prompt = f"""
You are a Senior Application Security Engineer.

Analyze the following source code.

Filename:
{filename}

Source Code:

{code}

Identify:

- SQL Injection
- Command Injection
- XSS
- CSRF
- SSRF
- Authentication Issues
- Authorization Issues
- Hardcoded Secrets
- Sensitive Information Exposure
- Unsafe File Uploads
- Path Traversal
- Deserialization Risks
- Input Validation Problems
- Dependency Risks

For every finding include:

Severity

Explanation

Impact

Recommended Fix

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # -----------------------------------------------------
    # Repository Security
    # -----------------------------------------------------

    def analyze_repository(
        self,
        provider,
        model,
        repository_information,
    ):

        prompt = f"""
Analyze the security posture of this repository.

Repository:

{repository_information}

Generate

Security Score

Critical Issues

High Risk

Medium Risk

Low Risk

Best Practices

Recommendations

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # -----------------------------------------------------
    # Dependency Security
    # -----------------------------------------------------

    def dependency_scan(
        self,
        provider,
        model,
        dependencies,
    ):

        prompt = f"""
Review the following dependencies.

{dependencies}

Identify

Outdated Packages

Known Risks

Deprecated Libraries

Upgrade Recommendations

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # -----------------------------------------------------
    # Secret Scan
    # -----------------------------------------------------

    def secret_scan(
        self,
        provider,
        model,
        code,
    ):

        prompt = f"""
Inspect the following code.

{code}

Detect

API Keys

Passwords

Private Keys

JWT Secrets

Database Credentials

Tokens

Environment Variables

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )