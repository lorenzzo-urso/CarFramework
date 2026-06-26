---
name: hacarthon-ideacao
description: Use esta skill depois que o time já escolheu uma única ideia de solução para o Desafio 1 do haCARthon. Gera um rascunho qualificado das respostas da entrega obrigatória de Ideação, com duas versões por campo (curta e expandida), âncora obrigatória em dados abertos, benefícios individuais e coletivos separados, gancho para o protótipo, e autoavaliação final no olhar do jurado.
---

# Ideação — primeira entrega obrigatória do haCARthon

## Quando usar

Depois que o time já decidiu qual ideia seguir (geralmente após usar a skill
`hacarthon-convergencia`, ou se o time já chegou com a ideia pronta).

## O que esta entrega exige (fonte: Guia do Participante, pág. 5)

A plataforma de entrega pede respostas para os seguintes temas:
**problema, solução, público-alvo, impacto, viabilidade, tempo de implementação
e benefícios.**

As perguntas exatas só aparecem na plataforma no momento da submissão — trate
a lista acima como os temas certos a cobrir. Ao entregar, ajuste a redação ao
texto exato de cada pergunta.

## Os 4 critérios de avaliação (nota 1 a 10 cada)

Cada resposta gerada deve ser escrita para pontuar bem nestes critérios:

1. **Pertinência temática** — responde diretamente ao Desafio 1 (simplificar
   declaração/retificação do CAR, usando dados abertos, cumprindo o Código
   Florestal, gerando benefícios individuais e coletivos)
2. **Relevância do problema** — o problema descrito é real, urgente e afeta
   de forma concreta o produtor rural
3. **Usabilidade e design** — a solução é de fácil compreensão, acesso
   simplificado, linguagem acessível; o próprio texto da ideação deve modelar
   essa clareza
4. **Inovação e criatividade** — a abordagem é diferente do que já existe ou
   do que o jurado esperaria como resposta óbvia

Em caso de empate na avaliação final, prevalece o critério 4.

## Processo

### Passo 1 — Ler os dados reais do produtor

Leia `dados/raimundo-research.md`. Se o arquivo tiver dados preenchidos, use
trechos e fatos concretos de lá em vez de generalidades — especialmente para
o campo Problema e para o gancho do vídeo.

Se o arquivo ainda não tiver dados reais, avise o usuário explicitamente no
início da resposta e prossiga com a persona genérica do Seu Raimundo. Marque
com `[DADO A CONFIRMAR]` os pontos que dependerão da entrevista real.

### Passo 2 — Confirmar a ideia escolhida

Antes de gerar, peça ou confirme em uma frase: qual é a ideia que o time
decidiu seguir? Não gere rascunho sem isso.

### Passo 3 — Gerar os 7 campos com duas versões cada

Para cada campo, entregue **duas versões**:
- **Curta** (~150 caracteres) — para formulários com limite de caracteres
- **Expandida** (~400-600 caracteres) — para campos livres ou caixas maiores

Ao final de cada campo, adicione uma linha de avaliação no seguinte formato:
> `[Jurado] Critério principal: X | Nota estimada atual: N/10 | Para subir: ...`

---

#### Campo 1 — Problema

Descreva a dor concreta do produtor rural com o CAR. Prefira um caso
específico (real, se disponível em `raimundo-research.md`) a uma generalização.
Conecte com pelo menos uma destas dificuldades reais:
- Dificuldade de entender os limites técnicos do imóvel (APP, Reserva Legal)
- Complexidade da plataforma do SICAR
- Dependência de terceiros pagos (técnicos, despachantes) para fazer o CAR
- Risco de multa ou bloqueio de crédito por CAR irregular

> `[Jurado] Critério principal: Relevância do problema | Nota estimada atual: ?/10 | Para subir: incluir dado real do produtor entrevistado`

---

#### Campo 2 — Solução

O que a solução é, em 2-3 frases sem jargão técnico. O leitor precisa entender
o que ela faz sem saber o que é CAR, SIG ou Código Florestal.

Ao final da versão expandida, inclua obrigatoriamente este gancho:
> **No vídeo de protótipo, o jurado verá: ___**
(preencher com o que será demonstrado — telas, maquete, fluxo)

> `[Jurado] Critério principal: Pertinência temática + Inovação | Nota estimada atual: ?/10 | Para subir: deixar mais claro o diferencial vs. o processo atual do SICAR`

---

#### Campo 3 — Público-alvo

Pequenos e médios produtores rurais. Se o time tiver segmentação adicional
(região, tipo de propriedade, situação cadastral), inclua — isso sobe a nota
de relevância.

> `[Jurado] Critério principal: Relevância do problema | Nota estimada atual: ?/10 | Para subir: quantificar o público (ex: "X milhões de imóveis com CAR pendente no Brasil")`

---

#### Campo 4 — Impacto

**Obrigatório: separar em dois parágrafos.**

