# src/ui/chat_history.py

import os
import streamlit as st

from src.ai.chat_history import ChatHistory


history = ChatHistory()


def show_chat_history():

    st.title("📝 AI Chat History")

    chats = history.load_all()

    if len(chats) == 0:

        st.info("No chat history found.")

        return

    st.sidebar.subheader("History")

    titles = []

    for chat in chats:

        titles.append(
            f"{chat['timestamp']} | {chat['repository']}"
        )

    selected = st.sidebar.selectbox(
        "Saved Chats",
        titles,
    )

    index = titles.index(selected)

    chat = chats[index]

    st.subheader("Repository")

    st.success(chat["repository"])

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Provider",
            chat["provider"],
        )

    with col2:

        st.metric(
            "Model",
            chat["model"],
        )

    st.divider()

    st.subheader("Prompt")

    st.text_area(
        "",
        chat["prompt"],
        height=180,
        disabled=True,
    )

    st.divider()

    st.subheader("AI Response")

    st.markdown(chat["response"])

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:

        st.download_button(
            "⬇ Markdown",
            chat["response"],
            file_name=f"{chat['timestamp']}.md",
            mime="text/markdown",
            use_container_width=True,
        )

    with c2:

        st.download_button(
            "⬇ Text",
            chat["response"],
            file_name=f"{chat['timestamp']}.txt",
            mime="text/plain",
            use_container_width=True,
        )

    with c3:

        filename = f"{chat['timestamp']}.json"

        if st.button(
            "🗑 Delete",
            use_container_width=True,
        ):

            history.delete(filename)

            st.success("Deleted successfully.")

            st.rerun()

    st.divider()

    if st.button(
        "🧹 Clear Entire History",
        use_container_width=True,
    ):

        history.clear()

        st.success("History cleared.")

        st.rerun()