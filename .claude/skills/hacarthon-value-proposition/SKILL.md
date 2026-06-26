---
name: hacarthon-value-proposition
description: Use esta skill para preencher o Value Proposition Canvas com os dados reais do produtor entrevistado e da solução escolhida. Mapeia dores/ganhos do Seu Raimundo contra o que a solução entrega, identifica os 3 encaixes mais fortes para o pitch, e sinaliza o que a solução promete mas não encaixa em nenhuma dor real.
---

# Value Proposition Canvas — encaixe entre dor real e solução

## Por que usar

O critério de maior peso após inovação é **"relevância do problema resolvido"**.
O VPC garante que a solução responde a dores reais do Seu Raimundo — não a
dores que o time imaginou que ele teria. Cada encaixe forte no canvas vira
um argumento direto no pitch e na ideação.

## Quando usar

Depois de `hacarthon-pesquisa-produtor` (dados reais disponíveis) e depois
de `hacarthon-convergencia` (ideia escolhida). Idealmente antes de
`hacarthon-narrativa`, porque os encaixes mais fortes alimentam a frase-ouro
e a âncora de inovação.

## Leitura prévia

- `dados/raimundo-research.md` — fonte primária das dores e ganhos reais
- Se o arquivo estiver vazio, usar as personas oficiais do Briefing dos
  Desafios (Seu Raimundo, págs. 5-6)

---

## Estrutura do canvas

O VPC tem dois lados que precisam encaixar:

```
┌─────────────────────────────┐     ┌─────────────────────────────┐
│     PERFIL DO CLIENTE       │     │       MAPA DE VALOR         │
│                             │     │                             │
│  [Tarefas]   [Dores]        │  ↔  │  [Produtos]  [Aliviadores]  │
│              [Ganhos]       │     │              [Geradores]    │
└─────────────────────────────┘     └─────────────────────────────┘
          Seu Raimundo                       Sua solução
```

---

## Processo

### Passo 1 — Perfil do Cliente (lado esquerdo)

Preencher com base nos dados reais do produtor. Se houver dados de dois
perfis (Raimundo e Luana), fazer um canvas por perfil — mas priorizar
Raimundo para o Desafio 1.

#### 1a. Tarefas (Customer Jobs)

O que o Seu Raimundo está tentando realizar? Listar as tarefas nos 3 níveis:

**Funcional** — o que ele precisa fazer literalmente:
- Declarar o imóvel no SICAR
- Georreferenciar as áreas (APP, Reserva Legal, perímetro)
- Corrigir erros e reenviar após notificação do OEMA
- Manter o cadastro atualizado

**Emocional** — como ele quer se sentir:
- Seguro de que não vai ser multado
- No controle da situação, sem depender de intermediários pagos
- Respeitado no processo, não tratado como quem não entende nada

**Social** — como quer ser visto:
- Como um produtor regularizado, não um infrator ambiental
- Como alguém que cuida da propriedade corretamente

#### 1b. Dores (Pains)

O que frustra, bloqueia ou gera medo? Ordenar da mais intensa para a menos:

Classificar cada dor em um dos 3 gargalos do Desafio 1:
- **[DIG]** Exclusão digital e técnica
- **[RET]** Ciclo de retificações infinitas
- **[COM]** Ruído na comunicação Estado-produtor

Exemplos de dores para referenciar (substituir pelos dados reais):
- Não entende o que é APP ou Reserva Legal na prática [DIG]
- Não consegue usar o SICAR sozinho [DIG]
- Recebe notificação de erro mas não sabe o que corrigir [COM]
- Pagou despachante caro e o cadastro voltou com erro mesmo assim [RET]
- Tem medo de declarar errado e ser multado [COM]
- Perde horas de trabalho para resolver questões burocráticas [RET]
- Não tem internet confiável na propriedade [DIG]

#### 1c. Ganhos (Gains)

O que seria um resultado positivo além do mínimo esperado?

**Mínimo esperado:** CAR enviado sem erros, sem precisar pagar alguém
**Desejado:** Processo rápido, feito pelo celular, com confirmação clara
**Inesperado:** Saber exatamente quais benefícios (crédito, isenção) seu CAR
regularizado vai desbloquear

---

