import json
import streamlit as st

from src.api.github_api import GitHubAPI
from src.ai.models import AIModels
from src.ai.repository_chat import RepositoryChat


def show_repository_chat():

    st.title("💬 AI Repository Chat")

    github = GitHubAPI()

    chat = RepositoryChat()

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
            key="repo_chat_provider",
        )

    with col2:

        model = st.selectbox(
            "Model",
            AIModels.models(provider),
            key="repo_chat_model",
        )

    repository_name = st.selectbox(
        "Repository",
        [repo["name"] for repo in repositories],
        key="repo_chat_repository",
    )

    repository = next(
        repo
        for repo in repositories
        if repo["name"] == repository_name
    )

    repository_context = json.dumps(
        repository,
        indent=2,
    )

    mode = st.selectbox(
        "Conversation Mode",
        [
            "Ask Anything",
            "Architecture",
            "Authentication",
            "API Endpoints",
            "Database",
            "Dependencies",
            "Improvement Suggestions",
            "Executive Summary",
        ],
    )

    question = st.text_area(
        "Question",
        height=150,
        placeholder="Example: Explain the authentication flow or summarize this repository...",
    )

    if st.button(
        "🤖 Ask AI",
        type="primary",
        use_container_width=True,
    ):

        with st.spinner(
            "Analyzing repository..."
        ):

            if mode == "Ask Anything":

                result = chat.ask(
                    provider,
                    model,
                    repository_name,
                    repository_context,
                    question,
                )

            elif mode == "Architecture":

                result = chat.explain_architecture(
                    provider,
                    model,
                    repository_name,
                    repository_context,
                )

            elif mode == "Authentication":

                result = chat.authentication_flow(
                    provider,
                    model,
                    repository_context,
                )

            elif mode == "API Endpoints":

                result = chat.api_endpoints(
                    provider,
                    model,
                    repository_context,
                )

            elif mode == "Database":

                result = chat.database_analysis(
                    provider,
                    model,
                    repository_context,
                )

            elif mode == "Dependencies":

                result = chat.dependency_explanation(
                    provider,
                    model,
                    repository_context,
                )

            elif mode == "Improvement Suggestions":

                result = chat.improvement_suggestions(
                    provider,
                    model,
                    repository_name,
                    repository_context,
                )

            else:

                result = chat.repository_summary(
                    provider,
                    model,
                    repository_name,
                    repository_context,
                )

        st.divider()

        st.subheader("AI Response")

        st.markdown(result)

        st.download_button(
            "⬇ Download Response",
            result,
            file_name="repository_chat.md",
            mime="text/markdown",
            use_container_width=True,
        )

        with st.expander(
            "Repository Metadata"
        ):

            st.json(repository)