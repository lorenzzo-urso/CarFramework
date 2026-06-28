# Terra Comum — visão do ecossistema

> Este documento cristaliza a concepção completa do projeto: o que foi
> construído no haCARthon, o que a arquitetura torna possível, e o horizonte
> de longo prazo. Serve como referência para pitch, captação e continuidade.

---

## O que existe hoje

O **Compadre** é um agente que ajuda o produtor rural a entender e corrigir
o CAR pelo WhatsApp. Ele faz isso raciocinando sobre a **Terra Comum** —
uma camada semântica aberta construída sobre o Registro Ambiental Rural
open-source (RER).

O Compadre não é o produto. É o primeiro agente que trafega na estrada.

### O que já funciona (PoC do haCARthon)

- **Análise própria de déficit de APP (P0-8):** o sistema calcula o problema
  a partir de dado aberto, sem autenticação no SICAR. Rodando sobre geometria
  real do GeoPackage SFB de MG (Alvinópolis, 41,7 ha): déficit de 4,19 ha de
  mata ciliar — descoberto, não apenas repetido.
- **Rastreabilidade (P0-7):** toda resposta cita a regra concreta vinda da
  ontologia (`car:FaixaAPP_ate10`, Lei 12.651/2012, Art. 4º, I, a). O LLM
  traduz a regra — nunca a inventa.
- **Separação evidência / interpretação:** o Compadre distingue "o que
  calculei com dados abertos" de "o que o governo diz". Isso resolve o medo
  central da persona (Seu Raimundo não quer sentir que está sendo autuado).
- **Agent Hub mínimo:** o Compadre é carregado por manifesto YAML — trocar
  o manifesto muda o agente sem mudar o código do loader.

---

## O diferencial real

### A regra vem do grafo, não do LLM

Qualquer chatbot de CAR que existe hoje ou vai existir amanhã é um LLM com
prompt. Quando a lei muda, o prompt fica errado silenciosamente.

Na Terra Comum, a lei está no grafo (`.ttl`). Quando muda, você muda um nó.
Todos os agentes que consomem aquele nó ficam corretos automaticamente.

### A análise é gerada, não raspada

O sistema não pergunta ao governo "você tem problema?". Ele calcula o problema
de forma independente, com dado aberto, sem autenticação. Isso inverte a
lógica: em vez de o produtor esperar a fiscalização descobrir, a plataforma
descobre antes.

Isso tem valor imediato em crédito rural, PSA, seguros, regularização
proativa — independente de qualquer parceria institucional.

### O Hub é infraestrutura, não produto

Qualquer cooperativa, OEMA, banco ou prefeitura pode escrever um manifesto
YAML e ter um agente especializado consumindo a mesma ontologia. O custo
marginal de cada novo agente é o custo de um manifesto — não de reimplementar
o conhecimento do Código Florestal.

---

## A arquitetura em camadas

```
FONTES DE DADOS
  públicas:  SICAR · MapBiomas · SIGEF · ANA · IBGE · SNIF
  privadas:  cooperativas · tradings · seguradoras · bancos
       |
       ↓  (normalização semântica)
       |
TERRA COMUM  ←  a camada que não existe hoje
  Ontologia do território  (APP · RL · biomas · CF · benefícios)
  Hub de agentes           (protocolo aberto · manifesto YAML)
  Análise própria          (geometria + regra + dado aberto)
       |
       ↓  (agentes especializados)
       |
AGENTES
  Compadre     →  produtor rural  (hoje)
  Auditor      →  OEMA / analista ambiental
  Crédito      →  banco / cooperativa
  Carbono      →  mercado voluntário · CRA · REDD+
  Territorial  →  governo · planejamento
  [N agentes]  →  qualquer manifesto
       |
       ↓  (canal agnóstico)
       |
CANAIS
  WhatsApp · Telegram · app de banco · portal · API · qualquer mensageiro
```

---

## O protocolo como bem público

O que estamos descrevendo é um **protocolo aberto de agentes especializados
sobre um grafo de conhecimento compartilhado**. A ontologia é o que garante
que todos os agentes falem a mesma língua, independente de quem os criou.

