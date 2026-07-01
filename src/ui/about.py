# src/ui/about.py

import streamlit as st


def show_about():

    st.title("🤖 AI GitHub Engineer")

    st.markdown("""
An AI-powered GitHub engineering platform built using
Python, Streamlit, GitHub REST API, Ollama and OpenAI.

---

## Features

### GitHub

- Dashboard
- Repository Explorer
- Branch Explorer
- Contributors
- Commit History
- Repository Statistics
- Repository Tree
- Repository Contents

---

### AI

- Repository Summary
- Architecture Analysis
- Dependency Analysis
- README Analysis
- Repository Health Report
- AI Code Review
- AI Documentation
- AI Refactoring
- Bug Detection
- Security Analysis
- AI Chat

---

### Providers

- Ollama
- OpenAI

---

### Export

- Markdown
- TXT
- PDF
- DOCX

---

### Technologies

- Python

- Streamlit

- GitHub REST API

- Ollama

- OpenAI

- Requests

- ReportLab

- python-docx

---

### Current Version

Version **1.0.0**

---

### Upcoming (Phase 4)

- AI Pull Request Review

- AI Issue Generator

- AI Commit Review

- AI Unit Test Generator

- AI Code Generator

- AI Repository Chat

- Multi Repository Analysis

- GitHub Automation

- MCP Integration

---

### Author

Built as a professional AI Software Engineering project.
""")