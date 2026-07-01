from src.api.github_api import GitHubAPI


def test_api_creation():

    api = GitHubAPI()

    assert api is not None


def test_authenticated_user_method():

    api = GitHubAPI()

    assert hasattr(api, "get_authenticated_user")


def test_repository_method():

    api = GitHubAPI()

    assert hasattr(api, "get_repositories")