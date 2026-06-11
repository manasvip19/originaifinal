import re


def _clamp(value, low=0, high=100):
    return max(low, min(high, int(value)))


class ScoringEngine:

    def score(self, summary, startup, market):
        word_count = len(summary.split()) if isinstance(summary, str) else 0
        discovery_strength = len(startup.get('solution', ''))
        growth_rate = self._parse_growth(market.get('industry_growth'))

        innovation = _clamp(35 + word_count // 8 + discovery_strength // 30)
        commercialization = _clamp(40 + word_count // 7 + growth_rate // 4)
        risk = _clamp(50 - word_count // 18 - discovery_strength // 60 + 3, 5, 90)
        investment = _clamp((innovation + commercialization - risk) // 2 + 12)
        funding_readiness = _clamp((investment + commercialization) // 2 + 8)
        investor_interest = _clamp((innovation + investment + commercialization) // 3 + 10)
        technology_readiness = _clamp(2 + min(discovery_strength // 35, 8), 1, 10)
        market_readiness = _clamp((growth_rate + commercialization) // 2, 1, 10)
        commercialization_readiness = _clamp((commercialization + market_readiness * 10) // 2)
        market_timing = _clamp(growth_rate + commercialization // 5)
        unicorn = _clamp((innovation + investment + market_timing) // 3)

        startup_success_probability = self._success_label(investment, risk, commercialization)
        commercialization_difficulty = self._difficulty_label(risk, commercialization)
        global_impact = _clamp((innovation + growth_rate + investment) // 3)

        return {
            "innovation_level": innovation,
            "scalability_score": _clamp(commercialization + 5),
            "risk_score": risk,
            "commercial_potential": commercialization,
            "investment_score": investment,
            "unicorn_potential_score": unicorn,
            "funding_readiness_score": funding_readiness,
            "investor_interest_score": investor_interest,
            "technology_readiness_level": technology_readiness,
            "market_readiness_level": market_readiness,
            "commercialization_readiness_score": commercialization_readiness,
            "market_timing_score": market_timing,
            "startup_success_probability": startup_success_probability,
            "commercialization_difficulty": commercialization_difficulty,
            "global_impact_score": global_impact,
            "commercialization_timeline": self._timeline(technology_readiness, market_readiness)
        }

    def _parse_growth(self, growth_value):
        if not isinstance(growth_value, str):
            return 18
        digits = re.findall(r"\d+", growth_value)
        if digits:
            return int(digits[0])
        return 18

    def _success_label(self, investment, risk, commercialization):
        score = investment + commercialization - risk
        if score >= 120:
            return "Very High"
        if score >= 90:
            return "High"
        if score >= 60:
            return "Moderate"
        return "Low"

    def _difficulty_label(self, risk, commercialization):
        if risk <= 15 and commercialization >= 70:
            return "Low"
        if risk <= 30:
            return "Medium"
        return "High"

    def _timeline(self, tech_readiness, market_readiness):
        if tech_readiness >= 8 and market_readiness >= 7:
            return "12-18 months"
        if tech_readiness >= 6 and market_readiness >= 5:
            return "18-24 months"
        return "24-36 months"
