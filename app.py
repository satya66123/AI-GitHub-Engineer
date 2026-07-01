# app.py

import streamlit as st

from src.api.github_api import GitHubAPI

from src.utils.session import SessionManager

# ---------------- Phase 1 ----------------

from src.ui.dashboard import show_dashboard
from src.ui.repository import show_repository

# ---------------- Phase 3 ----------------

from src.ui.ai_analysis import show_ai_analysis
from src.ui.code_analysis import show_code_analysis
from src.ui.reports import show_reports
from src.ui.ai_chat import show_ai_chat
from src.ui.chat_history import show_chat_history

# ---------------- Phase 4 ----------------

from src.ui.engineering_dashboard import (
    show_engineering_dashboard,
)

from src.ui.pull_request_review import (
    show_pull_request_review,
)

from src.ui.commit_analysis import (
    show_commit_analysis,
)

from src.ui.issue_generator import (
    show_issue_generator,
)

from src.ui.test_generator import (
    show_test_generator,
)

from src.ui.repository_score import (
    show_repository_score,
)

from src.ui.repository_chat import (
    show_repository_chat,
)

# ---------------- Common ----------------

from src.ui.settings import show_settings
from src.ui.logs import show_logs
from src.ui.about import show_about
from src.ui.sidebar import show_sidebar


# ----------------------------------------------------
# Streamlit
# ----------------------------------------------------

st.set_page_config(
    page_title="AI GitHub Engineer",
    page_icon="🤖",
    layout="wide",
)

SessionManager.initialize()

# ----------------------------------------------------
# GitHub
# ----------------------------------------------------

github = GitHubAPI()

user = github.get_authenticated_user()

if user is None:

    st.error("Unable to connect to GitHub.")

    st.stop()

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

page = show_sidebar(user)

# ----------------------------------------------------
# Routing
# ----------------------------------------------------

match page:

    # ---------------- Phase 1 ----------------

    case "🏠 Dashboard":
        show_dashboard()

    case "📂 Repository Explorer":
        show_repository()

    # ---------------- Phase 3 ----------------

    case "🤖 AI Repository Analysis":
        show_ai_analysis()

    case "💻 AI Code Analysis":
        show_code_analysis()

    case "📊 AI Reports":
        show_reports()

    case "💬 AI Chat":
        show_ai_chat()

    case "📝 Chat History":
        show_chat_history()

    # ---------------- Phase 4 ----------------

    case "👨‍💻 Engineering Dashboard":
        show_engineering_dashboard()

    case "🔀 Pull Request Review":
        show_pull_request_review()

    case "📝 Commit Analysis":
        show_commit_analysis()

    case "🐞 Issue Generator":
        show_issue_generator()

    case "🧪 Test Generator":
        show_test_generator()

    case "📈 Repository Score":
        show_repository_score()

    case "💬 Repository Chat":
        show_repository_chat()

    # ---------------- Common ----------------

    case "⚙️ Settings":
        show_settings()

    case "📄 Logs":
        show_logs()

    case "ℹ️ About":
        show_about()

    case _:
        show_dashboard()