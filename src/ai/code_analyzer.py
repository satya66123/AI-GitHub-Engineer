from src.ai.provider import AIProvider
from src.ai.ollama_client import OllamaClient
from src.ai.openai_client import OpenAIClient


class CodeAnalyzer:

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
    # Explain Code
    # -----------------------------------------------------

    def explain_code(
        self,
        provider,
        model,
        filename,
        code,
    ):

        prompt = f"""
You are an Expert Software Engineer.

Explain the following source code.

Filename:
{filename}

Code:

{code}

Explain:

1. Purpose
2. Classes
3. Functions
4. Business Logic
5. Execution Flow
6. Best Practices
7. Possible Improvements

Return the response in Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # -----------------------------------------------------
    # Review Code
    # -----------------------------------------------------

    def review_code(
        self,
        provider,
        model,
        filename,
        code,
    ):

        prompt = f"""
You are a Senior Software Engineer.

Review the following code.

Filename:
{filename}

Code:

{code}

Review:

- Code Quality
- Readability
- Maintainability
- Performance
- Security
- Bugs
- Suggestions

Return the response in Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # -----------------------------------------------------
    # Explain Function
    # -----------------------------------------------------

    def explain_function(
        self,
        provider,
        model,
        function_name,
        code,
    ):

        prompt = f"""
Explain the following function.

Function:
{function_name}

Code:

{code}

Include:

- Purpose
- Parameters
- Return Value
- Logic
- Time Complexity
- Space Complexity
- Example Usage

Return the response in Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # -----------------------------------------------------
    # Complexity Analysis
    # -----------------------------------------------------

    def complexity_analysis(
        self,
        provider,
        model,
        filename,
        code,
    ):

        prompt = f"""
Analyze the following source code.

Filename:
{filename}

Code:

{code}

Explain:

- Time Complexity
- Space Complexity
- Performance Bottlenecks
- Optimization Suggestions

Return the response in Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # -----------------------------------------------------
    # Multi File Project Analysis
    # -----------------------------------------------------

    def analyze_project(
        self,
        provider,
        model,
        project_name,
        files,
    ):

        prompt = f"""
Analyze the following software project.

Project:
{project_name}

Files:

{files}

Generate a report containing:

1. Project Summary
2. Architecture
3. Folder Structure
4. File Relationships
5. Code Quality
6. Strengths
7. Weaknesses
8. Recommendations
9. Best Practices
10. Overall Rating

Return the response in Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )