class PitchGenerator:

    def generate(self, research_summary, discovery, startup, market, scores):
        slides = [
            {
                "title": "Cover",
                "content": f"{startup.get('name', 'Research Venture')} — {startup.get('tagline', 'Research-to-market commercialization.') }"
            },
            {
                "title": "Problem",
                "content": startup.get('problem', 'Research breakthroughs struggle to reach market-ready products and investor traction.')
            },
            {
                "title": "Solution",
                "content": startup.get('solution', 'A commercialization engine that transforms academic innovation into a scalable product strategy.')
            },
            {
                "title": "Technology",
                "content": startup.get('technology_highlight', 'A research-backed technology platform designed to validate and commercialize discoveries quickly.')
            },
            {
                "title": "Market",
                "content": (
                    f"Addressable market: {market.get('market_size', 'N/A')}, growth: {market.get('growth_rate', 'N/A')}. "
                    f"TAM: {market.get('tam', 'N/A')}, SAM: {market.get('sam', 'N/A')}, SOM: {market.get('som', 'N/A')}"
                )
            },
            {
                "title": "Competition",
                "content": startup.get('competitive_advantage', 'Differentiates through research-driven IP, faster validation, and tailored commercial pathways.')
            },
            {
                "title": "Business Model",
                "content": startup.get('business_model', 'Subscription SaaS with enterprise licensing and premium services.')
            },
            {
                "title": "Revenue",
                "content": startup.get('revenue_streams') and ', '.join(startup.get('revenue_streams', [])) or 'Subscription, licensing, and professional services.'
            },
            {
                "title": "Financials",
                "content": (
                    f"Opportunity score: {scores.get('investment_score', 'N/A')} / 100, "
                    f"Funding readiness: {scores.get('funding_readiness_score', 'N/A')} / 100, "
                    f"Investor interest: {scores.get('investor_interest_score', 'N/A')} / 100."
                )
            },
            {
                "title": "Roadmap",
                "content": startup.get('growth_strategy', 'Pilot early customers, expand into adjacent verticals, and scale commercialization through enterprise adoption.')
            },
            {
                "title": "Funding Ask",
                "content": startup.get('funding_strategy', 'Raise capital to accelerate product-market fit and commercial launch.')
            },
            {
                "title": "Vision",
                "content": startup.get('vision', 'Build the leading research commercialization engine with broad industry impact.')
            },
            {
                "title": "Conclusion",
                "content": (
                    f"{startup.get('name', 'This opportunity')} is a strong candidate for early-stage investors seeking research-backed, scalable commercialization potential."
                )
            }
        ]

        return {
            "slides": slides
        }
