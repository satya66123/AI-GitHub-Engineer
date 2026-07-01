import json
import streamlit as st

from src.api.github_api import GitHubAPI
from src.ai.models import AIModels
from src.ai.pull_request_reviewer import PullRequestReviewer


def show_pull_request_review():

    st.title("🔀 AI Pull Request Review")

    github = GitHubAPI()

    reviewer = PullRequestReviewer()

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
            key="pr_provider",
        )

    with col2:

        model = st.selectbox(
            "Model",
            AIModels.models(provider),
            key="pr_model",
        )

    repository = st.selectbox(
        "Repository",
        [repo["name"] for repo in repositories],
        key="pr_repository",
    )

    owner = user["login"]

    pull_requests = github.get_pull_requests(
        owner,
        repository,
        state="open",
    )

    if len(pull_requests) == 0:

        st.info("No open pull requests found.")

        return

    pr_titles = [
        f"#{pr['number']} - {pr['title']}"
        for pr in pull_requests
    ]

    selected = st.selectbox(
        "Pull Request",
        pr_titles,
    )

    index = pr_titles.index(selected)

    pull_request = pull_requests[index]

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "State",
            pull_request["state"],
        )

    with col2:

        st.metric(
            "Author",
            pull_request["user"]["login"],
        )

    with col3:

        st.metric(
            "Comments",
            pull_request["comments"],
        )

    st.markdown("### Pull Request Description")

    st.write(
        pull_request.get(
            "body",
            "No description provided.",
        )
    )

    if st.button(
        "🤖 Review Pull Request",
        type="primary",
        use_container_width=True,
    ):

        pr_information = json.dumps(
            pull_request,
            indent=2,
        )

        with st.spinner(
            "Reviewing Pull Request..."
        ):

            result = reviewer.review(
                provider,
                model,
                repository,
                pr_information,
            )

        st.divider()

        st.subheader("AI Pull Request Review")

        st.markdown(result)

        st.download_button(
            "⬇ Download Review",
            result,
            file_name="pull_request_review.md",
            mime="text/markdown",
            use_container_width=True,
        )

        st.code(
            pr_information,
            language="json",
        )