O paralelo mais próximo que existe hoje é o MCP (Model Context Protocol) da
Anthropic — que resolve o problema de "como um agente consome ferramentas e
fontes de dados de qualquer provedor, de forma padronizada". O que estamos
construindo é um MCP **especializado no território rural brasileiro**, onde a
ontologia do Código Florestal é o contrato que normaliza tudo.

### O que isso implica na prática

- Uma cooperativa escreve um agente de crédito rural. Ele já sabe o que é
  APP, RL, bioma e situação do CAR — sem reimplementar nada.
- Um banco cria um agente de avaliação de risco de imóvel rural. Consome
  os agentes da cooperativa como ferramenta.
- Uma prefeitura expõe dados de uso do solo via manifesto. Qualquer agente
  no Hub passa a enxergar aquele território.
- O Compadre roda no WhatsApp hoje. Amanhã roda no Telegram, no app do
  sindicato, no app do banco — o protocolo é agnóstico de canal.

---

## O crescimento da ontologia

A ontologia hoje modela o **Código Florestal**. O território rural tem
camadas de conhecimento que se sobrepõem e nenhuma delas conversa entre si:

| Fonte | O que tem | Status |
|---|---|---|
| SICAR / CAR | cadastros, polígonos, situação | integrado |
| SFB / SNIF | cobertura e uso do solo | integrado (MG) |
| MapBiomas | histórico 1985–hoje | planejado |
| SIGEF / INCRA | titularidade, georreferenciamento | planejado |
| ANA | recursos hídricos, outorgas | planejado |
| IBGE | socioeconômico do produtor | planejado |
| Mercado de carbono | CRA, REDD+, créditos voluntários | planejado |
| Cooperativas | dados de produção | privado / futuro |
| Tradings | rastreabilidade de cadeia | privado / futuro |
| Seguradoras | histórico de sinistros por região | privado / futuro |

Quando fontes privadas entram na camada semântica — mesmo que o dado bruto
continue privado, só a semântica seja pública — você cria algo que não
existe: **inteligência territorial combinada**.

---

## O princípio da evidência separada da interpretação

Um ponto de design que se provou crítico: a Terra Comum não é um tribunal.
Ela é um **intérprete de contexto**.

O sistema distingue:
- **O que encontrei** (evidência com dado aberto, rastreável, citable)
- **O que isso pode significar** (interpretação, com margem de incerteza)
- **O que você deve fazer** (orientação, nunca decreto)

Isso é importante porque a persona tem medo de fiscalização. E é correto
porque a análise usa dados abertos com limitações conhecidas (largura do
rio assumida, data do GeoPackage, etc.). A honestidade epistêmica é um
diferencial, não uma fraqueza.

---

## O teto

O teto real não é o CAR.

É qualquer decisão que dependa de entender um território: concessão de
crédito, precificação de carbono, licenciamento ambiental, seguro agrícola,
compra de terra, política pública de uso do solo.

A ontologia vira o sistema nervoso. Os agentes viram os órgãos. As fontes
de dados viram os sentidos.

**É infraestrutura cognitiva do território.**

---

## O risco honesto

O modelo só vira ecossistema se a ontologia for tratada como bem público
com governança clara: quem valida mudanças, quem resolve conflitos de
interpretação quando a lei muda. Sem isso, cada organização forca a
ontologia e o protocolo fragmenta.

Isso é um problema de governança, não de tecnologia. E é o mesmo problema
que o Linux, o OSM e o W3C já resolveram antes.

---

## Números

| Métrica | Valor |
|---|---|
| Imóveis no CAR | 8,2 milhões |
| Área mapeável | 7 milhões de km² |
| Crédito rural (Pronaf) | R$ 15 bilhões/ano |
| CARs pendentes ou com erro | estimativa: 30–40% |
| Custo de um novo agente | 1 manifesto YAML |
| Fontes de dado necessárias | já públicas e abertas |

---

## Frase

> "Não construímos um táxi. Construímos a estrada."

A diferença entre construir o Compadre e construir a Terra Comum é a
diferença entre resolver um problema e criar infraestrutura para que
qualquer um resolva o problema melhor do que nós.
