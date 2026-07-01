# src/config/settings.py

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """
    Application Configuration
    """

    # ---------------------------------------------------------
    # Application
    # ---------------------------------------------------------

    APP_NAME = "AI GitHub Engineer"

    VERSION = "1.0.0"

    DEBUG = True

    REQUEST_TIMEOUT = 300

    # ---------------------------------------------------------
    # GitHub
    # ---------------------------------------------------------

    GITHUB_API_URL = "https://api.github.com"

    GITHUB_TOKEN = os.getenv(
        "GITHUB_TOKEN",
        "",
    )

    # ---------------------------------------------------------
    # Ollama
    # ---------------------------------------------------------

    OLLAMA_URL = os.getenv(
        "OLLAMA_URL",
        "http://localhost:11434/api/generate",
    )

    OLLAMA_TAGS_URL = os.getenv(
        "OLLAMA_TAGS_URL",
        "http://localhost:11434/api/tags",
    )

    OLLAMA_EMBEDDING_URL = os.getenv(
        "OLLAMA_EMBEDDING_URL",
        "http://localhost:11434/api/embeddings",
    )

    DEFAULT_OLLAMA_MODEL = os.getenv(
        "DEFAULT_OLLAMA_MODEL",
        "qwen2.5:1.5b",
    )

    # ---------------------------------------------------------
    # OpenAI
    # ---------------------------------------------------------

    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY",
        "",
    )

    DEFAULT_OPENAI_MODEL = os.getenv(
        "DEFAULT_OPENAI_MODEL",
        "gpt-4.1-mini",
    )

    # ---------------------------------------------------------
    # AI
    # ---------------------------------------------------------

    DEFAULT_PROVIDER = os.getenv(
        "DEFAULT_PROVIDER",
        "Ollama",
    )

    DEFAULT_TEMPERATURE = float(
        os.getenv(
            "DEFAULT_TEMPERATURE",
            0.2,
        )
    )

    DEFAULT_MAX_TOKENS = int(
        os.getenv(
            "DEFAULT_MAX_TOKENS",
            2048,
        )
    )

    # ---------------------------------------------------------
    # Export
    # ---------------------------------------------------------

    EXPORT_FOLDER = "exports"

    HISTORY_FOLDER = "history"

    LOG_FOLDER = "logs"

    # ---------------------------------------------------------
    # Logging
    # ---------------------------------------------------------

    LOG_FILE = os.path.join(
        LOG_FOLDER,
        "app.log",
    )

    # ---------------------------------------------------------
    # GitHub Analysis
    # ---------------------------------------------------------

    MAX_REPOSITORIES = 100

    MAX_COMMITS = 20

    MAX_FILE_SIZE = 1024 * 1024  # 1 MB

    # ---------------------------------------------------------
    # Supported File Types
    # ---------------------------------------------------------

    SUPPORTED_EXTENSIONS = [

        ".py",

        ".java",

        ".js",

        ".ts",

        ".tsx",

        ".jsx",

        ".php",

        ".cs",

        ".cpp",

        ".c",

        ".h",

        ".hpp",

        ".go",

        ".rs",

        ".rb",

        ".swift",

        ".kt",

        ".scala",

        ".html",

        ".css",

        ".scss",

        ".sql",

        ".xml",

        ".json",

        ".yaml",

        ".yml",

        ".md",

        ".txt",

        ".dockerfile",
    ]

    # ---------------------------------------------------------
    # Dependency Files
    # ---------------------------------------------------------

    DEPENDENCY_FILES = [

        "requirements.txt",

        "package.json",

        "pom.xml",

        "composer.json",

        "Dockerfile",

        "docker-compose.yml",

        "pyproject.toml",

        "Pipfile",

        "build.gradle",

        "Cargo.toml",

        "go.mod",
    ]


settings = Settings()