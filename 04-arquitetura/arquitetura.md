# Arquitetura — a Terra Comum

> O backend não é demonstrado no protótipo — é contado no pitch. O vídeo mostra só
> o Compadre. Este documento descreve a arquitetura e dá as explicações (técnica e
> simples) prontas para o pitch.

---

## Explicação simples (para o pitch e para o produtor)

**A ontologia é um mapa de significados.** Escreve, de forma organizada, tudo o que
existe no mundo do CAR e como cada coisa se liga à outra: o que é uma Área de
Preservação, o que é Reserva Legal, que um rio exige uma faixa de mata do lado, que
sem o CAR em dia não se acessa crédito. É como um quadro com todas as regras do
Código Florestal ligadas por setas. O computador passa a "entender" esse mundo, não
só guardar dados soltos.

**A camada semântica é a tradutora.** Fica entre a montanha de regras técnicas e a
pessoa do outro lado. Pega o que está em "idioma de governo" e devolve na língua de
quem vive no campo — e faz o caminho de volta também.

**Juntas:** a ontologia é o **conhecimento** (sabe o que cada coisa significa); a
camada semântica é a **conversa** (usa esse conhecimento para falar com cada um na
língua certa). Uma sabe a regra, a outra explica a regra.

---

## A pilha em camadas

```
        Compadre (agente, WhatsApp)              ← a cara (vídeo)
                  ▲
   Terra Comum (ontologia + semântica + Agent Hub) ← o motor (pitch)
                  ▲
                  │
        Camada Semântica (metrics layer — conceitos de negócio)
                  ▲
        Knowledge Graph + Ontologia do CAR (RDF/OWL)
                  ▲
        Normalização (ETL) + PostGIS
                  ▲
   ┌──────────────┼──────────────┬──────────────┐
  RER          SIGEF        MapBiomas       Legislação
(PostGIS,
 registro,
 fundação)
```

Da camada semântica saem **dois consumos**:
- **BI headless** — APIs analíticas (dashboards, portais, sistemas externos)
- **Agent Hub** — registro de agentes, skills, ferramentas MCP

Ambos consomem **conceitos já resolvidos** — não precisam saber o que é uma APP ou
um déficit de RL. A regra é definida **uma vez** na camada semântica; quando o
Código Florestal muda, todos os consumidores recebem o novo comportamento.

---

## O Agent Hub — o diferencial

Transforma uma aplicação fechada num **"sistema operacional" do domínio CAR**: um
protocolo aberto onde qualquer dev/órgão/pesquisador cria agentes que "entendem o
território", consumindo o grafo + a camada semântica + integrações externas.

```
name: auditor_app
description: identifica inconsistências de APP
tools:  [query_knowledge_graph, spatial_analysis]
rules:  [verificar APP declarada, comparar cobertura, gerar evidências]
output: parecer_tecnico
```

Por que importa: **agentes de IA são ruins com dados crus**. Com a camada
semântica, o agente trabalha sobre **conceitos** (Imóvel → possui APP → em bioma →
déficit de RL → risco), com respostas contextualizadas pelas regras e
**rastreáveis** — não um RAG só de texto.

Aposta de pitch: não é *"criar a IA que entende todo o agro"* (gigantesco). É
*"criar o protocolo aberto para que qualquer um crie agentes que entendem o
território rural brasileiro"*.

---

## O RER é a fundação, não o concorrente

O **RER** (`github.com/Rural-Environmental-Registry/core`) é o DPG do governo para
**registro/gestão** do CAR — Spring Boot, Vue, PostgreSQL/PostGIS, GeoServer,
Keycloak; REST API. **Não tem ontologia, camada semântica nem agentes** — que é
exatamente a nossa camada.

- Estamos em camadas diferentes: o RER é **transacional** (registro, PostGIS); a
  Terra Comum é **semântica/inteligência** em cima. O RER é uma das fontes/fundação.
- **Buildável:** o RER é open-source e self-hostável (Docker Compose) com REST API —
  dá para subir uma instância, carregar dados de teste e o agente ler/escrever de
  verdade contra ela.
- **Distinção honesta:** instância própria do RER ≠ CAR nacional ao vivo. Claim:
  *"construído sobre o RER open-source"* (demo), não *"consultamos o sistema
  nacional por CPF"* (roadmap).
- **Enquadramento:** *"O RER é o corpo; a Terra Comum é a linguagem e a inteligência."*

---

## Validação externa (verificável)

- **Não há implementação pública de ontologia para o CAR** — somos os primeiros.
- **Embrapa tem os ativos de base:** OntoAgroHidro, GTermos/Agrotermos, alinhamento
  ao **AGROVOC** (FAO). Reusar/alinhar = história open-source sólida.
- **Referências maduras:** AgroPortal, AgroLD (Agronomic Linked Data).
