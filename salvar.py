import json
import os

def salvar_historias(titulo,texto):
    if os.path.exists("salvas.json"):
        with open("salvas.json", "r", encoding="utf-8") as arquivo:
            salvas = json.load(arquivo)
    else:
        salvas = []

    salvas.append({"titulo": titulo, "texto": texto})

    with open("salvas.json", "w", encoding="utf-8") as arquivo:
        json.dump(salvas, arquivo, ensure_ascii=False, indent=2)

def carregar_historias():
    if os.path.exists("salvas.json"):
        with open("salvas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    else:
        return []