import streamlit as st

from src.api.github_api import GitHubAPI
from src.utils.helper import RepositoryHelper


def show_repository():

    github = GitHubAPI()

    user = github.get_authenticated_user()

    if user is None:
        st.error("Unable to connect to GitHub.")
        return

    repos = github.get_repositories()

    if not repos:
        st.warning("No repositories found.")
        return

    st.title("📂 Repository Explorer")

    repo_names = sorted(
        [repo["name"] for repo in repos]
    )

    selected_repo = st.selectbox(
        "Select Repository",
        repo_names,
    )

    selected = next(
        repo
        for repo in repos
        if repo["name"] == selected_repo
    )

    owner = user["login"]

    details = github.get_repository(
        owner,
        selected_repo,
    )

    if details is None:
        st.error("Unable to load repository details.")
        return

    st.divider()

    col1, col2 = st.columns([3, 1])

    with col1:

        st.subheader(details["name"])

        st.write(
            details["description"]
            or "No description available."
        )

    with col2:

        if details["private"]:
            st.error("Private")
        else:
            st.success("Public")

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "⭐ Stars",
        details["stargazers_count"],
    )

    c2.metric(
        "🍴 Forks",
        details["forks_count"],
    )

    c3.metric(
        "🐞 Issues",
        details["open_issues_count"],
    )

    c4.metric(
        "💻 Language",
        details["language"] or "N/A",
    )

    st.divider()

    st.write(
        f"**Default Branch:** {details['default_branch']}"
    )

    st.write(
        f"**Created:** {RepositoryHelper.format_date(details['created_at'])}"
    )

    st.write(
        f"**Updated:** {RepositoryHelper.format_date(details['updated_at'])}"
    )

    st.write(
        f"**Clone URL:** `{details['clone_url']}`"
    )

    st.link_button(
        "Open GitHub Repository",
        details["html_url"],
        use_container_width=True,
    )

    st.divider()

    tab1, tab2, tab3 = st.tabs(
        [
            "🌿 Branches",
            "👥 Contributors",
            "📝 Recent Commits",
        ]
    )

    with tab1:

        branches = github.get_branches(
            owner,
            selected_repo,
        )

        if not branches:
            st.info("No branches found.")
        else:
            for branch in branches:
                st.write(
                    f"🌿 {branch['name']}"
                )

    with tab2:

        contributors = github.get_contributors(
            owner,
            selected_repo,
        )

        if not contributors:
            st.info("No contributors found.")
        else:
            for contributor in contributors:
                st.write(
                    f"👤 {contributor['login']} "
                    f"({contributor['contributions']} commits)"
                )

    with tab3:

        commits = github.get_commits(
            owner,
            selected_repo,
        )

        if not commits:
            st.info("No commits found.")
        else:
            for commit in commits[:10]:

                message = commit["commit"]["message"]

                author = commit["commit"]["author"]["name"]

                date = RepositoryHelper.format_date(
                    commit["commit"]["author"]["date"]
                )

                with st.container(border=True):

                    st.write(f"**{message}**")

                    st.caption(
                        f"{author} • {date}"
                    )