- **Individual** — o que muda para o Seu Raimundo: menos risco de multa ou
  embargo, acesso a crédito rural, menos dependência de terceiro pago, menos
  tempo perdido
- **Coletivo** — o que muda para o sistema: mais imóveis regularizados no
  SICAR, dados de CAR mais confiáveis para gestão ambiental pública, redução
  do desmatamento por regularização facilitada

O enunciado do Desafio 1 cita explicitamente "benefícios individuais e
coletivos" — cobrir os dois é critério de pertinência temática.

> `[Jurado] Critério principal: Pertinência temática + Relevância | Nota estimada atual: ?/10 | Para subir: incluir o impacto coletivo com pelo menos uma métrica ou referência (ex: total de imóveis pendentes no SICAR)`

---

#### Campo 5 — Viabilidade

**Âncora de dados abertos obrigatória:** nomeie pelo menos um dataset real
que a solução usaria. Exemplos disponíveis no ecossistema do CAR:

| Dataset | O que oferece | Onde acessar |
|---|---|---|
| SICAR / RER (via SNIF) | Dados públicos de CAR por estado | snif.florestal.gov.br |
| MapBiomas | Cobertura e uso do solo atualizado | mapbiomas.org |
| SIGEF / INCRA | Georreferenciamento de imóveis rurais | sigef.incra.gov.br |
| IBGE Malha Rural | Limites de municípios e territórios | ibge.gov.br |
| Código Florestal Digital | Parâmetros legais de APP/RL por bioma | florestal.gov.br |

Descreva o que já existe (não precisa ser construído do zero) e o que a solução
adiciona em cima disso. Seja honesto sobre o que é mockup/conceito vs. o que
poderia funcionar de verdade — o edital aceita protótipo conceitual.

Lembre: a solução deve ser de código aberto (exigência do edital).

> `[Jurado] Critério principal: Pertinência temática + Inovação | Nota estimada atual: ?/10 | Para subir: citar o dataset específico pelo nome oficial, não apenas "dados abertos"`

---

#### Campo 6 — Tempo de implementação

Estimativa realista em três horizontes:
- **Hackathon (agora):** o que o protótipo/vídeo vai demonstrar
- **Piloto (3-6 meses):** o mínimo para testar com um grupo real de produtores
- **Escala (12-24 meses):** integração com SICAR e adoção mais ampla

Esses três horizontes mostram que o time pensou além do hackathon sem
prometer o impossível.

> `[Jurado] Critério principal: Relevância + Inovação | Nota estimada atual: ?/10 | Para subir: ancorar o piloto em um parceiro concreto (ex: cooperativa, EMATER, sindicato rural)`

---

#### Campo 7 — Benefícios

Síntese final em um parágrafo. Une impacto + viabilidade em uma resposta à
pergunta: "por que vale a pena construir isso?". Deve citar:
- O benefício principal para o produtor (concreto, não abstrato)
- O benefício para o sistema público (MAPA, estados, IBAMA)
- A natureza open-source como multiplicador de impacto

> `[Jurado] Critério principal: todos os 4 | Nota estimada atual: ?/10 | Para subir: este campo é o resumo executivo — se o jurado ler só um campo, deve ser este`

---

### Passo 4 — Autoavaliação no olhar do jurado

Ao final do rascunho, gere obrigatoriamente esta tabela:

| Critério | Nota estimada | Ponto mais forte | Ponto mais fraco |
|---|---|---|---|
| 1. Pertinência temática | /10 | | |
| 2. Relevância do problema | /10 | | |
| 3. Usabilidade e design | /10 | | |
| 4. Inovação e criatividade | /10 | | |
| **Média estimada** | **/10** | | |

Depois da tabela, liste no máximo 3 ações concretas para o time elevar a
média antes de submeter.

### Passo 5 — Lista de lacunas

Liste os pontos onde o rascunho está fraco por falta de dado real:
- Estatísticas que precisam ser confirmadas
- Dados do produtor entrevistado ainda não preenchidos
- Nomes de parceiros ou datasets específicos a validar

## Cuidados

- Não invente estatísticas, números ou citações atribuídas ao produtor real.
  Use `[NÚMERO A CONFIRMAR]` se necessário.
- Não prometa funcionalidades de software completo se a entrega real será
  um protótipo conceitual — mantenha a viabilidade coerente com o que será
  demonstrado no vídeo.
- A linguagem das respostas deve ser simples e direta — o critério de
  usabilidade avalia a solução, mas o texto da ideação deve modelar essa
  mesma clareza para o jurado confiar que o time entendeu o usuário.
- O gancho "No vídeo, o jurado verá:" no Campo 2 é obrigatório — ele garante
  que ideação e protótipo contam a mesma história.
- Se o time ainda não tiver acesso à plataforma de submissão, avise que os
  campos gerados aqui são rascunhos e deverão ser ajustados ao texto exato
  das perguntas da plataforma no momento da entrega.
