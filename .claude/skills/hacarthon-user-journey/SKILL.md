---
name: hacarthon-user-journey
description: Use esta skill para mapear a jornada atual do Seu Raimundo pelas 5 etapas do CAR, identificar o ponto exato de maior dor, e gerar a versão futura com a solução aplicada. A jornada futura vira diretamente a estrutura do roteiro do vídeo de protótipo e o slide "Como funciona" do pitch.
---

# User Journey Map — jornada do Seu Raimundo pelo CAR

## Por que usar

O critério de **usabilidade e design** exige que a solução demonstre
acesso simplificado e fácil compreensão. Uma jornada mapeada prova que o
time entende onde o usuário trava hoje — e que a solução intervém no
ponto certo, não em qualquer lugar do processo.

A jornada futura (com a solução) é também a estrutura mais natural para o
vídeo de protótipo: mostra o usuário em ação, do problema à resolução.

## Quando usar

Depois de `hacarthon-pesquisa-produtor` e `hacarthon-convergencia`.
Pode ser usada em paralelo com `hacarthon-value-proposition` — as duas
se complementam. A jornada identifica *onde* intervir; o VPC identifica
*por que* vale intervir.

Idealmente antes de `hacarthon-roteiro-prototipo`, pois a jornada futura
alimenta diretamente o roteiro do vídeo.

## Leitura prévia

- `dados/raimundo-research.md` — para usar dados reais de como o produtor
  vive cada etapa do processo
- Briefing dos Desafios, pág. 4 — as 5 etapas oficiais do processo CAR

---

## As 5 etapas oficiais do processo CAR

Estas são as etapas definidas no Briefing — a jornada sempre começa aqui:

1. **Preenchimento** — produtor declara dados do imóvel no SICAR
2. **Validação** — OEMA analisa e pode solicitar correções
3. **Integração** — governo federal integra as informações
4. **Uso** — dados usados para regularização e acesso a benefícios
5. **Atualização** — manutenção contínua para manter a base confiável

---

## Processo

### Passo 1 — Jornada atual (sem a solução)

Para cada uma das 5 etapas, preencher 4 dimensões:

**Formato por etapa:**

```
### Etapa N — [Nome]

**O que o Raimundo faz:**
[Ação concreta — o que ele literalmente faz, com que ferramenta, com ajuda de quem]

**O que ele pensa:**
[Monólogo interno — dúvida, medo, confusão ou esperança. Em linguagem simples,
como se fosse a voz dele]

**Como ele se sente:**
[Emoção dominante nesta etapa: confuso / com medo / frustrado / aliviado /
perdido / desconfiante / esperançoso]
Intensidade: 🔴 Alta dor / 🟡 Dor moderada / 🟢 Neutro ou positivo

**Ponto de atrito:**
[O obstáculo concreto que pode fazer ele desistir ou errar nesta etapa]
```

Ao final das 5 etapas, identificar:

**Momento de colapso** — a etapa de maior dor (🔴), onde o produtor desiste,
erra, ou precisa de ajuda paga. Este é o ponto de intervenção prioritário
da solução.

**Citação real** — se houver dado em `raimundo-research.md`, extrair a frase
que melhor representa a dor no momento de colapso. Esta frase é o gancho
do vídeo e do pitch.

---

### Passo 2 — Curva emocional da jornada atual

Gerar uma representação textual da curva emocional, etapa por etapa:

```
Etapa:     1          2          3          4          5
           Preencher  Validar    Integrar   Usar       Atualizar
Emoção:    😟         😰         😶         😌         😕
Nível:     Baixo      Baixo      Neutro     Alto       Baixo
           (ansiedade) (medo)               (alívio)   (dúvida)
```

Identificar: o vale mais fundo (pior momento) e o pico mais alto (melhor
momento). A solução deve aprofundar o pico e elevar o vale.

---

### Passo 3 — Jornada futura (com a solução)

