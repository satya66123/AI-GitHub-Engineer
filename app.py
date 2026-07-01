import streamlit as st

from src.api.github_api import GitHubAPI
from src.ui.sidebar import show_sidebar
from src.ui.dashboard import show_dashboard
from src.ui.repository import show_repository

st.set_page_config(
    page_title="AI GitHub Engineer",
    page_icon="🤖",
    layout="wide",
)

github = GitHubAPI()
user = github.get_authenticated_user()

page = show_sidebar(user)

if page == "🏠 Dashboard":
    show_dashboard()

elif page == "📂 Repository Explorer":
    show_repository()

elif page == "⚙️ Settings":

    st.title("⚙️ Settings")

    st.info("Settings page will be implemented in Phase 3.")

elif page == "📄 Logs":

    st.title("📄 Logs")

    st.info("Log viewer will be implemented in Phase 3.")

elif page == "ℹ️ About":

    st.title("ℹ️ About")

    st.markdown("""
# AI GitHub Engineer

Version **1.0**

An AI-powered GitHub engineering platform built with:

- 🐍 Python
- 🎈 Streamlit
- 🐙 GitHub REST API
- 🤖 Ollama (coming soon)
- 🧠 OpenAI (optional)
- ⚡ MCP-ready architecture

### Current Phase

✅ Phase 1 - GitHub API Foundation

✅ Phase 2 - Repository Explorer Dashboard

Upcoming:

- AI Repository Analysis
- Code Review
- AI Chat
- GitHub Automation
- AI Coding Agent
""")