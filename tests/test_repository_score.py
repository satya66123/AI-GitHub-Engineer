from src.ai.repository_scorer import RepositoryScorer


def test_repository_scorer_creation():

    scorer = RepositoryScorer()

    assert scorer is not None


def test_repository_score_method():

    scorer = RepositoryScorer()

    assert hasattr(scorer, "score_repository")