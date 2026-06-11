class IndustryMapper:

    INDUSTRY_KEYWORDS = {
        "Healthcare": ["health", "medical", "biomedical", "clinical", "nanomedicine", "diagnostic", "patient", "therapy", "biotech"],
        "Agriculture": ["crop", "agriculture", "farming", "harvest", "soil", "plant", "disease", "pesticide", "horticulture"],
        "Energy": ["energy", "battery", "solar", "wind", "power", "grid", "storage", "renewable", "electric"],
        "FinTech": ["financial", "bank", "payment", "blockchain", "transaction", "insurance", "credit", "investment", "ledger"],
        "Robotics": ["robot", "automation", "autonomous", "navigation", "drone", "actuator", "sensor", "mobility", "mechatronic"],
        "ClimateTech": ["climate", "carbon", "sustainability", "emissions", "environment", "recycling", "ecosystem", "conservation"],
        "Cybersecurity": ["security", "cyber", "encryption", "malware", "threat", "privacy", "authentication", "firewall"],
        "Education": ["education", "learning", "tutor", "classroom", "student", "curriculum", "edtech", "training"]
    }

    def map_industry(self, discovery):
        text = discovery.lower() if isinstance(discovery, str) else ""
        scores = {industry: 0 for industry in self.INDUSTRY_KEYWORDS}

        for industry, keywords in self.INDUSTRY_KEYWORDS.items():
            for keyword in keywords:
                if keyword in text:
                    scores[industry] += 1

        sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
        if sorted_scores and sorted_scores[0][1] > 0:
            return sorted_scores[0][0]

        return "Technology"