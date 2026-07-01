from src.ai.provider import AIProvider
from src.ai.ollama_client import OllamaClient
from src.ai.openai_client import OpenAIClient

from src.ai.pull_request_reviewer import PullRequestReviewer
from src.ai.commit_analyzer import CommitAnalyzer
from src.ai.issue_generator import IssueGenerator
from src.ai.test_generator import TestGenerator
from src.ai.changelog_generator import ChangelogGenerator
from src.ai.repository_scorer import RepositoryScorer
from src.ai.workflow_analyzer import WorkflowAnalyzer
from src.ai.docker_analyzer import DockerAnalyzer
from src.ai.license_analyzer import LicenseAnalyzer
from src.ai.code_quality_analyzer import CodeQualityAnalyzer
from src.ai.repository_chat import RepositoryChat
from src.ai.project_generator import ProjectGenerator


class EngineeringAssistant:

    def __init__(self):

        self.ollama = OllamaClient()
        self.openai = OpenAIClient()

        self.pr_reviewer = PullRequestReviewer()
        self.commit_analyzer = CommitAnalyzer()
        self.issue_generator = IssueGenerator()
        self.test_generator = TestGenerator()
        self.changelog_generator = ChangelogGenerator()
        self.repository_scorer = RepositoryScorer()
        self.workflow_analyzer = WorkflowAnalyzer()
        self.docker_analyzer = DockerAnalyzer()
        self.license_analyzer = LicenseAnalyzer()
        self.code_quality = CodeQualityAnalyzer()
        self.repository_chat = RepositoryChat()
        self.project_generator = ProjectGenerator()

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
    # Universal Engineering Assistant
    # ----------------------------------------------------

    def assistant(
        self,
        provider,
        model,
        repository,
        context,
        request,
    ):

        prompt = f"""
You are an Expert AI Software Engineering Assistant.

Repository

{repository}

Repository Context

{context}

User Request

{request}

Choose the most appropriate engineering approach.

Possible Tasks

- Repository Analysis
- Code Review
- Pull Request Review
- Commit Analysis
- Bug Detection
- Security Review
- Documentation
- Refactoring
- Test Generation
- Repository Scoring
- CI/CD Review
- Docker Review
- License Review
- Architecture Review
- Project Planning

Provide a professional response.

Markdown Format.
"""

        return self._generate(
            provider,
            model,
            prompt,
        )

    # ----------------------------------------------------
    # Repository Health Check
    # ----------------------------------------------------

    def health_check(
        self,
        provider,
        model,
        repository,
        repository_information,
    ):

        return self.repository_scorer.score_repository(
            provider,
            model,
            repository,
            repository_information,
        )

    # ----------------------------------------------------
    # AI Project Planner
    # ----------------------------------------------------

    def project_planner(
        self,
        provider,
        model,
        project_name,
        requirements,
    ):

        return self.project_generator.roadmap(
            provider,
            model,
            project_name,
            requirements,
        )

    # ----------------------------------------------------
    # AI Code Reviewer
    # ----------------------------------------------------

    def code_review(
        self,
        provider,
        model,
        filename,
        code,
    ):

        return self.code_quality.analyze(
            provider,
            model,
            filename,
            code,
        )

    # ----------------------------------------------------
    # AI Repository Advisor
    # ----------------------------------------------------

    def repository_advisor(
        self,
        provider,
        model,
        repository,
        repository_context,
    ):

        return self.repository_chat.improvement_suggestions(
            provider,
            model,
            repository,
            repository_context,
        )

    # ----------------------------------------------------
    # AI Release Manager
    # ----------------------------------------------------

    def release_manager(
        self,
        provider,
        model,
        repository,
        commits,
    ):

        return self.changelog_generator.release_notes(
            provider,
            model,
            repository,
            commits,
        )