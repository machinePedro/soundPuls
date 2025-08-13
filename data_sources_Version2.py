import requests

def fetch_news():
    # Simulação de coleta de notícias
    # Substitua pela sua API Key real
    API_KEY = "SUA_API_KEY"
    url = f"https://newsapi.org/v2/top-headlines?country=br&apiKey={API_KEY}"
    resp = requests.get(url)
    articles = resp.json().get("articles", [])
    return [f"{a['title']}. {a.get('description', '')}" for a in articles]