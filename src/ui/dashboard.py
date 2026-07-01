import streamlit as st

from src.api.github_api import GitHubAPI
from src.utils.helper import RepositoryHelper


def show_dashboard():

    github = GitHubAPI()

    user = github.get_authenticated_user()

    if user is None:
        st.error("Unable to connect to GitHub.")
        return

    repos = github.get_repositories()

    helper = RepositoryHelper()

    # ---------------------------------------------------
    # Header
    # ---------------------------------------------------

    st.title("🏠 GitHub Dashboard")

    st.write(
        f"Welcome **{user['login']}** 👋"
    )

    st.divider()

    # ---------------------------------------------------
    # Statistics
    # ---------------------------------------------------

    stats = helper.calculate_statistics(repos)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Repositories",
        stats["repositories"]
    )

    col2.metric(
        "Followers",
        user["followers"]
    )

    col3.metric(
        "Following",
        user["following"]
    )

    col4.metric(
        "Stars",
        stats["stars"]
    )

    st.divider()

    # ---------------------------------------------------
    # Search / Filter
    # ---------------------------------------------------

    left, middle, right = st.columns([2, 2, 2])

    search = left.text_input(
        "🔍 Search Repository"
    )

    languages = github.get_languages(repos)

    language = middle.selectbox(
        "Language",
        languages
    )

    sort = right.selectbox(
        "Sort By",
        [
            "Recently Updated",
            "Name",
            "Stars",
            "Forks",
            "Created Date",
        ],
    )

    repos = helper.search_repositories(
        repos,
        search,
    )

    repos = helper.filter_by_language(
        repos,
        language,
    )

    repos = helper.sort_repositories(
        repos,
        sort,
    )

    st.success(
        f"{len(repos)} repositories found."
    )

    st.divider()

    # ---------------------------------------------------
    # Repository Cards
    # ---------------------------------------------------

    if len(repos) == 0:

        st.warning(
            "No repositories found."
        )

        return

    for repo in repos:

        with st.container(border=True):

            c1, c2 = st.columns([4, 1])

            with c1:

                st.subheader(repo["name"])

                st.write(
                    repo["description"]
                    or "No description available."
                )

            with c2:

                if repo["private"]:
                    st.error("Private")
                else:
                    st.success("Public")

            info1, info2, info3 = st.columns(3)

            info1.write(
                f"⭐ Stars : {repo['stargazers_count']}"
            )

            info2.write(
                f"🍴 Forks : {repo['forks_count']}"
            )

            info3.write(
                f"💻 {repo['language']}"
            )

            info4, info5 = st.columns(2)

            info4.write(
                f"📅 Updated : {helper.format_date(repo['updated_at'])}"
            )

            info5.write(
                f"🌿 Default Branch : {repo['default_branch']}"
            )

            st.link_button(
                "Open Repository",
                repo["html_url"],
                use_container_width=True,
            )

    st.divider()

    # ---------------------------------------------------
    # Languages
    # ---------------------------------------------------

    st.subheader("📈 Languages Used")

    languages = helper.top_languages(repos)

    if len(languages) == 0:

        st.info("No language data.")

        return

    for language, count in languages:

        st.progress(
            count / len(repos),
            text=f"{language} ({count})",
        )