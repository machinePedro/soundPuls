class DecisionEngine:
    def __init__(self):
        pass

    def prioritize_threats(self, threats):
        # Ordena ameaças por score (quanto menor, mais relevante)
        return sorted(threats, key=lambda t: t['score'])