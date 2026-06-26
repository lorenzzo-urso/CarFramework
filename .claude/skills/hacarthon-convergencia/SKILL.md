---
name: hacarthon-convergencia
description: Use esta skill quando o time tiver várias ideias de solução soltas para o Desafio 1 do haCARthon (simplificar o CAR para o produtor rural) e precisar convergir para uma única ideia antes de seguir para ideação, protótipo e pitch. Avalia cada ideia contra os 4 critérios oficiais de julgamento e contra o perfil real do Seu Raimundo (ou da pessoa real entrevistada pelo time).
---

# Convergência de ideias — Desafio 1 do haCARthon

## Quando usar

O time tem 2 ou mais ideias de solução ainda não fechadas e precisa decidir qual seguir. Esta skill NÃO inventa a solução — ela organiza e avalia o que o time já trouxe, para acelerar a decisão.

## Contexto fixo do desafio

Leia `dados/edital-resumo.md` primeiro — ele tem o resumo curado do desafio,
da persona e dos critérios de avaliação. Se a informação necessária não
estiver lá, ou parecer incompleta para o que está sendo avaliado, consulte o
PDF original indicado na tabela de fallback ao final daquele arquivo (ex:
`Briefing_dos_Desafios.pdf` para exemplos de solução mais detalhados, ou
`Edital.pdf` para regras formais).

Resumo rápido para referência imediata, caso o arquivo não esteja disponível:

**Desafio 1:** Como simplificar a declaração e retificação do Cadastro Ambiental Rural (CAR)
para o produtor rural, aproveitando bases de dados abertas, garantindo cumprimento do
Código Florestal e gerando benefícios individuais e coletivos.

**Não é necessário software funcional.** Protótipos, wireframes, fluxogramas, vídeos e
apresentações são aceitos e avaliados da mesma forma que algo funcional.

**Os 4 critérios oficiais de julgamento (nota 1 a 10 cada):**
1. Pertinência temática ao desafio
2. Relevância do problema resolvido
3. Usabilidade e design — acesso simplificado e fácil compreensão do usuário
4. Inovação e criatividade da solução

Em caso de empate, prevalece a maior nota em "inovação e criatividade".

## Persona de referência

Sempre que possível, prefira os dados reais coletados pelo time (ver
`dados/raimundo-research.md` na raiz do projeto) sobre a persona genérica abaixo.
Use a persona genérica apenas como complemento ou se o arquivo de dados reais
ainda não existir.

**Seu Raimundo** — pequeno/médio produtor rural. Depende da propriedade para
renda e sustento. Quer regularizar o imóvel sem complicação, evitar multas e
embargos, e acessar crédito. Tem dificuldade com plataformas digitais e com o
entendimento técnico do Código Florestal (limites do imóvel, APP, reserva legal).
Confia em pessoas próximas (vizinhos, sindicatos, cooperativas, técnicos
agrícolas, gerentes de banco). Se informa por rádio, TV, WhatsApp e TikTok.
Maior medo: perder a terra, ter prejuízo financeiro, ser fiscalizado.

## Processo

1. **Liste as ideias do time.** Peça ao usuário para descrever cada ideia em
   1-3 frases se ainda não tiver feito isso na conversa.

2. **Se o arquivo `dados/raimundo-research.md` existir, leia-o primeiro.**
   Ele tem prioridade sobre a persona genérica acima para julgar relevância
   do problema.

3. **Para cada ideia, avalie nos 4 critérios**, dando uma nota estimada de
   1 a 10 e uma justificativa curta (1-2 frases) por critério. Seja honesto
   nas notas — o objetivo é ajudar a decidir, não inflar todas as ideias.

4. **Monte uma tabela comparativa** com as ideias nas linhas e os 4 critérios
   nas colunas, mais uma coluna de "soma" ao final.

5. **Dê uma recomendação justificada**, mas deixe claro que a decisão final é
   do time. Aponte explicitamente:
   - Qual ideia tem melhor nota em "relevância do problema" e por quê
   - Qual ideia seria mais fácil de demonstrar em um vídeo de até 2 minutos
   - Se alguma ideia pode ser combinada/simplificada a partir de duas ideias soltas

6. **Não avance para ideação, roteiro ou pitch nesta mesma execução.**
   Pare após apresentar a comparação e a recomendação. O time decide e then
   invoca a próxima skill (`hacarthon-ideacao`) já com a ideia escolhida.

## Cuidados

- Não despreze ideias por serem "tecnicamente simples" — o edital privilegia
  usabilidade e clareza, não sofisticação técnica.
- Não simule respostas do Raimundo ou da pessoa real entrevistada. Se faltar
  informação sobre como ela reagiria a uma ideia, diga isso explicitamente
  como uma lacuna, em vez de inventar uma reação.
- Se nenhuma ideia tiver ligação clara com dados abertos existentes (uma das
  exigências do enunciado do Desafio 1), aponte isso como risco antes de
  recomendar.
