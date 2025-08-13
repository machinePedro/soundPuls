from data.sources import fetch_news
from core.threat_analyzer import ThreatAnalyzer
from core.decision_engine import DecisionEngine
from interface.cli import display_alerts

def main():
    noticias = fetch_news()
    analyzer = ThreatAnalyzer()
    engine = DecisionEngine()
    threats = [analyzer.analyze(n) for n in noticias]
    threats = [t for t in threats if t]
    prioritized = engine.prioritize_threats(threats)
    display_alerts(prioritized)

if __name__ == "__main__":
    main()