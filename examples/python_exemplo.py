"""Compara a reputação de empresas no Reclame Aqui e salva um CSV.

Requisitos: pip install apify-client
Uso: APIFY_TOKEN=seu_token python python_exemplo.py
"""
import csv
import os

from apify_client import ApifyClient

EMPRESAS = ["nubank", "itau", "bradesco", "banco-do-brasil", "santander", "picpay"]

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("ing-karlen/reclame-aqui-company-reputation").call(
    run_input={"companies": EMPRESAS, "maxTags": 3}
)

linhas = [e for e in client.dataset(run["defaultDatasetId"]).iterate_items() if e.get("found")]
linhas.sort(key=lambda e: e["reputationScore"] or 0, reverse=True)

with open("ranking_reputacao.csv", "w", newline="", encoding="utf-8") as f:
    campos = ["name", "reputationStatus", "reputationScore", "complaints", "solvedRatePct", "avgResponseTimeHours"]
    w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
    w.writeheader()
    w.writerows(linhas)

for e in linhas:
    problema = e["topProblems"][0]["name"] if e.get("topProblems") else "-"
    print(f'{e["name"]:<25} {e["reputationStatus"]:<16} nota {e["reputationScore"]}  principal problema: {problema}')
