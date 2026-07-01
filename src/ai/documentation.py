from src.ai.provider import AIProvider
from src.ai.ollama_client import OllamaClient
from src.ai.openai_client import OpenAIClient


class DocumentationGenerator:

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
    # File Documentation
    # -----------------------------------------------------

    def generate_file_documentation(
        self,
        provider,
        model,
        filename,
        code,
    ):

        prompt = f"""
You are a Senior Software Engineer and Technical Writer.

Generate professional documentation for the following source code.

Filename:
{filename}

Source Code:

{code}

Generate documentation with the following sections:

# Overview

# Purpose

# Classes

# Functions

# Parameters

# Return Values

# Dependencies

# Execution Flow

# Example Usage

# Notes

Return the response in Markdown format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # -----------------------------------------------------
    # Function Documentation
    # -----------------------------------------------------

    def generate_function_documentation(
        self,
        provider,
        model,
        function_name,
        code,
    ):

        prompt = f"""
Document the following function.

Function:
{function_name}

Code:

{code}

Include:

- Purpose
- Parameters
- Return Value
- Raises Exceptions
- Example
- Best Practices

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # -----------------------------------------------------
    # Class Documentation
    # -----------------------------------------------------

    def generate_class_documentation(
        self,
        provider,
        model,
        class_name,
        code,
    ):

        prompt = f"""
Document the following class.

Class:
{class_name}

Code:

{code}

Generate:

# Class Overview

# Responsibilities

# Attributes

# Methods

# Relationships

# Example Usage

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # -----------------------------------------------------
    # README Generator
    # -----------------------------------------------------

    def generate_readme(
        self,
        provider,
        model,
        project_name,
        project_description,
        technologies,
    ):

        prompt = f"""
Generate a professional GitHub README.

Project Name:
{project_name}

Description:
{project_description}

Technologies:
{technologies}

Include:

# Title

# Description

# Features

# Tech Stack

# Installation

# Usage

# Folder Structure

# Screenshots Placeholder

# Future Improvements

# License

Return complete README.md in Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # -----------------------------------------------------
    # API Documentation
    # -----------------------------------------------------

    def generate_api_documentation(
        self,
        provider,
        model,
        api_code,
    ):

        prompt = f"""
Generate API documentation.

API Source:

{api_code}

Include:

- Endpoint
- HTTP Method
- Parameters
- Request Example
- Response Example
- Status Codes
- Error Responses

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # -----------------------------------------------------
    # Project Documentation
    # -----------------------------------------------------

    def generate_project_documentation(
        self,
        provider,
        model,
        project_name,
        repository_information,
    ):

        prompt = f"""
Generate professional software project documentation.

Project:
{project_name}

Repository Information:

{repository_information}

Generate:

# Executive Summary

# Architecture

# Modules

# Folder Structure

# Technologies

# Design Pattern

# Installation

# Configuration

# Usage

# Deployment

# Security

# Improvements

# Conclusion

Return Markdown.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )