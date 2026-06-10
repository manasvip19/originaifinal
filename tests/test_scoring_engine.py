from scoring_engine import ScoringEngine


def test_scoring_engine_returns_all_scores():
    engine = ScoringEngine()
    startup = {'solution': 'A machine learning commercialization platform.'}
    market = {'industry_growth': '+22%'}
    scores = engine.score('This is a sample research summary that is sufficiently long.', startup, market)

    required_keys = [
        'innovation_level',
        'scalability_score',
        'risk_score',
        'commercial_potential',
        'investment_score',
        'unicorn_potential_score',
        'funding_readiness_score',
        'investor_interest_score',
        'technology_readiness_level',
        'market_readiness_level',
        'commercialization_readiness_score',
        'market_timing_score',
        'startup_success_probability',
    ]

    assert all(key in scores for key in required_keys)
    assert 0 <= scores['innovation_level'] <= 100
    assert 0 <= scores['investment_score'] <= 100

