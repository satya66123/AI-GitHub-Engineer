from src.ai.provider import AIProvider
from src.ai.ollama_client import OllamaClient
from src.ai.openai_client import OpenAIClient

from src.ai.engineering_assistant import EngineeringAssistant
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


class GitHubEngineer:

    def __init__(self):

        self.ollama = OllamaClient()
        self.openai = OpenAIClient()

        self.assistant = EngineeringAssistant()

        self.pull_request_reviewer = PullRequestReviewer()
        self.commit_analyzer = CommitAnalyzer()
        self.issue_generator = IssueGenerator()
        self.test_generator = TestGenerator()
        self.changelog_generator = ChangelogGenerator()
        self.repository_scorer = RepositoryScorer()
        self.workflow_analyzer = WorkflowAnalyzer()
        self.docker_analyzer = DockerAnalyzer()
        self.license_analyzer = LicenseAnalyzer()
        self.code_quality_analyzer = CodeQualityAnalyzer()
        self.repository_chat = RepositoryChat()
        self.project_generator = ProjectGenerator()

    # ----------------------------------------------------
    # Provider
    # ----------------------------------------------------

    def generate(
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
    # Universal Engineering Request
    # ----------------------------------------------------

    def execute(
        self,
        provider,
        model,
        repository,
        context,
        request,
    ):

        return self.assistant.assistant(
            provider,
            model,
            repository,
            context,
            request,
        )

    # ----------------------------------------------------
    # Repository Review
    # ----------------------------------------------------

    def review_repository(
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
    # Repository Chat
    # ----------------------------------------------------

    def chat(
        self,
        provider,
        model,
        repository,
        repository_context,
        question,
    ):

        return self.repository_chat.ask(
            provider,
            model,
            repository,
            repository_context,
            question,
        )

    # ----------------------------------------------------
    # Pull Request Review
    # ----------------------------------------------------

    def review_pull_request(
        self,
        provider,
        model,
        repository,
        pull_request,
    ):

        return self.pull_request_reviewer.review(
            provider,
            model,
            repository,
            pull_request,
        )

    # ----------------------------------------------------
    # Commit Analysis
    # ----------------------------------------------------

    def analyze_commit(
        self,
        provider,
        model,
        repository,
        commit,
    ):

        return self.commit_analyzer.analyze_commit(
            provider,
            model,
            repository,
            commit,
        )

    # ----------------------------------------------------
    # Generate Issue
    # ----------------------------------------------------

    def create_issue(
        self,
        provider,
        model,
        repository,
        description,
    ):

        return self.issue_generator.feature_request(
            provider,
            model,
            repository,
            description,
        )

    # ----------------------------------------------------
    # Generate Tests
    # ----------------------------------------------------

    def generate_tests(
        self,
        provider,
        model,
        filename,
        code,
    ):

        return self.test_generator.pytest(
            provider,
            model,
            filename,
            code,
        )

    # ----------------------------------------------------
    # Generate Release Notes
    # ----------------------------------------------------

    def generate_release_notes(
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

    # ----------------------------------------------------
    # Analyze Workflow
    # ----------------------------------------------------

    def analyze_workflow(
        self,
        provider,
        model,
        repository,
        workflow,
    ):

        return self.workflow_analyzer.analyze_workflow(
            provider,
            model,
            repository,
            workflow,
        )

    # ----------------------------------------------------
    # Analyze Docker
    # ----------------------------------------------------

    def analyze_docker(
        self,
        provider,
        model,
        repository,
        dockerfile,
    ):

        return self.docker_analyzer.analyze_dockerfile(
            provider,
            model,
            repository,
            dockerfile,
        )

    # ----------------------------------------------------
    # Analyze License
    # ----------------------------------------------------

    def analyze_license(
        self,
        provider,
        model,
        repository,
        license_text,
    ):

        return self.license_analyzer.analyze_license(
            provider,
            model,
            repository,
            license_text,
        )

    # ----------------------------------------------------
    # Code Quality
    # ----------------------------------------------------

    def analyze_code_quality(
        self,
        provider,
        model,
        filename,
        code,
    ):

        return self.code_quality_analyzer.analyze(
            provider,
            model,
            filename,
            code,
        )

    # ----------------------------------------------------
    # Generate Project
    # ----------------------------------------------------

    def generate_project(
        self,
        provider,
        model,
        project_name,
        requirements,
    ):

        return self.project_generator.architecture(
            provider,
            model,
            project_name,
            requirements,
        )