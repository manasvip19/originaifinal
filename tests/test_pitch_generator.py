from pitch_generator import PitchGenerator


def test_pitch_deck_has_core_slides():
    generator = PitchGenerator()
    result = generator.generate(
        research_summary='A platform that automates creative workflows for early-stage founders.',
        discovery='Automated design workflows improve speed and quality for remote teams.',
        startup={'name': 'FlowCraft', 'tagline': 'Automate creative startup growth.', 'problem': 'Manual workflows slow down founders.', 'solution': 'AI-driven automation for creative teams.', 'business_model': 'SaaS subscription', 'revenue_streams': ['subscriptions', 'services'], 'growth_strategy': 'Target agencies and enterprise creative teams.', 'vision': 'Empower every creator with intelligent workflow automation.'},
        market={'market_size': 'USD 8B', 'growth_rate': '+18%', 'tam': 'USD 24B', 'sam': 'USD 12B', 'som': 'USD 4B'},
        scores={'investment_score': 88, 'funding_readiness_score': 72, 'investor_interest_score': 80}
    )

    slides = result['slides']
    titles = [slide['title'] for slide in slides]
    assert 'Cover' in titles
    assert 'Problem' in titles
    assert 'Solution' in titles
    assert 'Market' in titles
    assert 'Financials' in titles or 'Business Model' in titles
    assert 'Conclusion' in titles
    assert any('FlowCraft' in slide.get('content', '') for slide in slides)
