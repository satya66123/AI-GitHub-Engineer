# src/ui/settings.py

import streamlit as st

from src.ai.models import AIModels


def show_settings():

    st.title("⚙️ Settings")

    st.subheader("AI Configuration")

    provider = st.selectbox(
        "Default AI Provider",
        AIModels.providers(),
        key="default_provider",
    )

    model = st.selectbox(
        "Default Model",
        AIModels.models(provider),
        key="default_model",
    )

    st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.2,
        step=0.1,
        key="temperature",
    )

    st.slider(
        "Maximum Tokens",
        min_value=256,
        max_value=8192,
        value=2048,
        step=256,
        key="max_tokens",
    )

    st.divider()

    st.subheader("GitHub")

    st.checkbox(
        "Show Private Repositories",
        value=True,
        key="private_repositories",
    )

    st.checkbox(
        "Automatically Analyze README",
        value=True,
        key="auto_readme",
    )

    st.checkbox(
        "Automatically Detect Dependencies",
        value=True,
        key="auto_dependencies",
    )

    st.checkbox(
        "Automatically Analyze Repository Structure",
        value=True,
        key="auto_structure",
    )

    st.divider()

    st.subheader("Export")

    st.checkbox(
        "Enable Markdown Export",
        value=True,
        key="markdown_export",
    )

    st.checkbox(
        "Enable TXT Export",
        value=True,
        key="txt_export",
    )

    st.checkbox(
        "Enable PDF Export",
        value=False,
        key="pdf_export",
    )

    st.checkbox(
        "Enable DOCX Export",
        value=False,
        key="docx_export",
    )

    st.divider()

    if st.button(
        "Save Settings",
        use_container_width=True,
        type="primary",
    ):

        st.success("Settings saved successfully.")