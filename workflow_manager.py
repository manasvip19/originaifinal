from pdf_parser import extract_text
from research_agent import ResearchAgent
from industry_mapper import IndustryMapper
from startup_generator import StartupGenerator
from market_analyzer import MarketAnalyzer
from scoring_engine import ScoringEngine
from investor_report_generator import InvestorReportGenerator
from pitch_generator import PitchGenerator


class WorkflowManager:

    def run(self, pdf_path):

        text = extract_text(pdf_path)

        research = ResearchAgent()
        discovery = research.identify_discovery(text)
        summary = research.summarize(text)

        industry_mapper = IndustryMapper()
        industry = industry_mapper.map_industry(discovery or summary)

        startup_generator = StartupGenerator()
        startup = startup_generator.generate(summary, discovery, industry)

        market_analyzer = MarketAnalyzer()
        market = market_analyzer.analyze_market(industry)

        scorer = ScoringEngine()
        scores = scorer.score(summary, startup, market)

        investor_report = InvestorReportGenerator()
        report = investor_report.generate_report(summary, discovery, startup, market, scores)

        pitch_generator = PitchGenerator()
        pitch = pitch_generator.generate(summary, discovery, startup, market, scores)

        return {
            "research_summary": summary,
            "research_category": industry,
            "key_discovery": discovery,
            "industry": industry,
            "startup": startup,
            "market": market,
            "scores": scores,
            "investor_report": report,
            "pitch_deck": pitch
        }