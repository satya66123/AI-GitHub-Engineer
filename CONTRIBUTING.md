# 🤝 Contributing Guide

<p align="center">

![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=for-the-badge)
![Pull Requests](https://img.shields.io/badge/Pull_Requests-Welcome-blue?style=for-the-badge)
![Issues](https://img.shields.io/badge/Issues-Welcome-orange?style=for-the-badge)
![Open Source](https://img.shields.io/badge/Open_Source-Friendly-success?style=for-the-badge)
![Version](https://img.shields.io/badge/v1.0.0-Stable-success?style=for-the-badge)

</p>

---

# 👋 Welcome

Thank you for your interest in contributing to **AI GitHub Engineer**.

Whether you're fixing bugs, improving documentation, optimizing performance, or proposing new AI features, your contributions are appreciated.

---

# 📑 Table of Contents

* Ways to Contribute
* Development Setup
* Project Structure
* Coding Standards
* Branch Strategy
* Commit Message Guidelines
* Pull Request Process
* Reporting Issues
* Feature Requests
* Code of Conduct

---

# 🚀 Ways to Contribute

You can contribute by:

* 🐛 Fixing bugs
* ✨ Adding new features
* 📚 Improving documentation
* 🎨 Enhancing the UI
* ⚡ Optimizing performance
* 🔒 Improving security
* 🧪 Adding tests
* 🌍 Improving accessibility
* 💡 Suggesting ideas

---

# 💻 Development Setup

## 1. Fork the Repository

Click the **Fork** button on GitHub.

---

## 2. Clone Your Fork

```bash id="f7zqma"
git clone https://github.com/<your-username>/AI-GitHub-Engineer.git

cd AI-GitHub-Engineer
```

---

## 3. Create a Virtual Environment

```bash id="5ixt5e"
python -m venv venv
```

Activate:

Windows

```bash id="p9e7dk"
venv\Scripts\activate
```

Linux/macOS

```bash id="4mw1a8"
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash id="jlwmts"
pip install -r requirements.txt
```

---

## 5. Configure Environment

Create a `.env` file.

```env id="b6hk2d"
GITHUB_TOKEN=

OPENAI_API_KEY=

DEFAULT_PROVIDER=Ollama
```

---

## 6. Run the Application

```bash id="2uk7gw"
streamlit run app.py
```

---

# 📁 Project Structure

Main folders:

```text id="tnybjt"
src/

├── ai/
├── api/
├── config/
├── ui/
└── utils/
```

Keep new modules inside the appropriate package.

---

# 🧹 Coding Standards

Please follow these guidelines:

* Use meaningful variable names.
* Write modular code.
* Keep functions focused on a single responsibility.
* Add docstrings where appropriate.
* Prefer readability over cleverness.
* Avoid duplicated code.

---

# 🌿 Branch Strategy

Create a feature branch for every contribution.

Example:

```bash id="96dvf3"
git checkout -b feature/new-feature
```

Examples:

* feature/repository-search
* feature/docker-analysis
* fix/chat-history
* docs/readme-update

---

# 📝 Commit Message Guidelines

Use Conventional Commits.

Examples:

```text id="kp49s0"
feat: add repository score improvements

fix: resolve GitHub authentication issue

docs: update installation guide

refactor: simplify repository analyzer

test: add unit tests for GitHub API

style: improve dashboard layout
```

---

# 🔄 Pull Request Process

Before submitting a Pull Request:

* Ensure the application runs successfully.
* Test your changes.
* Update documentation if necessary.
* Keep commits focused and descriptive.
* Resolve merge conflicts.

When opening the PR:

* Describe the change.
* Explain the motivation.
* Reference related issues if applicable.
* Include screenshots for UI changes.

---

# 🐞 Reporting Issues

When reporting a bug, include:

* Operating System
* Python version
* Error message
* Steps to reproduce
* Expected behavior
* Actual behavior
* Screenshots (if applicable)

---

# 💡 Feature Requests

Feature requests are welcome.

A good feature request should include:

* Problem statement
* Proposed solution
* Benefits
* Example workflow
* Additional context

---

# 🔒 Security

If you discover a security issue:

* Do not publish sensitive information publicly.
* Contact the maintainer privately if possible.
* Include clear reproduction steps.

---

# 🧪 Testing

Before submitting code:

* Verify the application starts correctly.
* Test affected functionality.
* Ensure no existing features are broken.
* Check both Ollama and OpenAI workflows if your changes affect AI integration.

---

# 📚 Documentation

Documentation improvements are encouraged.

Examples:

* Better examples
* Typo fixes
* API documentation
* Screenshots
* Architecture diagrams
* Tutorials

---

# 🌟 Recognition

Every meaningful contribution helps improve the project.

Contributors may be recognized in future releases and release notes.

---

# 📜 Code of Conduct

Please:

* Be respectful.
* Be constructive.
* Welcome new contributors.
* Focus on collaboration.
* Provide helpful feedback.

Harassment, discrimination, or abusive behavior will not be tolerated.

---

# 🚀 Future Contributions

Areas where contributions are especially welcome:

* MCP integration
* Semantic repository search
* Vector database support
* Multi-agent AI
* GitHub Actions integration
* Plugin architecture
* Performance optimization
* Additional export formats
* UI enhancements
* Testing improvements

---

# ❤️ Thank You

Thank you for helping improve **AI GitHub Engineer**.

Every contribution—whether code, documentation, bug reports, or ideas—helps make the project better for everyone.

---

<p align="center">

![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=for-the-badge)

![Pull Requests](https://img.shields.io/badge/Pull%20Requests-Welcome-blue?style=for-the-badge)

**🚀 Let's build better AI software engineering tools together!**

</p>
