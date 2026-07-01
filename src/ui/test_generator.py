import streamlit as st

from src.ai.models import AIModels
from src.ai.test_generator import TestGenerator


def show_test_generator():

    st.title("🧪 AI Test Generator")

    generator = TestGenerator()

    col1, col2 = st.columns(2)

    with col1:

        provider = st.selectbox(
            "AI Provider",
            AIModels.providers(),
            key="test_provider",
        )

    with col2:

        model = st.selectbox(
            "Model",
            AIModels.models(provider),
            key="test_model",
        )

    language = st.selectbox(
        "Programming Language",
        [
            "Python (PyTest)",
            "Java (JUnit)",
            "JavaScript (Jest)",
            "PHP (PHPUnit)",
            "Integration Tests",
            "Coverage Report",
        ],
    )

    filename = st.text_input(
        "Filename",
        placeholder="example.py",
    )

    source_code = st.text_area(
        "Source Code",
        height=350,
        placeholder="Paste your source code here...",
    )

    if st.button(
        "🚀 Generate Tests",
        type="primary",
        use_container_width=True,
    ):

        if not source_code.strip():

            st.warning(
                "Please provide source code."
            )

            return

        with st.spinner(
            "Generating AI tests..."
        ):

            if language == "Python (PyTest)":

                result = generator.pytest(
                    provider,
                    model,
                    filename,
                    source_code,
                )

            elif language == "Java (JUnit)":

                result = generator.junit(
                    provider,
                    model,
                    filename,
                    source_code,
                )

            elif language == "JavaScript (Jest)":

                result = generator.jest(
                    provider,
                    model,
                    filename,
                    source_code,
                )

            elif language == "PHP (PHPUnit)":

                result = generator.phpunit(
                    provider,
                    model,
                    filename,
                    source_code,
                )

            elif language == "Integration Tests":

                result = generator.integration_tests(
                    provider,
                    model,
                    filename,
                    source_code,
                )

            else:

                result = generator.coverage_report(
                    provider,
                    model,
                    filename,
                    source_code,
                )

        st.divider()

        st.subheader("Generated Output")

        st.markdown(result)

        st.download_button(
            "⬇ Download",
            result,
            file_name="generated_tests.md",
            mime="text/markdown",
            use_container_width=True,
        )

        with st.expander("Source Code"):

            st.code(
                source_code,
                language="python",
            )

        with st.expander("Generated Result"):

            st.code(result)