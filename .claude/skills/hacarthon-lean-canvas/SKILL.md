---
name: hacarthon-lean-canvas
description: Use esta skill para preencher o Lean Canvas da solução escolhida. Cobre os 9 blocos do modelo de negócio em formato enxuto, com foco especial no bloco que mais reprova no pitch (modelo de negócio para solução open-source/bem público). Entrega o canvas completo e mapeia cada bloco ao elemento correspondente do pitch e da ideação.
---

# Lean Canvas — modelo de negócio em 9 blocos

## Por que usar

O pitch do haCARthon exige obrigatoriamente um **modelo de negócio**. É o
campo onde mais times travam ou dão respostas vagas que derrubam a nota.
Para soluções open-source e de bem público digital — como exige o edital —
o modelo de negócio não é intuitivo e precisa ser pensado com cuidado.

O Lean Canvas também é a base para responder à pergunta mais frequente da
banca: *"Quem paga por isso? Quem mantém?"*

## Quando usar

Depois de `hacarthon-convergencia` (ideia definida) e idealmente depois de
`hacarthon-value-proposition` (dores/ganhos mapeados). Pode rodar em paralelo
com `hacarthon-user-journey`. O canvas gerado alimenta diretamente o slide
de modelo de negócio do `hacarthon-pitch`.

## Leitura prévia

- `dados/raimundo-research.md` — para os blocos de segmento e canais
- Solução descrita na conversa ou em `hacarthon-convergencia`

---

## Os 9 blocos do Lean Canvas

### Bloco 1 — Problema

Os **3 problemas principais** que a solução resolve, em ordem de prioridade.
Não é a lista completa de dores — são os 3 que a solução resolve de verdade.

Usar os gargalos oficiais do Desafio 1 como referência:
- Exclusão digital e técnica
- Ciclo de retificações infinitas
- Ruído na comunicação Estado-produtor

**Alternativas existentes:** o que o Seu Raimundo faz hoje para tentar
resolver cada problema (ex: contratar despachante, pedir ajuda a vizinho,
deixar o CAR irregular). Isso também será útil na banca.

---

### Bloco 2 — Segmentos de Clientes

Quem é o usuário primário e quem é o usuário secundário?

**Primário:** Pequenos e médios produtores rurais — perfil Seu Raimundo.
Especificar se houver segmentação mais fina (ex: produtores sem acesso
a internet, produtores em processo de retificação, etc.)

**Secundário:** Analistas dos OEMAs — perfil Luana. A solução pode facilitar
também o trabalho dela, reduzindo o ciclo de retificações.

**Adotantes iniciais (Early Adopters):** Qual subgrupo do público primário
adotaria primeiro? Ex: produtores que já tentaram fazer o CAR e trancaram,
produtores com crédito rural bloqueado por CAR irregular.

---

### Bloco 3 — Proposta de Valor Única

Uma frase que diz o que a solução faz, para quem, e por que é diferente.
Deve ser clara o suficiente para que alguém que nunca ouviu falar do CAR
entenda o valor.

**Formato sugerido:**
`[Verbo de ação] + [resultado concreto] + [para quem] + [sem o obstáculo central]`

Ex: "Permite que o pequeno produtor rural declare e corrija o CAR pelo
celular, em linguagem simples, sem precisar de despachante ou técnico."

Este bloco alimenta diretamente a frase-ouro da skill `hacarthon-narrativa`.

---

### Bloco 4 — Solução

Os **3 recursos principais** da solução — não o produto inteiro, mas os
3 elementos que diretamente aliviam os 3 problemas do Bloco 1.

Formato: `[Problema que resolve] → [Recurso da solução]`

Ser honesto: se a solução for um protótipo/wireframe, descrever o que o
protótipo demonstra — não o software final hipotético.

---

### Bloco 5 — Canais

Como o Seu Raimundo vai descobrir e acessar a solução?

Este bloco é estratégico para o haCARthon porque o produtor rural
**não procura soluções no app store** nem em sites governamentais por conta
própria. Os canais precisam ser onde ele já está:

Canais a considerar (baseados no perfil oficial das personas):
- **WhatsApp** — canal de maior confiança e uso
- **Sindicatos rurais e cooperativas** — intermediários de confiança
- **EMATER / extensionistas agrícolas** — já têm acesso presencial ao produtor
- **Gerentes de banco rural** — ponte natural via crédito rural
- **Rádio rural** — ainda presente em muitas regiões
- **TikTok** — crescente entre produtores mais jovens

Para cada canal: descrever como a solução chegaria ao produtor por ele.

---

### Bloco 6 — Estrutura de Custos

O que custa para construir, manter e operar a solução?

Para soluções open-source de bem público digital, os custos típicos são:
- Infraestrutura de hospedagem / servidores
- Manutenção e atualização do código
- Onboarding e suporte ao produtor
- Atualização dos dados abertos que a solução consome

**Custo mais crítico a declarar:** manutenção contínua. Soluções open-source
sem financiamento garantido morrem. Nomear isso honestamente é mais forte
do que fingir que não existe.

---

### Bloco 7 — Fontes de Receita

**Este é o bloco mais difícil para soluções open-source / bem público digital.**

