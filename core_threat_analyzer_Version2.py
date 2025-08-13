from textblob import TextBlob

class ThreatAnalyzer:
    def analyze(self, text):
        sentiment = TextBlob(text).sentiment.polarity
        if sentiment < -0.3:
            return {'text': text, 'score': sentiment}
        return None