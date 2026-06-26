# Lean Canvas — Terra Comum / Compadre

> Modelo de Bem Público Digital: o produto é a camada semântica aberta + Agent
> Hub; o Compadre é o agente produtor-facing. O produtor é usuário e fonte de
> dados, **nunca cliente pagante**.

---

## 1. Problema
1. **Comunicação** — notificação do órgão em linguagem técnica gera medo e paralisia
2. **Exclusão técnica** — produtor não consegue georreferenciar APP/RL sozinho
3. **Retificação** — ciclo de correções por dado autodeclarado errado

*Problema oculto (lado da oferta):* governo e cooperativas não têm inteligência
individualizada e preditiva sobre os 8,2 milhões de CARs — só agregados retrospectivos.

## 2. Segmentos
- **Primário (não paga):** pequeno/médio produtor — Seu Raimundo (fonte de dados)
- **Early adopter:** produtor com crédito bloqueado ou com notificação pendente
- **Cliente pagante A:** cooperativas de crédito / bancos rurais
- **Cliente pagante B:** governo — órgãos estaduais, MDA/MGI
- **Canal (não paga):** CATI / EMATER / sindicatos / devs / Embrapa

## 3. Proposta de valor única
> "Uma camada semântica aberta do território rural que transforma dados
> fragmentados em conhecimento operacional — onde o produtor, o governo e agentes
> de IA raciocinam sobre o mesmo modelo. O problema não é falta de informação; é
> falta de contexto."

## 4. Solução
- **A cara:** Compadre — tradução + pré-preenchimento + validação + painel de benefícios
- **O motor:** normalização → Knowledge Graph + ontologia → camada semântica →
  BI headless + Agent Hub (sobre o RER)

## 5. Canais
WhatsApp (porta de entrada) · CATI/EMATER · cooperativas/sindicatos (que também
pagam) · gerente de crédito rural · devs/Embrapa (via Hub). O canal B2B é o mesmo
que distribui ao produtor — quem paga tem interesse em espalhar.

## 6. Estrutura de custos
Infra cloud (compute geoespacial off-peak) · manutenção da ontologia quando
normas mudam · curadoria do banco de programas · suporte via parceiros (não equipe
própria) · API de LLM (baixo por transação).
*Custo crítico:* manutenção contínua da ontologia — o que mata projeto
open-source sem dono; por isso o Bloco 7 existe desde o dia 1.

## 7. Fontes de receita ⭐
Produtor nunca paga; núcleo open-source; vende-se **acesso à camada semântica /
agentes** (inferência derivada), não o dado bruto.
- **A — Cooperativas de crédito (B2B, principal):** assinatura da API/Agent Hub →
  carteira elegível, risco diluído, crédito verde mais qualificado. Recorrente.
- **B — Governo (B2G, por projeto/parceria):** agente territorial + APIs analíticas
  → priorizar intervenção, reduzir ciclo de retificação. Serviço gerenciado ou DPG.
- **C — Efeito-rede:** terceiros constroem agentes sobre a camada → mais uso, mais
  dados, melhor inferência.

*Por que não é "mais um dashboard":* o painel público existente mostra o que
aconteceu, agregado. Servimos conceitos resolvidos e inferência individualizada e
acionável — consumida igual por dashboard, app e agente.

## 8. Métricas-chave
- Declarações iniciadas via solução (por mês/região)
- Taxa de conclusão (iniciaram → enviaram) vs. abandono atual do SICAR
- **Taxa de rejeição pelo órgão** vs. baseline — métrica-chave do ciclo de retificação
- Tempo médio para completar vs. processo com despachante
- (B2B) Crédito verde originado via matching
- Agentes/consumidores ativos na plataforma

## 9. Vantagem injusta
Ser o **substrato aberto** (efeito-rede: quanto mais agentes consomem, mais vira
padrão) + a **inteligência acumulada** (só existe dentro do nosso modelo
semântico). Reforçada por: ontologia do CAR inédita (alinhável ao AGROVOC/Embrapa);
rede CATI/cooperativas; posicionamento DPG (sobre o RER); pioneirismo do Agent Hub.
