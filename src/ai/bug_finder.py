from src.ai.provider import AIProvider
from src.ai.ollama_client import OllamaClient
from src.ai.openai_client import OpenAIClient


class BugFinder:

    def __init__(self):
        self.ollama = OllamaClient()
        self.openai = OpenAIClient()

    # -----------------------------------------------------
    # AI Provider
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
    # Bug Detection
    # -----------------------------------------------------

    def analyze_code(
        self,
        provider,
        model,
        filename,
        code,
    ):

        prompt = f"""
You are an expert Software Engineer and Security Reviewer.

Analyze the following source code.

Filename:
{filename}

Code:

{code}

Find:

1. Syntax Issues
2. Logical Bugs
3. Runtime Errors
4. Performance Problems
5. Memory Issues
6. Security Vulnerabilities
7. Code Smells
8. Maintainability Problems

For every issue provide:

- Problem
- Severity
- Explanation
- Suggested Fix

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # -----------------------------------------------------
    # Security Scan
    # -----------------------------------------------------

    def security_scan(
        self,
        provider,
        model,
        filename,
        code,
    ):

        prompt = f"""
Perform a security review.

Filename:
{filename}

Code:

{code}

Check for:

- SQL Injection
- Command Injection
- XSS
- CSRF
- Authentication Issues
- Authorization Issues
- Secrets
- Hardcoded Passwords
- Insecure API Calls

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # -----------------------------------------------------
    # Performance Scan
    # -----------------------------------------------------

    def performance_scan(
        self,
        provider,
        model,
        filename,
        code,
    ):

        prompt = f"""
Review the following code for performance.

Filename:
{filename}

Code:

{code}

Analyze:

- Slow algorithms
- Duplicate work
- Memory usage
- CPU usage
- Database queries
- API calls
- Optimization suggestions

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # -----------------------------------------------------
    # Best Practices
    # -----------------------------------------------------

    def best_practices(
        self,
        provider,
        model,
        filename,
        code,
    ):

        prompt = f"""
Review coding standards.

Filename:
{filename}

Code:

{code}

Evaluate:

- Naming
- Readability
- PEP8 / Language Standards
- Documentation
- Exception Handling
- Logging
- Modularity

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )