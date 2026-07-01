import json
import streamlit as st

from src.api.github_api import GitHubAPI
from src.ai.models import AIModels
from src.ai.commit_analyzer import CommitAnalyzer


def show_commit_analysis():

    st.title("📝 AI Commit Analysis")

    github = GitHubAPI()

    analyzer = CommitAnalyzer()

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
            key="commit_provider",
        )

    with col2:

        model = st.selectbox(
            "Model",
            AIModels.models(provider),
            key="commit_model",
        )

    repository = st.selectbox(
        "Repository",
        [repo["name"] for repo in repositories],
        key="commit_repository",
    )

    owner = user["login"]

    commits = github.get_commits(
        owner,
        repository,
        per_page=30,
    )

    if len(commits) == 0:

        st.info("No commits found.")

        return

    commit_titles = []

    for commit in commits:

        sha = commit["sha"][:7]

        message = commit["commit"]["message"]

        commit_titles.append(
            f"{sha} - {message}"
        )

    selected = st.selectbox(
        "Commit",
        commit_titles,
    )

    index = commit_titles.index(selected)

    commit = commits[index]

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Author",
            commit["commit"]["author"]["name"],
        )

    with col2:

        st.metric(
            "Date",
            commit["commit"]["author"]["date"][:10],
        )

    st.subheader("Commit Message")

    st.info(
        commit["commit"]["message"]
    )

    action = st.selectbox(
        "Analysis Type",
        [
            "Commit Analysis",
            "Quality Report",
            "Changelog",
            "Release Notes",
            "Generate Commit Message",
        ],
    )

    if st.button(
        "🚀 Analyze Commit",
        type="primary",
        use_container_width=True,
    ):

        commit_json = json.dumps(
            commit,
            indent=2,
        )

        with st.spinner(
            "Analyzing commit..."
        ):

            if action == "Commit Analysis":

                result = analyzer.analyze_commit(
                    provider,
                    model,
                    repository,
                    commit_json,
                )

            elif action == "Quality Report":

                result = analyzer.quality_report(
                    provider,
                    model,
                    commit_json,
                )

            elif action == "Changelog":

                result = analyzer.changelog(
                    provider,
                    model,
                    commit_json,
                )

            elif action == "Release Notes":

                result = analyzer.release_notes(
                    provider,
                    model,
                    commit_json,
                )

            else:

                result = analyzer.generate_commit_message(
                    provider,
                    model,
                    commit_json,
                )

        st.divider()

        st.subheader("AI Result")

        st.markdown(result)

        st.download_button(
            "⬇ Download Report",
            result,
            file_name="commit_analysis.md",
            mime="text/markdown",
            use_container_width=True,
        )

        with st.expander(
            "View Raw Commit JSON"
        ):

            st.code(
                commit_json,
                language="json",
            )