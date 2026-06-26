# Viabilidade — honesta, por horizonte

> O edital aceita protótipo conceitual — não exige software funcional. Este
> documento mantém a viabilidade honesta com o que será demonstrado.

---

## Três horizontes

### Horizonte 1 — Construível agora (hackathon)
| Componente | O que funciona | O que é mockado no vídeo |
|---|---|---|
| Interface (web mobile simulando WhatsApp) | Telas navegáveis reais | — |
| Status do CAR | Consulta na consulta pública pelo nº do CAR | Lookup automático por CPF (sem API) |
| SIGEF | API pública (se o imóvel for certificado) | Pequeno produtor às vezes não tem certificação |
| MapBiomas | Dado pré-computado para a região da demo | Consulta ao vivo por polígono (exige GEE) |
| Banco de programas/editais | JSON estático com casos reais + matching por regras | Atualização dinâmica |
| Camada semântica (tradução) | Chamada a LLM — rápida e de qualidade | — |
| Ontologia/grafo mínimos | Buildável (domínio fechado) | — |
| RER | Instância própria via Docker, dados de teste | Sistema nacional ao vivo |

### Horizonte 2 — Com parceria/apoio (meses)
Integração com o CAR nacional; RER com autenticação institucional; MapBiomas via
GEE em tempo real; pipeline de editais; WhatsApp Business API; inferência ML (exige
dados históricos de parceiro).

### Horizonte 3 — Escala
Agent Hub aberto a terceiros, inferência preditiva, primeiras assinaturas B2B/B2G.

---

## Disciplina de protótipo (o risco a controlar)

Não se constrói um Agent Hub funcional em 2,5 dias — e não se deve tentar. O vídeo
mostra o **Compadre (Raimundo)**; a arquitetura entra como **diagrama no pitch**.

Prioridade de construção, se houver tempo de código:
1. Ontologia + grafo do CAR mínimos (o substrato)
2. 1-2 agentes sobre o grafo (Produtor + Auditor)
3. Um painel/API simples consumindo a mesma camada (prova do "serving")

> ⚠️ **Nunca mostrar SPARQL, triplestore ou diagrama de arquitetura no vídeo** — o
> critério de usabilidade é julgado pela experiência do Raimundo.

---

## Componentes por viabilidade (resumo)

| Componente | Hackathon | Produção |
|---|---|---|
| Interface web/WhatsApp | ✅ Alta | 🟡 Média (aprovação Meta) |
| SIGEF | ✅ Alta | ✅ Alta |
| MapBiomas (GEE) | 🟡 Média | 🟡 Média |
| SICAR (dados diretos) | 🔴 Baixa (sem API) | 🔴 Baixa |
| RER (instância própria) | 🟡 Média | ✅ Alta |
| Ontologia + camada semântica | ✅ Alta | ✅ Alta |
| BI headless | 🟡 Média | ✅ Alta |
| Agent Hub | 🟡 Média (conceito) | ✅ Alta |
| Inferência por regras (v1) | ✅ Alta | ✅ Alta |
| Inferência ML (v2) | 🔴 (hackathon) | 🟡 Média (precisa de dados) |
