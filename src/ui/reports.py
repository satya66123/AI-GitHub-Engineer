import json
import streamlit as st

from src.api.github_api import GitHubAPI

from src.ai.provider import AIProvider
from src.ai.models import AIModels

from src.ai.health_report import HealthReport
from src.ai.repository_analyzer import RepositoryAnalyzer
from src.ai.security import SecurityAnalyzer
from src.ai.refactor import RefactorEngine


def show_reports():

    st.title("📊 AI Reports")

    github = GitHubAPI()

    repository_ai = RepositoryAnalyzer()
    health = HealthReport()
    security = SecurityAnalyzer()
    refactor = RefactorEngine()

    user = github.get_authenticated_user()

    if user is None:
        st.error("Unable to connect to GitHub.")
        return

    repositories = github.get_repositories()

    if len(repositories) == 0:
        st.warning("No repositories found.")
        return

    left, right = st.columns(2)

    with left:

        provider = st.selectbox(
            "AI Provider",
            AIModels.providers(),
        )

    with right:

        model = st.selectbox(
            "Model",
            AIModels.models(provider),
        )

    repository_name = st.selectbox(
        "Repository",
        [repo["name"] for repo in repositories],
    )

    repository = next(
        repo
        for repo in repositories
        if repo["name"] == repository_name
    )

    report_type = st.selectbox(
        "Report",
        [
            "Repository Health Report",
            "Repository Summary",
            "Architecture Report",
            "Security Report",
            "Improvement Report",
        ],
    )

    if st.button(
        "Generate Report",
        type="primary",
        use_container_width=True,
    ):

        repository_information = json.dumps(
            repository,
            indent=2,
        )

        with st.spinner("Generating report..."):

            if report_type == "Repository Health Report":

                result = health.analyze(
                    provider,
                    model,
                    repository_name,
                    repository_information,
                )

            elif report_type == "Repository Summary":

                result = repository_ai.summarize(
                    provider,
                    model,
                    repository_name,
                    repository_information,
                )

            elif report_type == "Architecture Report":

                result = repository_ai.architecture(
                    provider,
                    model,
                    repository_name,
                    repository_information,
                )

            elif report_type == "Security Report":

                result = security.analyze_repository(
                    provider,
                    model,
                    repository_information,
                )

            else:

                result = refactor.improve_project(
                    provider,
                    model,
                    repository_information,
                )

        st.divider()

        st.markdown(result)

        st.download_button(
            "Download Markdown",
            result,
            file_name="repository_report.md",
            mime="text/markdown",
            use_container_width=True,
        )

        st.download_button(
            "Download TXT",
            result,
            file_name="repository_report.txt",
            mime="text/plain",
            use_container_width=True,
        )