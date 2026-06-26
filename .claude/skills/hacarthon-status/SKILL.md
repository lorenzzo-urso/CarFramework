---
name: hacarthon-status
description: Use esta skill para diagnosticar o estado atual do projeto haCARthon — o que já foi feito, o que está bloqueado, o que falta, e qual é o próximo passo exato. Ideal para retomar o trabalho após uma pausa ou para orientar um novo agente que entra no projeto pela primeira vez.
---

# Status do projeto — diagnóstico e próximo passo

## Quando usar

- Ao retomar o trabalho após uma pausa (novo dia, nova sessão)
- Quando um novo agente ou membro do time entra no projeto
- Quando o time está travado e não sabe o que fazer a seguir
- Como primeira skill a rodar em qualquer sessão de trabalho

---

## Processo

### Passo 1 — Leitura do estado atual

Ler os seguintes arquivos em sequência:

1. `CLAUDE.md` — contexto geral, fluxo e skills disponíveis
2. `dados/raimundo-research.md` — verificar se está preenchido ou ainda é template
3. `dados/edital-resumo.md` — verificar se há anotações ou decisões do time
4. `mapa de oportunidadesa.txt` — ideias registradas
5. Qualquer arquivo `.md` ou `.txt` criado recentemente na raiz ou em `dados/`

Se houver arquivos gerados por skills anteriores (canvas, jornada, narrativa, etc.),
ler também — indicam que etapas já foram executadas.

---

### Passo 2 — Diagnóstico por etapa do fluxo

Para cada etapa do fluxo, classificar como:
- ✅ **Feita** — há evidência concreta (arquivo preenchido, decisão registrada)
- ⚠️ **Parcial** — iniciada mas incompleta ou baseada em dados genéricos
- ❌ **Faltando** — não há evidência de execução
- 🔒 **Bloqueada** — depende de uma etapa anterior não concluída

| # | Etapa | Skill | Estado | Observação |
|---|-------|-------|--------|------------|
| 1 | Dados do produtor real | `hacarthon-pesquisa-produtor` | ? | raimundo-research.md vazio = ❌ |
| 2 | Ideia escolhida | `hacarthon-convergencia` | ? | |
| 3 | Value Proposition Canvas | `hacarthon-value-proposition` | ? | 🔒 se etapa 2 ❌ |
| 4 | Jornada do usuário | `hacarthon-user-journey` | ? | 🔒 se etapa 2 ❌ |
| 5 | Lean Canvas | `hacarthon-lean-canvas` | ? | 🔒 se etapa 2 ❌ |
| 6 | Fio condutor / narrativa | `hacarthon-narrativa` | ? | 🔒 se etapas 3-5 ❌ |
| 7 | Rascunho da Ideação | `hacarthon-ideacao` | ? | 🔒 se etapa 6 ❌ |
| 8 | Roteiro do vídeo | `hacarthon-roteiro-prototipo` | ? | 🔒 se etapa 6 ❌ |
| 9 | Pitch (slides + script) | `hacarthon-pitch` | ? | 🔒 se etapa 7 ❌ |
| 10 | Simulação de banca | `hacarthon-banca` | ? | 🔒 se etapa 9 ❌ |
| 11 | Checklist final | `hacarthon-checklist-entrega` | ? | 🔒 se etapas 7+8+9 ❌ |

---

### Passo 3 — Identificar o gargalo atual

O gargalo é a **primeira etapa ❌ ou ⚠️ do fluxo** — tudo que vem depois
dela está bloqueado, mesmo que o time queira pular.

Nomear o gargalo claramente:
> "O gargalo atual é [etapa X]. Enquanto ela não for resolvida, as etapas
> Y e Z não podem avançar com qualidade."

---

### Passo 4 — Próximo passo concreto

Dar **uma única instrução** — não uma lista de opções, uma instrução:

> "O próximo passo é invocar `/hacarthon-[skill]` e fornecer [o que o time
> precisa ter em mãos para rodar essa skill]."

Se o gargalo depende de algo que o time precisa fazer fora do Claude
(ex: realizar entrevista com produtor, definir ideia em reunião, gravar vídeo),
dizer isso explicitamente:

> "Antes de continuar no Claude, o time precisa [ação humana específica].
> Quando isso estiver feito, volte com [o que trazer] e rode
> `/hacarthon-[skill]`."

---

### Passo 5 — Resumo executivo

Entregar um bloco compacto para o time copiar ou fixar:

```
## Status haCARthon — [data de hoje]

Concluído: [lista das etapas ✅]
Em risco: [lista das etapas ⚠️ com motivo]
Bloqueado: [lista das etapas ❌/🔒]

Gargalo atual: [etapa]
Próximo passo: /hacarthon-[skill] — [o que trazer]

Prazo de submissão: [se souber]
Entregas pendentes: [Ideação / Protótipo / Pitch — marcar as que faltam]
```

---

## Cuidados

- Não criar falsa sensação de progresso. Uma etapa é ✅ apenas se há
  evidência concreta — um arquivo preenchido, uma decisão registrada, um
  output gerado. "O time discutiu" sem registro não conta como ✅.
- Se `raimundo-research.md` estiver vazio, classificar a etapa 1 como ❌
  e deixar claro que todas as skills que dependem de dados reais vão
  produzir outputs genéricos até isso ser resolvido.
- Não sugerir pular etapas para "ganhar tempo" — o CLAUDE.md documenta as
  dependências por razões concretas. Pular a narrativa antes de ideação,
  por exemplo, resulta em 3 entregas contando histórias diferentes.
- Se o time não souber o prazo de submissão, sinalizar isso como risco e
  recomendar verificar no Discord da organização ou em `documentação-oficial/Edital.pdf`.
