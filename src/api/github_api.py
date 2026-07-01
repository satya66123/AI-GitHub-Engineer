import requests

from src.config.settings import settings
from src.utils.logger import logger


class GitHubAPI:
    """
    GitHub REST API Client
    """

    def __init__(self):
        self.base_url = settings.GITHUB_API_URL

        self.headers = {
            "Authorization": f"Bearer {settings.GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    # -------------------------------------------------------
    # Common GET Request
    # -------------------------------------------------------

    def _get(self, endpoint):
        try:

            response = requests.get(
                f"{self.base_url}{endpoint}",
                headers=self.headers,
                timeout=settings.REQUEST_TIMEOUT,
            )

            response.raise_for_status()

            return response.json()

        except Exception as e:

            logger.error(e)

            return None

    # -------------------------------------------------------
    # User
    # -------------------------------------------------------

    def get_authenticated_user(self):

        return self._get("/user")

    # -------------------------------------------------------
    # Repositories
    # -------------------------------------------------------

    def get_repositories(self):

        repos = self._get("/user/repos?per_page=100&sort=updated")

        if repos is None:
            return []

        return repos

    # -------------------------------------------------------
    # Repository Details
    # -------------------------------------------------------

    def get_repository(self, owner, repo):

        return self._get(f"/repos/{owner}/{repo}")

    # -------------------------------------------------------
    # Branches
    # -------------------------------------------------------

    def get_branches(self, owner, repo):

        branches = self._get(f"/repos/{owner}/{repo}/branches")

        if branches is None:
            return []

        return branches

    # -------------------------------------------------------
    # Contributors
    # -------------------------------------------------------

    def get_contributors(self, owner, repo):

        contributors = self._get(
            f"/repos/{owner}/{repo}/contributors"
        )

        if contributors is None:
            return []

        return contributors

    # -------------------------------------------------------
    # Commits
    # -------------------------------------------------------

    def get_commits(self, owner, repo):

        commits = self._get(
            f"/repos/{owner}/{repo}/commits"
        )

        if commits is None:
            return []

        return commits

    # -------------------------------------------------------
    # Languages
    # -------------------------------------------------------

    def get_languages(self, repos):

        languages = {"All"}

        for repo in repos:

            lang = repo.get("language")

            if lang:
                languages.add(lang)

        return sorted(list(languages))