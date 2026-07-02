import requests

from src.config.settings import settings
from src.utils.logger import logger


class GitHubAPI:
    """
    GitHub REST API Client
    """

    def __init__(self,token=None):

        if token is None:
            token = settings.GITHUB_TOKEN

        self.base_url = settings.GITHUB_API_URL

        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    # ----------------------------------------------------
    # Common GET Request
    # ----------------------------------------------------

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

    # ----------------------------------------------------
    # Authenticated User
    # ----------------------------------------------------

    def get_authenticated_user(self):

        return self._get("/user")

    # ----------------------------------------------------
    # User Repositories
    # ----------------------------------------------------

    def get_repositories(self):

        repos = self._get(
            "/user/repos?per_page=100&sort=updated"
        )

        if repos is None:
            return []

        return repos

    # ----------------------------------------------------
    # Repository Details
    # ----------------------------------------------------

    def get_repository(
        self,
        owner,
        repository,
    ):

        return self._get(
            f"/repos/{owner}/{repository}"
        )

    # ----------------------------------------------------
    # Branches
    # ----------------------------------------------------

    def get_branches(
        self,
        owner,
        repository,
    ):

        branches = self._get(
            f"/repos/{owner}/{repository}/branches"
        )

        if branches is None:
            return []

        return branches

    # ----------------------------------------------------
    # Contributors
    # ----------------------------------------------------

    def get_contributors(
        self,
        owner,
        repository,
    ):

        contributors = self._get(
            f"/repos/{owner}/{repository}/contributors"
        )

        if contributors is None:
            return []

        return contributors

    # ----------------------------------------------------
    # Commits
    # ----------------------------------------------------

    def get_commits(
        self,
        owner,
        repository,
        per_page=20,
    ):

        commits = self._get(
            f"/repos/{owner}/{repository}/commits?per_page={per_page}"
        )

        if commits is None:
            return []

        return commits

    # ----------------------------------------------------
    # Languages
    # ----------------------------------------------------

    def get_languages(
        self,
        repositories,
    ):

        languages = {"All"}

        for repo in repositories:

            language = repo.get("language")

            if language:
                languages.add(language)

        return sorted(list(languages))

    # ----------------------------------------------------
    # Repository Tree
    # ----------------------------------------------------

    def get_repository_tree(
        self,
        owner,
        repository,
        branch="main",
    ):

        branch_data = self._get(
            f"/repos/{owner}/{repository}/branches/{branch}"
        )

        if branch_data is None:
            return []

        sha = branch_data["commit"]["sha"]

        tree = self._get(
            f"/repos/{owner}/{repository}/git/trees/{sha}?recursive=1"
        )

        if tree is None:
            return []

        return tree.get("tree", [])

    # ----------------------------------------------------
    # Repository Contents
    # ----------------------------------------------------

    def get_contents(
        self,
        owner,
        repository,
        path="",
    ):

        result = self._get(
            f"/repos/{owner}/{repository}/contents/{path}"
        )

        if result is None:
            return []

        return result

    # ----------------------------------------------------
    # README
    # ----------------------------------------------------

    def get_readme(
        self,
        owner,
        repository,
    ):

        return self._get(
            f"/repos/{owner}/{repository}/readme"
        )

    # ----------------------------------------------------
    # Repository Languages
    # ----------------------------------------------------

    def get_repository_languages(
        self,
        owner,
        repository,
    ):

        languages = self._get(
            f"/repos/{owner}/{repository}/languages"
        )

        if languages is None:
            return {}

        return languages

    # ----------------------------------------------------
    # Repository Topics
    # ----------------------------------------------------

    def get_topics(
        self,
        owner,
        repository,
    ):

        try:

            response = requests.get(
                f"{self.base_url}/repos/{owner}/{repository}/topics",
                headers={
                    **self.headers,
                    "Accept": "application/vnd.github+json",
                },
                timeout=settings.REQUEST_TIMEOUT,
            )

            response.raise_for_status()

            data = response.json()

            return data.get("names", [])

        except Exception as e:

            logger.error(e)

            return []

    # ----------------------------------------------------
    # Releases
    # ----------------------------------------------------

    def get_releases(
        self,
        owner,
        repository,
    ):

        releases = self._get(
            f"/repos/{owner}/{repository}/releases"
        )

        if releases is None:
            return []

        return releases

    # ----------------------------------------------------
    # Pull Requests
    # ----------------------------------------------------

    def get_pull_requests(
        self,
        owner,
        repository,
        state="open",
    ):

        prs = self._get(
            f"/repos/{owner}/{repository}/pulls?state={state}"
        )

        if prs is None:
            return []

        return prs

    # ----------------------------------------------------
    # Issues
    # ----------------------------------------------------

    def get_issues(
        self,
        owner,
        repository,
        state="open",
    ):

        issues = self._get(
            f"/repos/{owner}/{repository}/issues?state={state}"
        )

        if issues is None:
            return []

        return issues

    # ----------------------------------------------------
    # Workflows
    # ----------------------------------------------------

    def get_workflows(
        self,
        owner,
        repository,
    ):

        workflows = self._get(
            f"/repos/{owner}/{repository}/actions/workflows"
        )

        if workflows is None:
            return []

        return workflows.get("workflows", [])

    # ----------------------------------------------------
    # Repository Statistics
    # ----------------------------------------------------

    def get_repository_statistics(
        self,
        repository,
    ):

        return {
            "stars": repository.get("stargazers_count", 0),
            "forks": repository.get("forks_count", 0),
            "watchers": repository.get("watchers_count", 0),
            "issues": repository.get("open_issues_count", 0),
            "size": repository.get("size", 0),
            "language": repository.get("language", "Unknown"),
            "default_branch": repository.get("default_branch", ""),
            "created_at": repository.get("created_at", ""),
            "updated_at": repository.get("updated_at", ""),
            "visibility": (
                "Private"
                if repository.get("private")
                else "Public"
            ),
        }