### Passo 2 — Mapa de Valor (lado direito)

Preencher com base na solução escolhida.

#### 2a. Produtos e Serviços

Listar os componentes concretos da solução:
- O canal de acesso (WhatsApp, app, site, papel impresso, etc.)
- As funcionalidades principais (pré-preenchimento, guia passo a passo, etc.)
- Os dados abertos que usa (SIGEF, SICAR público, MapBiomas, SNIF, etc.)

#### 2b. Aliviadores de Dores (Pain Relievers)

Para cada dor listada no perfil, descrever como a solução a reduz ou elimina.

**Formato:** `[Dor] → [Como a solução alivia]`

Exemplos do formato (não da solução):
- "Não entende APP → O assistente identifica automaticamente as APPs usando
  dados do SIGEF e mostra no mapa o que precisa ser preservado"
- "Recebe notificação de erro mas não sabe corrigir → O sistema traduz a
  notificação técnica do OEMA em linguagem simples com passo a passo de correção"

#### 2c. Geradores de Ganho (Gain Creators)

Para cada ganho desejado ou inesperado, como a solução o cria ou amplifica?

**Formato:** `[Ganho desejado] → [Como a solução o cria]`

---

### Passo 3 — Análise de encaixe

Após preencher os dois lados, fazer a análise de encaixe:

#### 3a. Encaixes fortes (✅)
Dores que a solução alivia de forma direta e concreta. Marcar cada uma.
**Estes são os argumentos centrais do pitch.**

#### 3b. Encaixes fracos (⚠️)
Dores que a solução toca mas não resolve de verdade — ou onde a solução
promete mais do que o protótipo demonstra. Sinalizar honestamente.

#### 3c. Dores sem encaixe (❌)
Dores do Raimundo que a solução não aborda. Isso não é problema — toda
solução tem escopo. Mas se for uma dor crítica e não houver encaixe, o
jurado vai perguntar sobre isso na banca.

#### 3d. Funcionalidades sem encaixe (🗑️)
Elementos da solução que não aliviam nenhuma dor e não criam nenhum ganho
do perfil real. Candidatos a corte — simplificam a solução e o protótipo.

---

### Passo 4 — Entrega do canvas

Produzir o canvas em formato de tabela markdown, pronto para ser referenciado
nas demais skills:

```markdown
## Value Proposition Canvas — [Nome da solução]

### Perfil do Seu Raimundo
| Tipo | Item | Intensidade |
|------|------|-------------|
| Tarefa funcional | ... | Alta/Média/Baixa |
| Dor [DIG/RET/COM] | ... | Alta/Média/Baixa |
| Ganho desejado | ... | Alta/Média/Baixa |

### Mapa de Valor
| Componente | Elemento | Encaixe |
|------------|----------|---------|
| Aliviador | ... → [dor que alivia] | ✅/⚠️ |
| Gerador | ... → [ganho que cria] | ✅/⚠️ |

### Top 3 encaixes para o pitch
1. [Encaixe mais forte — dor + aliviador]
2. [Segundo encaixe]
3. [Terceiro encaixe]

### Riscos
- Dores sem encaixe: [listar]
- Funcionalidades sem encaixe: [listar]
```

### Passo 5 — Conexão com as demais skills

Ao final, indicar explicitamente:
- **Para `hacarthon-narrativa`:** qual encaixe virar a frase-ouro e qual
  virar a âncora de inovação
- **Para `hacarthon-ideacao`:** qual encaixe usar no campo "Relevância do
  problema" e qual usar em "Benefícios"
- **Para `hacarthon-pitch`:** qual encaixe usar no slide "Problema" e qual
  no slide "Como funciona"

## Cuidados

- Não inventar dores que não foram relatadas pelo produtor entrevistado.
  Se o dado não estiver em `raimundo-research.md` nem no Briefing oficial,
  marcar como `[HIPÓTESE — não validada]`.
- Aliviadores de dores precisam ser concretos: "torna mais simples" não é
  um aliviador — "substitui o georreferenciamento manual por confirmação de
  mapa pré-preenchido com dados do SIGEF" é.
- Se a solução tiver mais funcionalidades sem encaixe do que com encaixe,
  o escopo está errado — sinalizar ao time antes de continuar.
