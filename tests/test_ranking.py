from app.ranking import lexical_score, hybrid_score


def test_lexical_overlap():
    assert lexical_score("annual leave", "annual leave policy") > 0


def test_hybrid_score_is_bounded():
    score = hybrid_score("annual leave", "annual leave policy", 0.9)
    assert 0.0 <= score <= 1.0
