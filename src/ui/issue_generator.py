import streamlit as st

from src.api.github_api import GitHubAPI
from src.ai.models import AIModels
from src.ai.issue_generator import IssueGenerator


def show_issue_generator():

    st.title("🐞 AI Issue Generator")

    github = GitHubAPI()

    generator = IssueGenerator()

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
            key="issue_provider",
        )

    with col2:

        model = st.selectbox(
            "Model",
            AIModels.models(provider),
            key="issue_model",
        )

    repository = st.selectbox(
        "Repository",
        [repo["name"] for repo in repositories],
        key="issue_repository",
    )

    issue_type = st.selectbox(
        "Issue Type",
        [
            "Bug Report",
            "Feature Request",
            "Enhancement",
            "Documentation",
            "Security",
            "Performance",
            "Refactoring",
            "Testing",
        ],
    )

    description = st.text_area(
        "Description",
        height=220,
        placeholder="Describe the issue or requirement...",
    )

    if st.button(
        "🚀 Generate Issue",
        type="primary",
        use_container_width=True,
    ):

        if not description.strip():

            st.warning(
                "Please enter a description."
            )

            return

        with st.spinner(
            "Generating GitHub issue..."
        ):

            if issue_type == "Bug Report":

                result = generator.bug_report(
                    provider,
                    model,
                    repository,
                    description,
                )

            elif issue_type == "Feature Request":

                result = generator.feature_request(
                    provider,
                    model,
                    repository,
                    description,
                )

            elif issue_type == "Enhancement":

                result = generator.enhancement(
                    provider,
                    model,
                    repository,
                    description,
                )

            elif issue_type == "Documentation":

                result = generator.documentation_issue(
                    provider,
                    model,
                    repository,
                    description,
                )

            elif issue_type == "Security":

                result = generator.security_issue(
                    provider,
                    model,
                    repository,
                    description,
                )

            elif issue_type == "Performance":

                result = generator.performance_issue(
                    provider,
                    model,
                    repository,
                    description,
                )

            elif issue_type == "Refactoring":

                result = generator.refactoring_task(
                    provider,
                    model,
                    repository,
                    description,
                )

            else:

                result = generator.testing_task(
                    provider,
                    model,
                    repository,
                    description,
                )

        st.divider()

        st.subheader("Generated GitHub Issue")

        st.markdown(result)

        st.download_button(
            "⬇ Download Markdown",
            result,
            file_name="github_issue.md",
            mime="text/markdown",
            use_container_width=True,
        )

        st.download_button(
            "⬇ Download Text",
            result,
            file_name="github_issue.txt",
            mime="text/plain",
            use_container_width=True,
        )

        st.code(
            result,
            language="markdown",
        )