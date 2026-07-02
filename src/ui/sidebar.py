import streamlit as st


def show_sidebar(user=None):

    with st.sidebar:

        st.title("🤖 AI GitHub Engineer")

        st.caption("Version 1.0")

        st.divider()

        page = st.radio(
            "Navigation",
            [

                "🏠 Dashboard",

                "📂 Repository Explorer",

                "🤖 AI Repository Analysis",

                "💻 AI Code Analysis",

                "📊 AI Reports",

                "💬 AI Chat",

                "📝 Chat History",

                "👨‍💻 Engineering Dashboard",

                "🔀 Pull Request Review",

                "📝 Commit Analysis",

                "🐞 Issue Generator",

                "🧪 Test Generator",

                "📈 Repository Score",

                "💬 Repository Chat",

                "⚙️ Settings",

                "📄 Logs",

                "ℹ️ About",

            ],
        )

        st.divider()

        if st.button("🚪 Logout", use_container_width=True):

            keys = [
                "logged_in",
                "token",
                "user",
            ]

            for key in keys:
                st.session_state.pop(key, None)

            st.success("Logged out successfully.")

            st.rerun()

        st.divider()

        if user:

            st.subheader("GitHub Profile")

            st.write(f"👤 **{user['login']}**")

            st.write(f"📦 Public Repos : {user['public_repos']}")

            st.write(f"👥 Followers : {user['followers']}")

            st.write(f"➡ Following : {user['following']}")

            st.write(f"⭐ Public Gists : {user['public_gists']}")

        st.divider()

        st.success("GitHub Connected")

        st.caption("AI GitHub Engineer")
        st.caption("Powered by GitHub API")
        st.caption("Supports Ollama & OpenAI")

    return page