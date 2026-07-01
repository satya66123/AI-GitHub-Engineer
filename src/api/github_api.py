import requests

from src.config.settings import settings
from src.utils.logger import logger


class GitHubAPI:

    def __init__(self):
        self.base_url = settings.GITHUB_API_URL

        self.headers = {
            "Authorization": f"Bearer {settings.GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    def get_authenticated_user(self):
        """Return authenticated GitHub user."""

        try:
            response = requests.get(
                f"{self.base_url}/user",
                headers=self.headers,
                timeout=settings.REQUEST_TIMEOUT,
            )

            response.raise_for_status()

            logger.info("Authenticated successfully.")

            return response.json()

        except Exception as e:
            logger.error(e)
            return None

    def get_repositories(self):
        """Return authenticated user's repositories."""

        try:
            response = requests.get(
                f"{self.base_url}/user/repos",
                headers=self.headers,
                timeout=settings.REQUEST_TIMEOUT,
            )

            response.raise_for_status()

            logger.info("Repositories fetched successfully.")

            return response.json()

        except Exception as e:
            logger.error(e)
            return []