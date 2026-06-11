class MarketAnalyzer:

    MARKET_PROFILES = {
        "Healthcare": {
            "market_size": "$67.8B",
            "growth_rate": "+18.2%",
            "tam": "$240B",
            "sam": "$74B",
            "som": "$28B",
            "industry_growth": "+22%"
        },
        "Agriculture": {
            "market_size": "$32.2B",
            "growth_rate": "+16.8%",
            "tam": "$120B",
            "sam": "$42B",
            "som": "$15B",
            "industry_growth": "+19%"
        },
        "Energy": {
            "market_size": "$45.6B",
            "growth_rate": "+21.4%",
            "tam": "$190B",
            "sam": "$60B",
            "som": "$22B",
            "industry_growth": "+24%"
        },
        "FinTech": {
            "market_size": "$56.4B",
            "growth_rate": "+25.1%",
            "tam": "$210B",
            "sam": "$68B",
            "som": "$26B",
            "industry_growth": "+27%"
        },
        "Robotics": {
            "market_size": "$21.8B",
            "growth_rate": "+19.7%",
            "tam": "$85B",
            "sam": "$30B",
            "som": "$11B",
            "industry_growth": "+20%"
        },
        "Technology": {
            "market_size": "$38.3B",
            "growth_rate": "+17.8%",
            "tam": "$150B",
            "sam": "$55B",
            "som": "$18B",
            "industry_growth": "+18%"
        }
    }

    def analyze_market(self, industry):
        return self.MARKET_PROFILES.get(industry, self.MARKET_PROFILES["Technology"])
