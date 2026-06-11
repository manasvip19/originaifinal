import random
import re


class StartupGenerator:

    STARTUP_SUFFIXES = ["AI", "Labs", "Systems", "Solutions", "Works", "Dynamics", "Analytics"]
    STARTUP_PREFIXES = ["Nova", "Quantum", "Eco", "Neo", "Pulse", "Vertex", "Alpha", "Core"]

    def generate(self, summary, discovery=None, industry="Technology"):
        if not summary:
            summary = "A commercialization engine for emerging research-driven ventures."

        startup_name = self._build_name(summary, discovery, industry)
        tagline = self._build_tagline(summary, discovery, industry)
        mission = f"Enable organizations to bring {industry.lower()} research to market with speed, precision and commercial readiness."
        vision = f"To be the trusted platform that converts academic breakthroughs into investor-ready companies in {industry.lower()}."
        problem = self._extract_problem(summary)
        solution = self._extract_solution(summary, discovery)
        target_market = self._build_target_market(summary, industry)
        technology_highlight = self._build_technology_highlight(discovery, summary)
        value_proposition = self._build_value_proposition(summary, industry)
        competitive_advantage = self._build_competitive_advantage(summary, industry)
        business_model = self._build_business_model(industry)
        revenue_streams = self._build_revenue_streams(industry)
        gtm_strategy = self._build_gtm_strategy(industry)
        growth_strategy = self._build_growth_strategy(industry)
        funding_strategy = self._build_funding_strategy(industry)
        commercialization_roadmap = self._build_commercialization_roadmap(industry)
        funding_roadmap = self._build_funding_roadmap(industry)
        founder_profile = self._build_founder_profile(industry)

        return {
            "name": startup_name,
            "tagline": tagline,
            "mission": mission,
            "vision": vision,
            "problem": problem,
            "solution": solution,
            "target_market": target_market,
            "technology_highlight": technology_highlight,
            "ideal_customer": target_market,
            "value_proposition": value_proposition,
            "competitive_advantage": competitive_advantage,
            "business_model": business_model,
            "revenue_streams": revenue_streams,
            "go_to_market_strategy": gtm_strategy,
            "growth_strategy": growth_strategy,
            "funding_strategy": funding_strategy,
            "commercialization_roadmap": commercialization_roadmap,
            "funding_roadmap": funding_roadmap,
            "founder_profile": founder_profile,
            "exit_strategy": self._build_exit_strategy(industry)
        }

    def _build_name(self, summary, discovery, industry):
        seed = discovery or summary
        words = re.findall(r"\b[A-Z][a-z]{2,}\b|\b[a-z]{5,}\b", seed)
        core = None
        for candidate in words:
            if len(candidate) > 5 and candidate.lower() not in industry.lower():
                core = candidate
                break
        if not core:
            core = industry.replace('Tech', '').strip() or 'Origin'
        core = re.sub(r"[^A-Za-z0-9]", "", core)
        prefix = random.choice(self.STARTUP_PREFIXES)
        suffix = random.choice(self.STARTUP_SUFFIXES)
        return f"{prefix}{core}{suffix}"

    def _build_tagline(self, summary, discovery, industry):
        if discovery:
            return f"Bringing {discovery.lower()} to commercial scale in {industry.lower()}."
        return f"Turning {industry.lower()} research into investor-ready product opportunities."

    def _extract_problem(self, summary):
        problem_match = re.search(r"(problem|challenge|barrier|gap|obstacle|difficulty)[^\.]+", summary, flags=re.IGNORECASE)
        if problem_match:
            return problem_match.group(0).strip().rstrip('.') + '.'
        return "Complex research findings are hard to commercialize, delaying market entry and investor validation."

    def _extract_solution(self, summary, discovery):
        if discovery:
            return f"A commercialization platform that converts {discovery.lower()} into market-ready products, investor messaging, and scalable business models."
        return "A commercialization engine that turns technical breakthroughs into scalable offerings, go-to-market plans, and investor-ready execution."

    def _build_target_market(self, summary, industry):
        if "enterprise" in summary.lower() or "business" in summary.lower():
            return f"Enterprise innovation teams and strategic investors in {industry.lower()}."
        return f"Research institutions, innovation labs and early-stage investors focused on {industry.lower()}."

    def _build_technology_highlight(self, discovery, summary):
        if discovery:
            return f"Built around {discovery.lower()}, the solution accelerates validation and product integration."
        return f"Leverages advanced {summary.split()[0].lower()} concepts to deliver research-based product innovation."

    def _build_value_proposition(self, summary, industry):
        return f"Combines academic research intelligence with commercialization workflows to accelerate product-market fit in {industry.lower()}."

    def _build_competitive_advantage(self, summary, industry):
        return f"Differentiates through research-backed IP, rapid validation workflows, and a clear path from discovery to revenue in {industry.lower()}."

    def _build_business_model(self, industry):
        if industry == "Healthcare":
            return "Enterprise SaaS with clinical licensing and professional services."
        if industry == "FinTech":
            return "Subscription SaaS with transaction fees and premium analytics."
        if industry == "Energy":
            return "SaaS with systems integration and recurring service contracts."
        if industry == "Agriculture":
            return "Subscription platform with field services and data-driven advisory revenue."
        if industry == "Robotics":
            return "Software-enabled robotics-as-a-service plus implementation consulting."
        return "Subscription SaaS with enterprise licensing, premium services, and data monetization."

    def _build_revenue_streams(self, industry):
        streams = ["Subscription fees", "Enterprise licensing", "Professional services"]
        if industry in ["Healthcare", "FinTech"]:
            streams.append("Data monetization")
        else:
            streams.append("Integration services")
        return streams

    def _build_gtm_strategy(self, industry):
        return f"Launch with pilot customers in {industry.lower()}, partner with research labs, and scale through targeted B2B channels."

    def _build_growth_strategy(self, industry):
        return f"Expand into adjacent {industry.lower()} verticals while deepening enterprise adoption through proven pilot outcomes."

    def _build_funding_strategy(self, industry):
        return f"Raise capital to accelerate product-market fit, build strategic partnerships, and fund go-to-market expansion in {industry.lower()}."

    def _build_commercialization_roadmap(self, industry):
        return f"Pilot research use cases, validate with early customers, secure strategic partnerships, and expand commercialization across {industry.lower()} segments."

    def _build_funding_roadmap(self, industry):
        return "Use seed funding to complete product-market fit, followed by a growth round to scale sales, marketing, and industry partnerships."

    def _build_founder_profile(self, industry):
        return f"Founders combine research expertise, commercialization experience, and industry insight in {industry.lower()} innovation."

    def _build_exit_strategy(self, industry):
        return f"Position for strategic acquisition by leading {industry.lower()} incumbents or a growth-stage financing event."
