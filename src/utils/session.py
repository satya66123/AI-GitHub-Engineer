# src/utils/session.py

import streamlit as st


class SessionManager:

    @staticmethod
    def initialize():

        defaults = {

            "provider": "Ollama",

            "model": "llama3.1:8b",

            "repository": "",

            "messages": [],

            "analysis": "",

            "report": "",

            "selected_file": "",

            "selected_page": "Dashboard",

        }

        for key, value in defaults.items():

            if key not in st.session_state:

                st.session_state[key] = value

    @staticmethod
    def clear_chat():

        st.session_state.messages = []

    @staticmethod
    def clear_analysis():

        st.session_state.analysis = ""

    @staticmethod
    def clear_report():

        st.session_state.report = ""

    @staticmethod
    def reset():

        keys = list(st.session_state.keys())

        for key in keys:

            del st.session_state[key]

        SessionManager.initialize()