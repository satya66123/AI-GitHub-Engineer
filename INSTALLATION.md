# ⚙️ Installation Guide

<p align="center">

![Installation](https://img.shields.io/badge/Installation-Guide-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge\&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Supported-FF4B4B?style=for-the-badge\&logo=streamlit)
![OpenAI](https://img.shields.io/badge/OpenAI-Supported-412991?style=for-the-badge\&logo=openai)
![Ollama](https://img.shields.io/badge/Ollama-Supported-black?style=for-the-badge)
![Version](https://img.shields.io/badge/v1.0.0-Stable-success?style=for-the-badge)

</p>

---

# 📑 Table of Contents

* Prerequisites
* Clone Repository
* Create Virtual Environment
* Install Dependencies
* Configure Environment Variables
* Install Ollama
* Configure OpenAI
* Run Application
* Verify Installation
* Troubleshooting

---

# 💻 Prerequisites

Before installing, ensure you have the following software installed.

| Software                  | Version             |
| ------------------------- | ------------------- |
| Python                    | 3.11+               |
| Git                       | Latest              |
| Streamlit                 | Latest              |
| Ollama                    | Latest              |
| GitHub Account            | Required            |
| OpenAI API Key (Optional) | Required for OpenAI |

---

# 📥 Clone Repository

```bash
git clone https://github.com/satya66123/AI-GitHub-Engineer.git

cd AI-GitHub-Engineer
```

---

# 🐍 Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

Verify installation

```bash
pip list
```

---

# 🤖 Install Ollama

Download and install Ollama from:

https://ollama.com

After installation, verify:

```bash
ollama --version
```

---

# 📥 Download Models

Example:

```bash
ollama pull qwen2.5:1.5b

ollama pull llama3.1:8b

ollama pull gemma3:4b
```

Recommended default model

```text
qwen2.5:1.5b
```

---

# 🔐 Environment Variables

Create a `.env` file.

```env
GITHUB_TOKEN=your_github_personal_access_token

OPENAI_API_KEY=your_openai_api_key

DEFAULT_PROVIDER=Ollama

DEFAULT_OLLAMA_MODEL=qwen2.5:1.5b

OLLAMA_URL=http://localhost:11434/api/generate

OLLAMA_TAGS_URL=http://localhost:11434/api/tags
```

---

# 🔑 GitHub Token

Create a GitHub Personal Access Token with permissions such as:

* repo
* read:user
* read:org

Paste it into your `.env` file.

---

# 🤖 OpenAI Configuration

If using OpenAI:

```env
OPENAI_API_KEY=your_api_key
```

If using Ollama only:

Leave the OpenAI key empty.

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Application URL

```text
http://localhost:8501
```

---

# ✅ Verify Installation

Ensure:

* GitHub profile loads
* Repository list appears
* AI Provider dropdown works
* Ollama models are listed
* OpenAI models appear (if configured)
* AI analysis completes successfully

---

# 🛠 Troubleshooting

## Ollama not detected

```bash
ollama serve
```

---

## GitHub Authentication Failed

* Verify Personal Access Token
* Check repository permissions

---

## OpenAI Authentication Failed

* Verify API key
* Check billing status
* Confirm internet connection

---

## No Models Found

Run:

```bash
ollama list
```

If empty:

```bash
ollama pull qwen2.5:1.5b
```

---

## Streamlit Not Found

Install Streamlit:

```bash
pip install streamlit
```

---

# 📸 Expected Home Screen

After successful installation, you should see:

* Dashboard
* Repository Explorer
* AI Repository Analysis
* AI Code Analysis
* AI Chat
* Engineering Dashboard
* Repository Score

---

# 🚀 Recommended Local Models

| Model          | Purpose                |
| -------------- | ---------------------- |
| qwen2.5:1.5b   | Fast general model     |
| llama3.1:8b    | High-quality reasoning |
| gemma3:4b      | Balanced performance   |
| mistral        | Code and documentation |
| deepseek-coder | Code generation        |

---

# 📋 Installation Checklist

* ✅ Python Installed
* ✅ Git Installed
* ✅ Ollama Installed
* ✅ Models Downloaded
* ✅ Repository Cloned
* ✅ Virtual Environment Created
* ✅ Dependencies Installed
* ✅ Environment Variables Configured
* ✅ Application Running

---

<p align="center">

![Installation Complete](https://img.shields.io/badge/Installation-Complete-success?style=for-the-badge)

**🚀 Ready to start using AI GitHub Engineer**

</p>
