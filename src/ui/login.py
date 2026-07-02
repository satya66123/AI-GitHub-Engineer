import streamlit as st
from src.api.github_api import GitHubAPI

def show_login():

    st.title("🔐 AI GitHub Engineer")

    st.write("Enter your GitHub Personal Access Token")

    token = st.text_input(
        "GitHub Token",
        type="password"
    )

    if st.button("Login"):


        if not token:
            st.error("Please enter your GitHub token.")
            return False

        api = GitHubAPI(token)

        user = api.get_authenticated_user()

        if user:

            st.session_state.github_token = token
            st.session_state.user = user
            st.session_state.logged_in = True

            st.success("Login Successful!")

            st.rerun()

        else:

            st.error("Invalid GitHub Token")

    return False