// Monitora a reputação de concorrentes no Reclame Aqui.
// Requisitos: npm install apify-client
// Uso: APIFY_TOKEN=seu_token node node_exemplo.mjs
import { ApifyClient } from 'apify-client';

const empresas = ['magazine-luiza-loja-online', 'mercado-livre', 'amazon', 'shopee', 'casas-bahia-loja-online'];

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('ing-karlen/reclame-aqui-company-reputation').call({ companies: empresas });
const { items } = await client.dataset(run.defaultDatasetId).listItems();

console.table(
    items
        .filter((e) => e.found)
        .map((e) => ({
            empresa: e.name,
            selo: e.reputationStatus,
            nota: e.reputationScore,
            reclamacoes: e.complaints,
            resolvidas: `${e.solvedRatePct}%`,
            respostaHoras: e.avgResponseTimeHours,
        })),
);
