# src/ui/logs.py

import os
import streamlit as st


LOG_FILE = "logs/app.log"


def show_logs():

    st.title("📄 Application Logs")

    if not os.path.exists(LOG_FILE):

        st.warning("Log file not found.")

        return

    with open(
        LOG_FILE,
        "r",
        encoding="utf-8",
        errors="ignore",
    ) as file:

        logs = file.readlines()

    total_logs = len(logs)

    col1, col2 = st.columns(2)

    col1.metric(
        "Total Log Entries",
        total_logs,
    )

    col2.metric(
        "Log File",
        "app.log",
    )

    st.divider()

    keyword = st.text_input(
        "Search Logs",
        placeholder="ERROR, INFO, WARNING...",
    )

    level = st.selectbox(
        "Log Level",
        [
            "ALL",
            "INFO",
            "WARNING",
            "ERROR",
            "CRITICAL",
        ],
    )

    filtered_logs = []

    for line in logs:

        if level != "ALL":

            if level not in line:
                continue

        if keyword:

            if keyword.lower() not in line.lower():
                continue

        filtered_logs.append(line)

    st.subheader(
        f"Showing {len(filtered_logs)} Log Entries"
    )

    log_text = "".join(filtered_logs)

    st.text_area(
        "Application Logs",
        value=log_text,
        height=500,
    )

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(
            "⬇ Download Logs",
            data=log_text,
            file_name="app.log",
            mime="text/plain",
            use_container_width=True,
        )

    with col2:

        if st.button(
            "🗑 Clear Logs",
            use_container_width=True,
        ):

            with open(
                LOG_FILE,
                "w",
                encoding="utf-8",
            ) as file:

                file.write("")

            st.success("Logs cleared successfully.")

            st.rerun()