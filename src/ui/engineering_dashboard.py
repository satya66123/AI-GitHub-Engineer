import streamlit as st

from src.api.github_api import GitHubAPI

from src.ai.models import AIModels
from src.ai.github_engineer import GitHubEngineer


def show_engineering_dashboard():

    st.title("👨‍💻 AI GitHub Engineer")

    github = GitHubAPI()

    engineer = GitHubEngineer()

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
            key="eng_provider",
        )

    with col2:

        model = st.selectbox(
            "Model",
            AIModels.models(provider),
            key="eng_model",
        )

    repository = st.selectbox(
        "Repository",
        [repo["name"] for repo in repositories],
        key="eng_repo",
    )

    action = st.selectbox(
        "Engineering Task",
        [
            "Repository Review",
            "Repository Chat",
            "Pull Request Review",
            "Commit Analysis",
            "Issue Generator",
            "Test Generator",
            "Release Notes",
            "Workflow Review",
            "Docker Review",
            "License Review",
            "Code Quality",
            "Project Generator",
        ],
    )

    st.divider()

    user_input = st.text_area(
        "Input",
        height=250,
        placeholder="Paste commit, pull request, Dockerfile, workflow, source code or describe your request...",
    )

    if st.button(
        "🚀 Execute",
        use_container_width=True,
        type="primary",
    ):

        if not user_input.strip():

            st.warning("Please provide input.")

            return

        with st.spinner("AI Engineer is working..."):

            if action == "Repository Review":

                result = engineer.review_repository(
                    provider,
                    model,
                    repository,
                    user_input,
                )

            elif action == "Repository Chat":

                result = engineer.chat(
                    provider,
                    model,
                    repository,
                    user_input,
                    "Explain this repository.",
                )

            elif action == "Pull Request Review":

                result = engineer.review_pull_request(
                    provider,
                    model,
                    repository,
                    user_input,
                )

            elif action == "Commit Analysis":

                result = engineer.analyze_commit(
                    provider,
                    model,
                    repository,
                    user_input,
                )

            elif action == "Issue Generator":

                result = engineer.create_issue(
                    provider,
                    model,
                    repository,
                    user_input,
                )

            elif action == "Test Generator":

                result = engineer.generate_tests(
                    provider,
                    model,
                    "source.py",
                    user_input,
                )

            elif action == "Release Notes":

                result = engineer.generate_release_notes(
                    provider,
                    model,
                    repository,
                    user_input,
                )

            elif action == "Workflow Review":

                result = engineer.analyze_workflow(
                    provider,
                    model,
                    repository,
                    user_input,
                )

            elif action == "Docker Review":

                result = engineer.analyze_docker(
                    provider,
                    model,
                    repository,
                    user_input,
                )

            elif action == "License Review":

                result = engineer.analyze_license(
                    provider,
                    model,
                    repository,
                    user_input,
                )

            elif action == "Code Quality":

                result = engineer.analyze_code_quality(
                    provider,
                    model,
                    "source.py",
                    user_input,
                )

            else:

                result = engineer.generate_project(
                    provider,
                    model,
                    repository,
                    user_input,
                )

        st.divider()

        st.subheader("AI Result")

        st.markdown(result)

        st.download_button(
            "⬇ Download Markdown",
            result,
            file_name="engineering_result.md",
            mime="text/markdown",
            use_container_width=True,
        )