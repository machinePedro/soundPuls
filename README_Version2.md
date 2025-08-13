# Máquina (Person of Interest - Inspired AI)

Sistema modular inspirado na Máquina da série Person of Interest. Realiza coleta, análise e priorização de ameaças com base em dados públicos.

## Como usar

1. Instale dependências:
    ```
    pip install -r requirements.txt
    ```

2. Defina sua chave da NewsAPI no arquivo `data/sources.py`.

3. Execute:
    ```
    python main.py
    ```

## Expansão

- Adicione novos módulos de coleta em `data/sources.py`
- Implemente análises mais complexas em `core/threat_analyzer.py`
- Crie interfaces alternativas em `interface/`