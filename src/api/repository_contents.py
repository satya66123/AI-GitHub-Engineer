import base64
import requests

from src.config.settings import settings
from src.utils.logger import logger


class RepositoryContents:

    def __init__(self):

        self.base_url = settings.GITHUB_API_URL

        self.headers = {
            "Authorization": f"Bearer {settings.GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    # --------------------------------------------------------
    # Common GET
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # Repository Tree
    # --------------------------------------------------------

    def get_tree(
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

    # --------------------------------------------------------
    # File Content
    # --------------------------------------------------------

    def get_file(
        self,
        owner,
        repository,
        path,
    ):

        file = self._get(
            f"/repos/{owner}/{repository}/contents/{path}"
        )

        if file is None:
            return None

        if "content" not in file:
            return None

        try:

            content = base64.b64decode(
                file["content"]
            ).decode(
                "utf-8",
                errors="ignore",
            )

            return content

        except Exception as e:

            logger.error(e)

            return None

    # --------------------------------------------------------
    # README
    # --------------------------------------------------------

    def get_readme(
        self,
        owner,
        repository,
    ):

        readme = self._get(
            f"/repos/{owner}/{repository}/readme"
        )

        if readme is None:
            return ""

        try:

            return base64.b64decode(
                readme["content"]
            ).decode(
                "utf-8",
                errors="ignore",
            )

        except Exception:

            return ""

    # --------------------------------------------------------
    # requirements.txt
    # --------------------------------------------------------

    def get_requirements(
        self,
        owner,
        repository,
    ):

        return self.get_file(
            owner,
            repository,
            "requirements.txt",
        )

    # --------------------------------------------------------
    # package.json
    # --------------------------------------------------------

    def get_package_json(
        self,
        owner,
        repository,
    ):

        return self.get_file(
            owner,
            repository,
            "package.json",
        )

    # --------------------------------------------------------
    # pom.xml
    # --------------------------------------------------------

    def get_pom(
        self,
        owner,
        repository,
    ):

        return self.get_file(
            owner,
            repository,
            "pom.xml",
        )

    # --------------------------------------------------------
    # composer.json
    # --------------------------------------------------------

    def get_composer(
        self,
        owner,
        repository,
    ):

        return self.get_file(
            owner,
            repository,
            "composer.json",
        )

    # --------------------------------------------------------
    # Dockerfile
    # --------------------------------------------------------

    def get_dockerfile(
        self,
        owner,
        repository,
    ):

        return self.get_file(
            owner,
            repository,
            "Dockerfile",
        )

    # --------------------------------------------------------
    # GitHub Workflow Files
    # --------------------------------------------------------

    def get_workflows(
        self,
        owner,
        repository,
    ):

        tree = self.get_tree(
            owner,
            repository,
        )

        workflow_files = []

        for item in tree:

            path = item.get("path", "")

            if path.startswith(".github/workflows/"):

                content = self.get_file(
                    owner,
                    repository,
                    path,
                )

                workflow_files.append(
                    {
                        "path": path,
                        "content": content,
                    }
                )

        return workflow_files

    # --------------------------------------------------------
    # Python Files
    # --------------------------------------------------------

    def get_python_files(
        self,
        owner,
        repository,
    ):

        tree = self.get_tree(
            owner,
            repository,
        )

        files = []

        for item in tree:

            if item["type"] != "blob":
                continue

            path = item["path"]

            if path.endswith(".py"):

                files.append(path)

        return files

    # --------------------------------------------------------
    # Java Files
    # --------------------------------------------------------

    def get_java_files(
        self,
        owner,
        repository,
    ):

        tree = self.get_tree(
            owner,
            repository,
        )

        files = []

        for item in tree:

            if item["type"] != "blob":
                continue

            path = item["path"]

            if path.endswith(".java"):

                files.append(path)

        return files

    # --------------------------------------------------------
    # JavaScript Files
    # --------------------------------------------------------

    def get_javascript_files(
        self,
        owner,
        repository,
    ):

        tree = self.get_tree(
            owner,
            repository,
        )

        files = []

        for item in tree:

            if item["type"] != "blob":
                continue

            path = item["path"]

            if path.endswith(".js"):

                files.append(path)

        return files

    # --------------------------------------------------------
    # PHP Files
    # --------------------------------------------------------

    def get_php_files(
        self,
        owner,
        repository,
    ):

        tree = self.get_tree(
            owner,
            repository,
        )

        files = []

        for item in tree:

            if item["type"] != "blob":
                continue

            path = item["path"]

            if path.endswith(".php"):

                files.append(path)

        return files

    # --------------------------------------------------------
    # Generic Extension Search
    # --------------------------------------------------------

    def get_files_by_extension(
        self,
        owner,
        repository,
        extension,
    ):

        tree = self.get_tree(
            owner,
            repository,
        )

        files = []

        for item in tree:

            if item["type"] != "blob":
                continue

            path = item["path"]

            if path.endswith(extension):

                files.append(path)

        return files