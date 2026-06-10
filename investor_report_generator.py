class InvestorReportGenerator:

    def generate_report(self, research_summary, discovery, startup, market, scores):
        market_name = market.get('market_size', 'the addressable market')
        return {
            "executive_summary": (
                f"{startup.get('name', 'The opportunity')} is a research commercialization opportunity positioned to capture {market_name}. "
                f"The company combines deep domain research, a proven commercial model, and investor-ready execution."
            ),
            "research_overview": research_summary,
            "key_discovery": discovery,
            "startup_opportunity": (
                f"{startup.get('name', 'The opportunity')} provides {startup.get('solution', 'a scalable solution').lower()} for {startup.get('target_market', 'target customers')}. "
                f"This opportunity is built on research-driven differentiation and a clear path to market."
            ),
            "problem_solved": startup.get('problem', 'A real commercialization gap that prevents research from reaching market-ready products.'),
            "solution": startup.get('solution', 'A structured platform that turns research findings into investor-ready products.'),
            "industry": startup.get('industry', market.get('industry', 'Technology')),
            "target_market": startup.get('target_market', 'Research institutions, innovation teams, and strategic investors.'),
            "market_size": market.get('market_size', 'N/A'),
            "tam": market.get('tam', 'N/A'),
            "sam": market.get('sam', 'N/A'),
            "som": market.get('som', 'N/A'),
            "business_model": startup.get('business_model', 'Subscription SaaS with enterprise licensing and growth services.'),
            "revenue_model": ", ".join(startup.get('revenue_streams', [])) or 'Subscription and services',
            "go_to_market_plan": startup.get('go_to_market_strategy', 'Target pilot customers, partner with research labs, and scale through enterprise channels.'),
            "competition_analysis": startup.get('competitive_advantage', 'Competitive differentiation comes from research-backed IP, fast validation, and a clear market entry plan.'),
            "risk_analysis": (
                f"Risk is balanced across execution, market adoption, and technology readiness. The current risk score is {scores.get('risk_score', 'N/A')}."
            ),
            "technology_readiness": (
                f"Technology readiness is currently rated {scores.get('technology_readiness_level', 'N/A')} out of 10 based on solution maturity and innovation strength."
            ),
            "commercialization_readiness": (
                f"Commercialization readiness is {scores.get('commercialization_readiness_score', 'N/A')} / 100, reflecting market validation and scaling potential."
            ),
            "funding_readiness": (
                f"Funding readiness is {scores.get('funding_readiness_score', 'N/A')} / 100, indicating the opportunity is approaching investor-ready position."
            ),
            "expected_roi": (
                f"Expected ROI is strong given the market size, revenue model, and investor interest score of {scores.get('investor_interest_score', 'N/A')}."
            ),
            "investment_recommendation": (
                f"Recommend a focused round to close product-market fit, accelerate go-to-market execution, and secure industry partnerships in the {startup.get('industry', market.get('industry', 'technology')).lower()} sector."
            ),
            "final_verdict": (
                "The opportunity is strong for early-stage investors seeking research-led innovation with scalable commercialization potential."
            )
        }
