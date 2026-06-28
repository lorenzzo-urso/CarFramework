# CarFramework — Terra Comum / Compadre

> Repositório da **Equipe 229** no **haCARthon — Desafio 1** (MGI · FBDS · ENAP · Impact Hub Brasil).
> Código aberto. Solução: simplificar a declaração e retificação do CAR para o produtor rural.

---

## A solução em uma frase

> **Terra Comum** (camada semântica aberta do território — ontologia + Agent Hub sobre o RER
> open-source) + **Compadre** (agente que ajuda o produtor a resolver o CAR pelo WhatsApp).
> Princípio: **esconde a máquina pesada, ensina só o essencial.**

- **A cara (vídeo):** o Compadre — Seu Raimundo conversa pelo WhatsApp, entende o que fazer.
- **O motor (pitch):** a Terra Comum — ontologia do Código Florestal + Agent Hub que permite
  criar N agentes sobre o mesmo modelo de conhecimento.

---

## PoC — o que está funcionando hoje

O PoC roda localmente com backend Python + FastAPI e frontend HTML/JS puro.

```
poc/web/        →  interface WhatsApp do Compadre (chat + bastidores em tempo real)
poc/backend/    →  API /conversa → ontologia RDF + análise geoespacial + LLM
poc/contracts/  →  contrato JSON entre frontend e backend
```

**Para rodar:** execute `iniciar.bat` na raiz (abre backend na porta 8000 e frontend na 3000).

### O que o PoC demonstra

| Funcionalidade | Status |
|---|---|
| Chat WhatsApp simulado com o Compadre | ✅ |
| Consulta de pendências do CAR com rastreabilidade (ontologia → regra citada) | ✅ |
| Análise de APP por geometria real (GeoPackage, EPSG:32723) | ✅ |
| LLM traduz dados técnicos para linguagem simples (Haiku 4.5) | ✅ |
| Delegação Compadre → Professor para perguntas conceituais | ✅ |
| Agente Professor (explica o Código Florestal em linguagem livre) | ✅ |
| Vitrine do Agent Hub (7 agentes, 2 operacionais) | ✅ |
| Fallback offline (resposta empacotada, sem backend) | ✅ |

### Agent Hub — manifests disponíveis

| Agente | Personas | Status |
|---|---|---|
| `compadre` | Produtor rural | Operacional |
| `professor` | Produtor, estudante, técnico | Operacional |
| `auditor` | Analistas dos OEMAs | Demonstrativo |
| `territorial` | Governo, prefeituras | Demonstrativo |
| `credito` | Bancos, cooperativas | Demonstrativo |
| `oportunidades` | Produtor, cooperativa de crédito | Demonstrativo |
| `comunicador` | Governo (OEMAs, MDA) | Demonstrativo |

Trocar o manifesto muda o agente — o motor (Terra Comum) é o mesmo.

---

## Como navegar

| Pasta | O que tem |
|---|---|
| [`01-produto/`](01-produto/) | O que é a solução, por que cabe no Desafio 1, narrativa |
| [`02-pesquisa/`](02-pesquisa/) | Persona Seu Raimundo + 3 gargalos + problema |
| [`03-frameworks/`](03-frameworks/) | Value Proposition, Jornada, Lean Canvas |
| [`04-arquitetura/`](04-arquitetura/) | Arquitetura em camadas + viabilidade |
| [`05-entregas/`](05-entregas/) | As 3 entregas obrigatórias + PRD do PoC |
| [`06-referencias/`](06-referencias/) | Bases de dados abertas, resumo do edital, riscos |
| [`poc/`](poc/) | Código do PoC — backend, frontend, contratos, agentes |

**Comece por:** [`01-produto/produto.md`](01-produto/produto.md).

---

## Estado das 3 entregas obrigatórias

| Entrega | Formato | Status |
|---|---|---|
| 1. Ideação | Formulário na plataforma (10 campos) | ✅ Versão oficial da equipe — [`05-entregas/1-ideacao-equipe.md`](05-entregas/1-ideacao-equipe.md) |
| 2. Protótipo | Vídeo ≤2min no YouTube | 🟡 Roteiro pronto — [`05-entregas/2-roteiro-video.md`](05-entregas/2-roteiro-video.md) · falta gravar e postar |
| 3. Pitch | PDF + áudio na plataforma | 🟡 Script pronto — [`05-entregas/3-pitch.md`](05-entregas/3-pitch.md) · falta slides PDF + áudio |

---

## Pendências da equipe (ação humana)

Ver detalhe em [`06-referencias/riscos-e-pendencias.md`](06-referencias/riscos-e-pendencias.md).

- 🔴 Gravar e postar o vídeo no YouTube (≤2min)
- 🔴 Montar slides do pitch em PDF
- 🔴 Gravar áudio do pitch dentro da plataforma
- 🟡 Confirmar limite do vídeo (2 ou 3 min) com a organização
- 🟡 Confirmar parceiro do piloto (CATI-SP ou cooperativa)

---

## Bases de dados abertas utilizadas

SICAR · SIGEF (INCRA) · MapBiomas · base SFB de Uso do Solo · RER open-source (governo federal)

---

## Nota sobre dados e open-source

Solução obrigatoriamente open-source (requisito do edital). Usa a persona oficial **Seu Raimundo**
(fictícia, do Briefing). Insights de produtor real entram anonimizados. Nenhum dado pessoal
identificável, credencial ou `.env` deve ser adicionado a este repositório.

Instância do RER: self-hostável via Docker. Nunca "consultamos o sistema nacional por CPF".
