from datetime import datetime


class RepositoryHelper:
    """
    Repository Utility Functions
    """

    @staticmethod
    def search_repositories(repositories, keyword):
        """
        Search repositories by name.
        """

        if not keyword:
            return repositories

        keyword = keyword.lower()

        return [
            repo
            for repo in repositories
            if keyword in repo["name"].lower()
        ]

    @staticmethod
    def filter_by_language(repositories, language):
        """
        Filter repositories by programming language.
        """

        if language == "All":
            return repositories

        return [
            repo
            for repo in repositories
            if repo.get("language") == language
        ]

    @staticmethod
    def sort_repositories(repositories, sort_by):
        """
        Sort repositories.
        """

        repos = repositories.copy()

        if sort_by == "Name":

            repos.sort(
                key=lambda x: x["name"].lower()
            )

        elif sort_by == "Stars":

            repos.sort(
                key=lambda x: x["stargazers_count"],
                reverse=True,
            )

        elif sort_by == "Forks":

            repos.sort(
                key=lambda x: x["forks_count"],
                reverse=True,
            )

        elif sort_by == "Recently Updated":

            repos.sort(
                key=lambda x: x["updated_at"],
                reverse=True,
            )

        elif sort_by == "Created Date":

            repos.sort(
                key=lambda x: x["created_at"],
                reverse=True,
            )

        return repos

    @staticmethod
    def calculate_statistics(repositories):
        """
        Dashboard statistics.
        """

        total_repositories = len(repositories)

        total_stars = sum(
            repo["stargazers_count"]
            for repo in repositories
        )

        total_forks = sum(
            repo["forks_count"]
            for repo in repositories
        )

        languages = {}

        for repo in repositories:

            lang = repo.get("language")

            if not lang:
                lang = "Unknown"

            languages[lang] = languages.get(lang, 0) + 1

        return {
            "repositories": total_repositories,
            "stars": total_stars,
            "forks": total_forks,
            "languages": languages,
        }

    @staticmethod
    def format_date(date_string):
        """
        Convert GitHub date into readable format.
        """

        if not date_string:
            return ""

        dt = datetime.strptime(
            date_string,
            "%Y-%m-%dT%H:%M:%SZ"
        )

        return dt.strftime("%d %b %Y")

    @staticmethod
    def top_languages(repositories):

        stats = RepositoryHelper.calculate_statistics(
            repositories
        )

        return sorted(
            stats["languages"].items(),
            key=lambda x: x[1],
            reverse=True,
        )