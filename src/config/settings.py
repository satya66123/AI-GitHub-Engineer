"""
Project Configuration
---------------------
Loads environment variables and project settings.
"""

import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

class Settings:
    """Application settings."""

    # GitHub
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
    GITHUB_API_URL = "https://api.github.com"

    # Application
    APP_NAME = "AI GitHub Engineer"
    VERSION = "1.0.0"

    # Request Timeout
    REQUEST_TIMEOUT = 30


settings = Settings()