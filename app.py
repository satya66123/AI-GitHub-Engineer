import streamlit as st

from src.ui.home import show_home


st.set_page_config(
    page_title="AI GitHub Engineer",
    page_icon="🤖",
    layout="wide",
)

show_home()