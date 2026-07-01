import streamlit as st

from src.api.github_api import GitHubAPI
from src.api.repository_contents import RepositoryContents

from src.ai.provider import AIProvider
from src.ai.models import AIModels
from src.ai.code_analyzer import CodeAnalyzer
from src.ai.bug_finder import BugFinder
from src.ai.documentation import DocumentationGenerator
from src.ai.refactor import RefactorEngine
from src.ai.security import SecurityAnalyzer


def show_code_analysis():

    st.title("💻 AI Code Analysis")

    github = GitHubAPI()
    contents = RepositoryContents()

    analyzer = CodeAnalyzer()
    bug_finder = BugFinder()
    documentation = DocumentationGenerator()
    refactor = RefactorEngine()
    security = SecurityAnalyzer()

    user = github.get_authenticated_user()

    if user is None:
        st.error("Unable to connect to GitHub.")
        return

    repositories = github.get_repositories()

    if not repositories:
        st.warning("No repositories found.")
        return

    owner = user["login"]

    provider = st.selectbox(
        "AI Provider",
        AIModels.providers(),
    )

    model = st.selectbox(
        "Model",
        AIModels.models(provider),
    )

    repo_name = st.selectbox(
        "Repository",
        [repo["name"] for repo in repositories],
    )

    python_files = contents.get_python_files(
        owner,
        repo_name,
    )

    if not python_files:

        st.warning("No Python files found.")

        return

    file_path = st.selectbox(
        "Source File",
        python_files,
    )

    analysis = st.selectbox(
        "Analysis",
        [
            "Explain Code",
            "Review Code",
            "Complexity",
            "Bug Finder",
            "Security Scan",
            "Documentation",
            "Refactor",
        ],
    )

    code = contents.get_file(
        owner,
        repo_name,
        file_path,
    )

    st.subheader("Source Code")

    st.code(
        code,
        language="python",
    )

    if st.button(
        "🚀 Analyze",
        use_container_width=True,
        type="primary",
    ):

        with st.spinner("Running AI Analysis..."):

            if analysis == "Explain Code":

                result = analyzer.explain_code(
                    provider,
                    model,
                    file_path,
                    code,
                )

            elif analysis == "Review Code":

                result = analyzer.review_code(
                    provider,
                    model,
                    file_path,
                    code,
                )

            elif analysis == "Complexity":

                result = analyzer.complexity_analysis(
                    provider,
                    model,
                    file_path,
                    code,
                )

            elif analysis == "Bug Finder":

                result = bug_finder.analyze_code(
                    provider,
                    model,
                    file_path,
                    code,
                )

            elif analysis == "Security Scan":

                result = security.analyze_code(
                    provider,
                    model,
                    file_path,
                    code,
                )

            elif analysis == "Documentation":

                result = documentation.generate_file_documentation(
                    provider,
                    model,
                    file_path,
                    code,
                )

            elif analysis == "Refactor":

                result = refactor.refactor_code(
                    provider,
                    model,
                    file_path,
                    code,
                )

        st.divider()

        st.subheader("AI Result")

        st.markdown(result)

        st.download_button(
            "Download Markdown",
            result,
            file_name="analysis.md",
            mime="text/markdown",
            use_container_width=True,
        )