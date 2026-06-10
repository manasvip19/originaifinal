from investor_report_generator import InvestorReportGenerator


def test_investor_report_contains_sections():
    generator = InvestorReportGenerator()
    report = generator.generate_report(
        research_summary='A next-generation AI product for climate risk quantification.',
        discovery='A research-based climate risk scoring model that predicts extreme weather losses.',
        startup={
            'name': 'ClimateEye',
            'tagline': 'Real-time climate risk intelligence.',
            'solution': 'A predictive climate intelligence platform.',
            'problem': 'Enterprises need faster, more accurate climate risk insights.',
            'industry': 'Climate Tech',
            'business_model': 'SaaS with tiered enterprise pricing',
            'revenue_streams': ['subscriptions', 'data licensing'],
            'go_to_market_strategy': 'Partner with insurance and asset managers.',
            'competitive_advantage': 'Proprietary climate models and enterprise integration.'
        },
        market={
            'industry': 'Climate Tech',
            'market_size': 'USD 12B',
            'tam': 'USD 30B',
            'sam': 'USD 15B',
            'som': 'USD 5B',
            'trend': 'accelerating'
        },
        scores={
            'investment_score': 86,
            'risk_score': 20,
            'technology_readiness_level': 7,
            'commercialization_readiness_score': 80,
            'funding_readiness_score': 75,
            'investor_interest_score': 82
        }
    )

    assert 'executive_summary' in report
    assert 'research_overview' in report
    assert 'key_discovery' in report
    assert 'startup_opportunity' in report
    assert 'problem_solved' in report
    assert 'solution' in report
    assert 'industry' in report
    assert 'target_market' in report
    assert 'market_size' in report
    assert 'business_model' in report
    assert 'revenue_model' in report
    assert 'go_to_market_plan' in report
    assert 'competition_analysis' in report
    assert 'risk_analysis' in report
    assert 'technology_readiness' in report
    assert 'commercialization_readiness' in report
    assert 'funding_readiness' in report
    assert 'investment_recommendation' in report
    assert 'final_verdict' in report

    assert 'ClimateEye' in report['executive_summary'] or 'ClimateEye' in report['startup_opportunity']
