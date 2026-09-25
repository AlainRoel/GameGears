import json
from pathlib import Path

ARQUIVO_JOGOS = Path(__file__).resolve().parent.parent / "jogos.json"


def carregar_jogos():
    if not ARQUIVO_JOGOS.exists():
        return []

    with open(ARQUIVO_JOGOS, "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []


def salvar_jogos(jogos):
    with open(ARQUIVO_JOGOS, "w", encoding="utf-8") as arquivo:
        json.dump(jogos, arquivo, ensure_ascii=False, indent=4)