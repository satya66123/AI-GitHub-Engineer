import json
import streamlit as st

from src.api.github_api import GitHubAPI
from src.ai.models import AIModels
from src.ai.repository_scorer import RepositoryScorer


def show_repository_score():

    st.title("📊 AI Repository Score")

    github = GitHubAPI()

    scorer = RepositoryScorer()

    user = github.get_authenticated_user()

    if user is None:

        st.error("Unable to connect to GitHub.")

        return

    repositories = github.get_repositories()

    if len(repositories) == 0:

        st.warning("No repositories found.")

        return

    col1, col2 = st.columns(2)

    with col1:

        provider = st.selectbox(
            "AI Provider",
            AIModels.providers(),
            key="score_provider",
        )

    with col2:

        model = st.selectbox(
            "Model",
            AIModels.models(provider),
            key="score_model",
        )

    repository_name = st.selectbox(
        "Repository",
        [repo["name"] for repo in repositories],
        key="score_repository",
    )

    repository = next(
        repo
        for repo in repositories
        if repo["name"] == repository_name
    )

    report = st.selectbox(
        "Report Type",
        [
            "Overall Repository Score",
            "Architecture Score",
            "Code Quality",
            "Security Score",
            "Documentation Score",
            "Testing Score",
            "Production Readiness",
            "Improvement Plan",
        ],
    )

    if st.button(
        "🚀 Generate Score",
        type="primary",
        use_container_width=True,
    ):

        repository_information = json.dumps(
            repository,
            indent=2,
        )

        with st.spinner(
            "Analyzing repository..."
        ):

            if report == "Overall Repository Score":

                result = scorer.score_repository(
                    provider,
                    model,
                    repository_name,
                    repository_information,
                )

            elif report == "Architecture Score":

                result = scorer.architecture_score(
                    provider,
                    model,
                    repository_information,
                )

            elif report == "Code Quality":

                result = scorer.code_quality(
                    provider,
                    model,
                    repository_information,
                )

            elif report == "Security Score":

                result = scorer.security_score(
                    provider,
                    model,
                    repository_information,
                )

            elif report == "Documentation Score":

                result = scorer.documentation_score(
                    provider,
                    model,
                    repository_information,
                )

            elif report == "Testing Score":

                result = scorer.testing_score(
                    provider,
                    model,
                    repository_information,
                )

            elif report == "Production Readiness":

                result = scorer.production_readiness(
                    provider,
                    model,
                    repository_information,
                )

            else:

                result = scorer.improvement_plan(
                    provider,
                    model,
                    repository_information,
                )

        st.divider()

        st.subheader("AI Repository Report")

        st.markdown(result)

        st.download_button(
            "⬇ Download Report",
            result,
            file_name="repository_score.md",
            mime="text/markdown",
            use_container_width=True,
        )

        with st.expander(
            "Repository Metadata"
        ):

            st.json(repository)