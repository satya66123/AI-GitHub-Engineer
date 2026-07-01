from src.ai.provider import AIProvider
from src.ai.ollama_client import OllamaClient
from src.ai.openai_client import OpenAIClient


class ProjectGenerator:

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
    # Project Architecture
    # ----------------------------------------------------

    def architecture(
        self,
        provider,
        model,
        project_name,
        requirements,
    ):

        prompt = f"""
You are a Principal Software Architect.

Design a software architecture.

Project

{project_name}

Requirements

{requirements}

Generate

Architecture

Layers

Components

Technology Stack

Folder Structure

Data Flow

Design Patterns

Best Practices

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Folder Structure
    # ----------------------------------------------------

    def folder_structure(
        self,
        provider,
        model,
        project_name,
        requirements,
    ):

        prompt = f"""
Generate a professional folder structure.

Project

{project_name}

Requirements

{requirements}

Return a complete directory tree.

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # README Generator
    # ----------------------------------------------------

    def readme(
        self,
        provider,
        model,
        project_name,
        requirements,
    ):

        prompt = f"""
Generate a professional README.md.

Project

{project_name}

Requirements

{requirements}

Include

Overview

Features

Architecture

Installation

Usage

Configuration

Screenshots Placeholder

Future Scope

License

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Requirements Generator
    # ----------------------------------------------------

    def requirements(
        self,
        provider,
        model,
        project_description,
    ):

        prompt = f"""
Generate dependency files.

Project

{project_description}

Generate

requirements.txt

package.json

Dockerfile

docker-compose.yml

Explain why each dependency is needed.

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Configuration Files
    # ----------------------------------------------------

    def configuration(
        self,
        provider,
        model,
        project_description,
    ):

        prompt = f"""
Generate configuration files.

Project

{project_description}

Generate

.env.example

.gitignore

.editorconfig

.pre-commit-config.yaml

Explain each configuration.

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Boilerplate Code
    # ----------------------------------------------------

    def boilerplate(
        self,
        provider,
        model,
        project_name,
        requirements,
    ):

        prompt = f"""
Generate project boilerplate.

Project

{project_name}

Requirements

{requirements}

Generate

Main Entry Point

Configuration

Folder Layout

Starter Classes

Starter Functions

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Development Roadmap
    # ----------------------------------------------------

    def roadmap(
        self,
        provider,
        model,
        project_name,
        requirements,
    ):

        prompt = f"""
Create a professional development roadmap.

Project

{project_name}

Requirements

{requirements}

Generate

Phase 1

Phase 2

Phase 3

Phase 4

Milestones

Timeline

Deliverables

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )