import streamlit as st

from src.api.github_api import GitHubAPI


def show_home():

    st.title("🤖 AI GitHub Engineer")

    st.caption("Phase 1 - GitHub API Connection")

    github = GitHubAPI()

    user = github.get_authenticated_user()

    if user is None:
        st.error("❌ Unable to connect to GitHub.")
        return

    st.success("✅ Connected to GitHub")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Username", user["login"])

    with col2:
        st.metric("Public Repositories", user["public_repos"])

    with col3:
        st.metric("Followers", user["followers"])

    st.divider()

    st.subheader("Repository List")

    repos = github.get_repositories()

    if not repos:
        st.info("No repositories found.")
        return

    for repo in repos:

        with st.container(border=True):

            st.markdown(f"### {repo['name']}")

            st.write(repo["description"] or "No description")

            c1, c2, c3 = st.columns(3)

            c1.write(f"⭐ Stars : {repo['stargazers_count']}")

            c2.write(f"🍴 Forks : {repo['forks_count']}")

            c3.write(f"🌐 {repo['language']}")