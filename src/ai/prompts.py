class RepositoryPrompts:

    @staticmethod
    def repository_summary(repository_name, repository_data):

        return f"""
You are an expert Senior Software Engineer.

Analyze the following GitHub repository.

Repository:
{repository_name}

Repository Information:
{repository_data}

Generate a professional report.

Include:

1. Project Overview

2. Purpose

3. Main Features

4. Technology Stack

5. Folder Structure

6. Design Pattern

7. Strengths

8. Weaknesses

9. Possible Improvements

10. Overall Summary

Write in clean markdown.
"""

    @staticmethod
    def architecture(repository_name, repository_data):

        return f"""
You are an expert Software Architect.

Analyze the architecture of this GitHub repository.

Repository:
{repository_name}

Repository Information:
{repository_data}

Explain:

- Project architecture
- Layers
- Components
- Folder responsibilities
- Flow of execution
- Design principles
- Suggested improvements

Write in markdown.
"""

    @staticmethod
    def dependency_analysis(repository_name, dependencies):

        return f"""
You are a Python dependency expert.

Repository:
{repository_name}

Dependencies:

{dependencies}

Explain:

- Purpose of every dependency
- Whether it is necessary
- Possible alternatives
- Security concerns
- Missing useful libraries

Write in markdown.
"""

    @staticmethod
    def readme_analysis(repository_name, readme):

        return f"""
Analyze this GitHub README.

Repository:

{repository_name}

README

{readme}

Generate:

1. Summary

2. Features

3. Installation

4. Missing documentation

5. Suggested improvements

Write professionally.
"""

    @staticmethod
    def explain_code(file_name, code):

        return f"""
You are an expert Python Software Engineer.

Explain the following source code.

Filename:

{file_name}

Code:

{code}

Explain:

- Purpose
- Classes
- Functions
- Flow
- Logic
- Improvements

Write professionally.
"""

    @staticmethod
    def bug_analysis(file_name, code):

        return f"""
Analyze the following code.

Filename:

{file_name}

Code:

{code}

Find:

- Bugs
- Logical errors
- Security issues
- Performance problems
- Code smells

Suggest fixes.

Return markdown.
"""

    @staticmethod
    def refactor(file_name, code):

        return f"""
Refactor the following code.

Filename:

{file_name}

Code:

{code}

Improve:

- Readability

- Maintainability

- Performance

- Naming

- Documentation

Return improved code first.

Then explain improvements.
"""

    @staticmethod
    def documentation(file_name, code):

        return f"""
Generate professional documentation.

Filename:

{file_name}

Code:

{code}

Include:

Overview

Functions

Parameters

Returns

Example

Markdown format.
"""

    @staticmethod
    def ask(repository_context, question):

        return f"""
You are an AI GitHub Engineer.

Repository Context

{repository_context}

Question

{question}

Answer only using the repository information.

If the answer is unknown,
say you cannot determine it from the repository.
"""