Opções defensáveis para este contexto (escolher a mais coerente com a solução):

**Opção A — Financiamento público direto**
> Custeada pelo governo federal (MAPA, IBAMA, ou estados via OEMAs) como
> infraestrutura pública digital, similar ao modelo do próprio SICAR.
> Argumento: o CAR é obrigação do Estado — ferramentas que ampliam sua
> eficácia são investimento público, não produto comercial.

**Opção B — Financiamento por doador / organização internacional**
> Modelo de organizações como a própria FBDS (co-organizadora do haCARthon),
> BID, Banco Mundial, ou fundações focadas em preservação ambiental.
> Argumento: o impacto ambiental do CAR bem-feito tem valor mensurável para
> financiadores de conservação.

**Opção C — Freemium com camada básica gratuita**
> Produtores individuais usam de graça (camada pública); cooperativas,
> sindicatos ou bancos rurais pagam por funcionalidades de gestão coletiva
> ou análise em escala.
> Argumento: quem tem interesse econômico na regularização do CAR
> (cooperativas, bancos rurais) pode financiar o acesso de quem não tem.

**Opção D — Modelo de serviço gerenciado por estados**
> Os estados (OEMAs) contratam a solução como serviço gerenciado, pois
> ela reduz a carga de trabalho de analistas como a Luana.
> Argumento: cada CAR irregular que chega ao OEMA custa tempo de analista —
> a solução é economia operacional para o estado.

**Instrução:** Escolher a opção mais coerente com o que a solução é na
prática. Combinar opções é permitido (ex: A + C). Registrar também
**quem não paga**: o produtor não deve pagar diretamente, pois isso viola
o princípio de acesso universal que o edital valoriza.

---

### Bloco 8 — Métricas-Chave

Como saber se a solução está funcionando? Listar 3-5 métricas concretas
e mensuráveis (não vagas como "satisfação do usuário"):

Sugestões contextuais:
- Número de declarações CAR iniciadas via solução
- Taxa de conclusão (começaram vs. enviaram com sucesso)
- Taxa de rejeição pelo OEMA (comparada à média atual sem a solução)
- Tempo médio para completar uma declaração (vs. processo atual)
- Número de produtores que fizeram o CAR sem intermediário pago

Para o pitch: escolher **1 métrica de impacto** que possa ser projetada.
Ex: "Se 10% dos CARs irregulares usassem a solução, seriam X produtores
regularizados por ano."

---

### Bloco 9 — Vantagem Injusta

O que a solução tem que é difícil ou impossível de copiar no curto prazo?

Para soluções open-source, a vantagem injusta raramente é o código. Pode ser:
- **Dado proprietário:** acesso a dados que outros não têm (ex: integração
  com base do SIGEF que outros não foram buscar)
- **Rede de confiança:** parceria com cooperativas ou EMATER que distribui
  a solução por canais que um app genérico não alcança
- **Design de linguagem:** vocabulário e fluxo construídos com o produtor
  real (dado de `raimundo-research.md`) — difícil de replicar sem pesquisa
- **Contexto normativo:** solução construída sobre os dados do CAR
  especificamente, não adaptada de outra coisa

**Este bloco alimenta a âncora de inovação da skill `hacarthon-narrativa`.**

---

## Entrega do canvas

Produzir o canvas completo em formato markdown, com todos os 9 blocos
preenchidos e as conexões com as demais skills sinalizadas:

```markdown
## Lean Canvas — [Nome da solução]

| Bloco | Conteúdo | Conecta com |
|-------|----------|-------------|
| 1. Problema | [3 problemas] | Pitch: slide Problema; Ideação: campo Problema |
| 2. Segmentos | [primário + early adopter] | Ideação: campo Público-alvo |
| 3. Proposta de valor | [frase única] | Narrativa: frase-ouro |
| 4. Solução | [3 recursos] | Pitch: slide Como funciona |
| 5. Canais | [como chega ao Raimundo] | Banca: pergunta de adoção |
| 6. Custos | [estrutura] | Banca: pergunta de sustentabilidade |
| 7. Receita | [modelo escolhido + justificativa] | Pitch: slide Modelo de negócio |
| 8. Métricas | [3-5 métricas + 1 de impacto] | Ideação: campo Impacto |
| 9. Vantagem injusta | [o que não é copiável] | Narrativa: âncora de inovação |
```

## Cuidados

- O bloco 7 (Receita) é o mais importante para o pitch e o mais cobrado
  na banca. Não escrever "gratuito" sem explicar quem financia. "Gratuito
  para o produtor, custeado por X" é uma resposta defensável.
- O bloco 9 (Vantagem injusta) não pode ser "somos open-source" — todo
  participante do haCARthon é obrigado a ser open-source. Precisa ser
  algo específico desta solução.
- Métricas vagas ("mais produtores regularizados") não passam pela banca.
  Toda métrica deve ter um denominador claro: em quanto tempo, em qual
  região, comparado com qual baseline.
- Se o time não souber responder o bloco 7, parar aqui e resolver antes
  de continuar — o pitch sem modelo de negócio defensável é eliminado
  pelo critério de relevância.
