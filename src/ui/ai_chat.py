# src/ui/ai_chat.py

import streamlit as st

from src.ai.models import AIModels
from src.ai.provider import AIProvider
from src.ai.streaming import StreamingAI
from src.ai.chat_history import ChatHistory


streaming = StreamingAI()
history = ChatHistory()


def show_ai_chat():

    st.title("💬 AI Repository Chat")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    provider = st.selectbox(
        "AI Provider",
        AIModels.providers(),
        key="chat_provider",
    )

    model = st.selectbox(
        "Model",
        AIModels.models(provider),
        key="chat_model",
    )

    repository = st.text_input(
        "Repository Name",
        placeholder="AI-GitHub-Engineer",
    )

    st.divider()

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    prompt = st.chat_input(
        "Ask anything about your repository..."
    )

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        final_prompt = f"""
    You are an expert AI GitHub Engineer.

    Repository:
    {repository}

    Question:
    {prompt}
    """

        with st.chat_message("assistant"):

            placeholder = st.empty()

            with st.spinner("🤖 AI is analyzing your repository..."):
                response = ""

                for chunk in streaming.stream(
                        provider,
                        model,
                        final_prompt,
                ):
                    response = chunk

                    placeholder.markdown(response + "▌")

                placeholder.markdown(response)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response,
            }
        )

        history.save(
            repository=repository,
            provider=provider,
            model=model,
            prompt=prompt,
            response=response,
        )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🧹 Clear Conversation",
            use_container_width=True,
        ):

            st.session_state.messages = []

            st.rerun()

    with col2:

        transcript = ""

        for message in st.session_state.messages:

            transcript += (
                f"{message['role'].upper()}\n"
                f"{message['content']}\n\n"
            )

        st.download_button(
            "⬇ Download Chat",
            transcript,
            file_name="ai_chat.md",
            mime="text/markdown",
            use_container_width=True,
        )