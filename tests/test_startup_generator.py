from startup_generator import StartupGenerator


def test_startup_generator_creates_complete_opportunity():
    generator = StartupGenerator()
    startup = generator.generate(
        summary='A novel research platform for adaptive robotics applications.',
        discovery='An autonomous navigation method for industrial vehicles.',
        industry='Robotics'
    )

    assert startup['name']
    assert startup['tagline']
    assert startup['problem']
    assert startup['solution']
    assert startup['business_model']
    assert isinstance(startup['revenue_streams'], list)
    assert startup['go_to_market_strategy']
    assert startup['funding_strategy']
    assert startup['commercialization_roadmap']
    assert startup['founder_profile']
