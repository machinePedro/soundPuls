def display_alerts(threats):
    if not threats:
        print("Nenhuma ameaça relevante detectada.")
        return
    print("Atenção! Possíveis ameaças detectadas:")
    for t in threats:
        print(f"- {t['text']} (score: {t['score']})")