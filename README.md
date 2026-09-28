# Reclame Aqui Scraper e API de reputação de empresas

Consulte a **reputação de qualquer empresa no Reclame Aqui** de forma automática: nota RA, selo RA1000, número de reclamações, índice de solução, "voltaria a fazer negócio", tempo médio de resposta, histórico em 5 períodos e os principais problemas reclamados.

➡️ **Ferramenta pronta para usar (sem programar):** [Reclame Aqui Scraper na Apify](https://apify.com/ing-karlen/reclame-aqui-company-reputation)

Este repositório traz **exemplos de uso** e um **conjunto de dados de exemplo**.

## Exemplo real: bancos e marketplaces (setembro de 2026)

| Empresa | Selo | Nota RA | Reclamações (6 meses) | Resolvidas % | Resposta média (h) |
|---|---|---|---|---|---|
| Nubank | RA1000 | 8.7 | 56.987 | 93,2 | 98 |
| PicPay | RA1000 | 8.6 | 16.981 | 90,6 | 182 |
| Banco Itaú | ÓTIMO | 8.1 | 19.160 | 85,1 | 160 |
| Mercado Pago | ÓTIMO | 8.0 | 54.217 | 80,4 | 267 |
| Banco do Brasil | BOM | 7.5 | 26.625 | 74,9 | 219 |
| Banco Santander | RUIM | 5.7 | 33.290 | 52,0 | 170 |
| Magazine Luiza | RA1000 | 8.2 | 56.890 | 90,7 | 301 |
| Amazon | ÓTIMO | 8.1 | 124.798 | 86,3 | 487 |
| Mercado Livre | BOM | 7.8 | 194.481 | 78,5 | 264 |
| Shopee | REGULAR | 6.8 | 137.658 | 67,1 | 460 |

Arquivo completo com 19 empresas: [`data/reputacao-empresas-2026-09.csv`](data/reputacao-empresas-2026-09.csv).

## Para que serve

- **Comparar concorrentes** do seu setor toda semana.
- **Avaliar fornecedores e parceiros** antes de fechar contrato.
- **Qualificar leads**: empresas com atendimento ruim precisam de ajuda; empresas RA1000 são bons parceiros.
- **Pesquisa de mercado e jornalismo**: ranking de um setor inteiro.
- **Painéis de reputação** no Google Sheets, Looker Studio ou Power BI.

## Como usar

1. Crie uma conta gratuita na [Apify](https://apify.com) (inclui créditos mensais grátis).
2. Abra o [Reclame Aqui Scraper](https://apify.com/ing-karlen/reclame-aqui-company-reputation) e informe as empresas como aparecem na URL. Por exemplo, `nubank` em `reclameaqui.com.br/empresa/nubank/`.
3. Baixe o resultado em Excel, CSV ou JSON, ou use a API.

### Python

Veja [`examples/python_exemplo.py`](examples/python_exemplo.py):

```python
from apify_client import ApifyClient

client = ApifyClient("SEU_TOKEN_APIFY")
run = client.actor("ing-karlen/reclame-aqui-company-reputation").call(
    run_input={"companies": ["nubank", "itau", "mercado-livre"]}
)
for empresa in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(empresa["name"], empresa["reputationScore"], empresa["solvedRatePct"])
```

### Node.js

Veja [`examples/node_exemplo.mjs`](examples/node_exemplo.mjs).

### Sem código

Funciona com **Make, Zapier, n8n e Google Sheets** pelas integrações da Apify. Também pode ser usado por agentes de IA via o **servidor MCP da Apify**.

## Preço

US$0,01 por empresa encontrada. Empresas não encontradas não são cobradas.

## Privacidade

Somente dados públicos no nível da empresa. **Nenhum texto de reclamação nem dado pessoal de consumidores** é coletado (LGPD). As páginas que o `robots.txt` do site não permite, como a busca, não são acessadas.

---

**English:** examples and a sample dataset for the [Reclame Aqui Scraper on Apify](https://apify.com/ing-karlen/reclame-aqui-company-reputation). It returns company reputation metrics from reclameaqui.com.br (RA score, complaints, solved rate, response time, 5 periods, top problems) for US$0.01 per company.
