---
name: hacarthon-banca
description: Use esta skill para simular uma banca de jurados exigente antes do pitch do haCARthon. Gera perguntas difíceis baseadas nos 4 critérios de avaliação e nos gargalos reais do Desafio 1, e para cada pergunta produz uma resposta defensável e sinaliza onde a solução tem buracos reais que precisam ser resolvidos.
---

# Simulação de banca — preparar o time para perguntas difíceis

## Quando usar

Depois que a ideação (`hacarthon-ideacao`) está rascunhada e antes de gravar
o áudio do pitch. A banca serve para dois fins:
1. Preparar o time para defender a solução verbalmente
2. Revelar buracos na proposta que ainda podem ser corrigidos antes da entrega

## Contexto de referência

Leia `dados/raimundo-research.md` e o rascunho de ideação disponível na
conversa antes de simular a banca — as perguntas serão mais cirúrgicas se
forem baseadas na solução específica do time, não genéricas.

Os 4 critérios de avaliação (nota 1 a 10 cada, empate decidido por critério 4):
1. Pertinência temática ao desafio
2. Relevância do problema resolvido
3. Usabilidade e design — acesso simplificado, fácil compreensão
4. Inovação e criatividade

Os 3 gargalos oficiais do Desafio 1 (fonte: Briefing dos Desafios):
- **Exclusão digital e técnica** — internet limitada, dificuldade de georreferenciar
- **Ciclo de retificações infinitas** — dados errados, vai-e-vem com OEMAs
- **Ruído na comunicação Estado-produtor** — linguagem inacessível, medo de sanções

## Processo

### Passo 1 — Receber a solução

Peça ao usuário que descreva a solução em 3-5 frases antes de começar.
Se a ideação já estiver na conversa, use diretamente.

### Passo 2 — Simular a banca

Gere perguntas organizadas por categoria. Para cada pergunta:
- Apresente a pergunta como um jurado perguntaria (direta, sem rodeios)
- Classifique o nível de risco: 🔴 Alta (buraco real) / 🟡 Média / 🟢 Baixa
- Gere uma resposta defensável de 2-4 frases
- Se for Alta: sinalize explicitamente o que o time precisa resolver antes de submeter

---

#### Bloco A — Pertinência e dados abertos

> **"Qual base de dados aberta específica a solução usa? Mostre onde está no
> site e o que exatamente ela fornece para a solução."**

> **"O enunciado do Desafio 1 pede que a solução 'aproveite bases de dados
> abertas disponíveis'. Onde exatamente isso aparece no protótipo de vocês?"**

> **"O problema que vocês descreveram existe de verdade ou é uma hipótese?
> Quantos imóveis no Brasil têm CAR irregular hoje?"**

---

#### Bloco B — Relevância e validação com o usuário

> **"Vocês testaram essa solução com algum produtor rural real? Se não,
> como sabem que ele usaria?"**

> **"O Seu Raimundo não tem internet confiável na propriedade. Como a
> solução de vocês funciona offline ou com conexão ruim?"**

> **"Vocês entrevistaram alguém para essa solução? O que a pessoa disse
> que foi mais surpreendente?"**

> **"Pequenos produtores frequentemente não confiam em apps do governo.
> Como vocês vencem essa desconfiança?"**

---

#### Bloco C — Usabilidade e design

> **"Mostrem o fluxo mais simples da solução em 3 passos. Se o produtor
> travar no passo 2, o que acontece?"**

> **"Um produtor de 60 anos, que usa só WhatsApp e rádio, consegue usar
> isso sem ajuda de ninguém? Expliquem como."**

> **"A interface de vocês pressupõe que o produtor sabe o que é APP ou
> Reserva Legal. E se ele não souber?"**

> **"O SICAR atual tem manual de 200 páginas. Por que a solução de vocês
> seria diferente na prática?"**

---

#### Bloco D — Inovação e diferencial

> **"O portal do SICAR já existe e é gratuito. Por que o produtor usaria
> a solução de vocês em vez do que já tem?"**

> **"Ferramentas de suporte ao CAR já existem no mercado (AtMarket,
> Terra Mapeada, AgroTools). O que vocês fazem que elas não fazem?"**

> **"Qual é a aposta criativa da solução de vocês? O que é genuinamente
> novo, não apenas uma melhoria incremental?"**

> **"Se um jurado vir 10 equipes apresentando hoje, por que vai lembrar
> da solução de vocês amanhã?"**

---

#### Bloco E — Modelo de negócio e sustentabilidade

> **"Quem paga por isso? O governo federal? Os estados? O produtor?
> Se é gratuito, quem mantém e atualiza?"**

> **"O edital exige código aberto. Mas código aberto não significa que
> alguém vai manter. Quem seria o guardião dessa solução depois do
> hackathon?"**

> **"Vocês dependem de uma API do SICAR que ainda não é pública. O que
> acontece se o governo não abrir essa API?"**

> **"Para escalar para 8 milhões de imóveis no CAR, o que precisaria
> mudar na solução?"**

---

#### Bloco F — Impacto coletivo

> **"Vocês descreveram o benefício para o produtor. Mas qual é o
> benefício para o governo, para o meio ambiente, para o Brasil?"**

> **"Se essa solução funcionasse, em quanto tempo o número de CARs
> regularizados aumentaria? Qual é a estimativa de vocês?"**

> **"A Luana, analista do OEMA, teria menos trabalho ou mais trabalho
> com essa solução? Por quê?"**

---

### Passo 3 — Relatório de risco

Ao final das perguntas, gere um relatório curto:

| Categoria | Risco | Ação antes da entrega |
|---|---|---|
| Pertinência / dados abertos | 🔴/🟡/🟢 | ... |
| Validação com usuário real | 🔴/🟡/🟢 | ... |
| Usabilidade offline/baixa literacia | 🔴/🟡/🟢 | ... |
| Diferencial claro vs. SICAR | 🔴/🟡/🟢 | ... |
| Modelo de negócio defensável | 🔴/🟡/🟢 | ... |
| Impacto coletivo quantificado | 🔴/🟡/🟢 | ... |

### Passo 4 — As 3 perguntas mais prováveis

Com base na solução específica do time, eleja as **3 perguntas que um jurado
exigente quase certamente fará** e gere as respostas mais sólidas possíveis.
Essas 3 devem ser ensaiadas pelo time antes de gravar o áudio do pitch.

## Cuidados

- Não suavize as perguntas. O objetivo é revelar fragilidades reais, não
  confortar o time. Uma banca que não incomoda não prepara.
- Não invente um problema que a solução não tem — as perguntas devem ser
  calibradas para o que foi descrito, não para uma solução genérica.
- Se a solução ainda não estiver bem definida, diga isso antes de começar:
  rodar a banca em cima de uma ideia vaga gera respostas igualmente vagas.
- Lembre o time que o critério de desempate é **inovação e criatividade** —
  o Bloco D é o mais estratégico para trabalhar.
