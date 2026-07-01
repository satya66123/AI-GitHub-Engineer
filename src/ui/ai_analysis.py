import json
import streamlit as st

from src.api.github_api import GitHubAPI
from src.ai.provider import (
    AIProvider,
    get_models,
)
from src.ai.repository_analyzer import RepositoryAnalyzer


def show_ai_analysis():

    st.title("🤖 AI Repository Analysis")

    github = GitHubAPI()

    analyzer = RepositoryAnalyzer()

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
            [
                AIProvider.OLLAMA.value,
                AIProvider.OPENAI.value,
            ],
        )

    with right:

        model = st.selectbox(
            "Model",
            get_models(provider),
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

    st.divider()

    analysis = st.radio(
        "Analysis Type",
        [
            "Repository Summary",
            "Architecture",
            "Dependency Analysis",
            "README Analysis",
            "Ask AI",
        ],
        horizontal=True,
    )

    question = ""

    if analysis == "Ask AI":

        question = st.text_area(
            "Question",
            height=120,
            placeholder="How does authentication work?",
        )

    if st.button(
        "🚀 Analyze",
        use_container_width=True,
        type="primary",
    ):

        with st.spinner("Analyzing repository..."):

            repository_json = json.dumps(
                repository,
                indent=2,
            )

            if analysis == "Repository Summary":

                result = analyzer.summarize(
                    provider,
                    model,
                    repository_name,
                    repository_json,
                )

            elif analysis == "Architecture":

                result = analyzer.architecture(
                    provider,
                    model,
                    repository_name,
                    repository_json,
                )

            elif analysis == "Dependency Analysis":

                dependencies = ""

                result = analyzer.dependency_analysis(
                    provider,
                    model,
                    repository_name,
                    dependencies,
                )

            elif analysis == "README Analysis":

                readme = repository.get(
                    "description",
                    "",
                )

                result = analyzer.readme_analysis(
                    provider,
                    model,
                    repository_name,
                    readme,
                )

            else:

                result = analyzer.ask(
                    provider,
                    model,
                    repository_json,
                    question,
                )

        st.divider()

        st.subheader("AI Response")

        st.markdown(result)

        st.download_button(
            "Download Result",
            result,
            file_name="analysis.md",
            mime="text/markdown",
            use_container_width=True,
        )