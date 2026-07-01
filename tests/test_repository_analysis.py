from src.ai.repository_analyzer import RepositoryAnalyzer


def test_repository_analyzer_creation():

    analyzer = RepositoryAnalyzer()

    assert analyzer is not None


def test_repository_summary_exists():

    analyzer = RepositoryAnalyzer()

    assert hasattr(analyzer, "summarize")