Redesenhar as mesmas 5 etapas mostrando como a experiência muda com a
solução aplicada. Focar nas etapas onde a solução intervém.

**Para cada etapa modificada pela solução:**

```
### Etapa N — [Nome] (COM a solução)

**O que muda:**
[O que a solução faz de diferente nesta etapa — concreto e específico]

**Dados abertos usados:**
[Qual base aberta alimenta a solução nesta etapa: SIGEF, SICAR público,
MapBiomas, SNIF/RER, etc. — obrigatório mencionar pelo menos um por etapa
que a solução toca, conforme requisito do Desafio 1]

**Como o Raimundo se sente agora:**
[Emoção nova nesta etapa com a solução]
Intensidade: 🔴/🟡/🟢

**O que ele não precisa mais fazer:**
[O obstáculo que foi removido]
```

Para etapas que a solução não toca, manter a descrição da jornada atual
sem alteração — honestidade sobre o escopo.

---

### Passo 4 — Curva emocional comparada

Gerar a comparação entre as duas curvas:

```
Etapa:     1          2          3          4          5
Atual:     😟(2)      😰(1)      😶(5)      😌(8)      😕(3)
Futuro:    😊(7)      😌(6)      😶(5)      😊(9)      😌(6)

Melhora maior: Etapa 1 (+5) e Etapa 2 (+5)
Etapas sem mudança: Etapa 3
```

*(Escala 1-10, onde 10 = melhor experiência possível)*

---

### Passo 5 — Roteiro de 6 quadros para o vídeo

Traduzir a jornada futura em um storyboard textual de 6 quadros, pronto
para alimentar a skill `hacarthon-roteiro-prototipo`:

| Quadro | Tempo sugerido | O que mostrar | O que narrar |
|--------|----------------|---------------|--------------|
| 1 — Gancho | 0:00-0:12 | Raimundo diante do problema (citação real ou dado) | Frase de impacto |
| 2 — Problema | 0:12-0:25 | A dificuldade atual (etapa de maior dor) | O que acontece hoje |
| 3 — Solução entra | 0:25-0:40 | O primeiro contato com a solução | Como começar |
| 4 — Passo principal | 0:40-1:05 | A etapa mais diferenciada da solução | Como funciona |
| 5 — Resultado | 1:05-1:20 | CAR enviado / benefício desbloqueado | O que mudou |
| 6 — Encerramento | 1:20-1:35 | Nome da solução + chamada à ação | Resumo em uma frase |

Total: ~1min35s (com folga de segurança abaixo dos 2 minutos)

---

### Passo 6 — Conexão com as demais skills

Indicar explicitamente o que cada skill deve usar desta jornada:

- **`hacarthon-narrativa`:** quadro 1 (gancho) → abertura; etapa de maior dor
  → contraste "antes"; etapa com maior melhora → contraste "depois"
- **`hacarthon-roteiro-prototipo`:** os 6 quadros do Passo 5 como estrutura base
- **`hacarthon-pitch`:** etapa de maior dor → slide Problema; jornada futura
  simplificada → slide Como funciona (3-4 passos)
- **`hacarthon-ideacao`:** a etapa de colapso → campo Problema; as etapas
  melhoradas → campo Solução e Benefícios

## Cuidados

- A jornada atual deve ser honesta sobre o que é difícil — não suavizar para
  fazer a solução parecer mais impactante. Jurados que conhecem o CAR percebem.
- A jornada futura deve ser honesta sobre o escopo da solução. Se a solução
  cobre apenas as etapas 1 e 2, as etapas 3, 4 e 5 permanecem como estão.
- Cada etapa tocada pela solução **deve mencionar um dado aberto específico**
  — é requisito do Desafio 1, não um detalhe opcional.
- Se não houver dado real do produtor em `raimundo-research.md`, sinalizar
  isso no início e usar a persona oficial do Briefing — mas avisar que a
  jornada deve ser validada com um produtor real.
