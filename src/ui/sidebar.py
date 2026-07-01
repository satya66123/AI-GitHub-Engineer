import streamlit as st


def show_sidebar(user=None):
    """
    Displays the application sidebar.
    """

    with st.sidebar:

        st.title("🤖 AI GitHub Engineer")

        st.caption("Version 1.0")

        st.divider()

        page = st.radio(
            "Navigation",
            [
                "🏠 Dashboard",
                "📂 Repository Explorer",
                "⚙️ Settings",
                "📄 Logs",
                "ℹ️ About",
            ],
        )

        st.divider()

        if user:

            st.subheader("GitHub User")

            st.write(f"**Username:** {user['login']}")

            st.write(f"**Followers:** {user['followers']}")

            st.write(f"**Following:** {user['following']}")

            st.write(f"**Public Repos:** {user['public_repos']}")

        st.divider()

        st.caption("AI GitHub Engineer")
        st.caption("Built with ❤️ using Streamlit & GitHub API")

    return page