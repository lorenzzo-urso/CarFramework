---
name: hacarthon-pitch
description: Use esta skill para montar a entrega de Pitch do haCARthon — slides em PDF com narração em áudio gravada por cima. Gera o conteúdo de cada slide e o script de narração, e usa a skill pptx do ambiente para produzir o arquivo .pptx final pronto para exportar como PDF.
---

# Pitch — terceira entrega obrigatória do haCARthon

## O que esta entrega exige

Leia `dados/edital-resumo.md` primeiro para confirmar os itens obrigatórios
e os critérios de avaliação. Se algo não estiver claro lá, use a tabela de
fallback ao final daquele arquivo para saber qual PDF original consultar.

A entrega é feita exclusivamente na plataforma de entregas: um PDF de slides
com áudio gravado por cima, apresentando o projeto. O pitch precisa trazer,
obrigatoriamente:

- Nome da solução
- Público-alvo
- Problema
- O que é a solução criada
- Como ela funciona
- Modelo de negócios
- Diferencial competitivo

## Quando usar

Depois que a ideação (`hacarthon-ideacao`) já está pronta — o pitch reaproveita
o problema, a solução e o público-alvo definidos ali, e adiciona modelo de
negócios e diferencial competitivo, que normalmente não aparecem na ideação.

## Processo

### 1. Gerar o conteúdo, slide por slide

Estrutura sugerida (ajustável conforme o conteúdo, mas sem pular nenhum item
obrigatório do edital):

1. **Capa** — nome da solução + uma frase de impacto sobre o problema
2. **O problema** — a dor real do produtor, com o caso concreto se disponível
   em `dados/raimundo-research.md`
3. **Público-alvo** — quem é afetado e em que escala
4. **A solução** — o que é, em poucas palavras
5. **Como funciona** — passo a passo simplificado (ideal: 3-4 passos, não mais)
6. **Modelo de negócio** — como a solução se sustenta ou se viabiliza
   (gratuito via parceria pública, freemium, licenciamento, etc. — escolher
   o que for coerente com a natureza de código aberto exigida pelo edital)
7. **Diferencial competitivo** — por que esta solução é diferente de algo que
   já existe ou de uma ideia óbvia
8. **Encerramento** — call to action / próximos passos

Para cada slide, gere:
- O texto que aparece na tela (curto — slides não são parágrafos)
- O script de narração completo (frases completas, em português simples)

### 2. Gerar o arquivo .pptx

Esta skill NÃO contém lógica própria de geração de pptx. Quando o usuário
pedir o arquivo final:

1. Leia a skill `pptx` do ambiente (geralmente em
   `/mnt/skills/public/pptx/SKILL.md` ou equivalente no Claude Code) e siga
   as instruções dela para criar a apresentação do zero com `pptxgenjs`.
2. Use o conteúdo gerado no passo 1 como texto de cada slide.
3. Escolha uma paleta de cores conectada ao tema (rural, ambiental, terra,
   verde/marrom/terracota) — evite azul genérico de slide corporativo.
4. Siga as regras de QA da skill pptx (texto não pode vazar da caixa, sem
   tarjas decorativas, contraste adequado) antes de entregar o arquivo final.

### 3. Entregar separadamente o script de narração

Mesmo depois de gerado o .pptx, entregue também o script de narração completo
em texto puro (markdown simples), slide por slide, para o time gravar o áudio.

## Cuidados

- Não generalize o "modelo de negócio" de forma vaga — o time precisa de algo
  que consiga defender se um jurado perguntar "e como isso se sustenta?".
  Se não houver clareza ainda, sinalize isso como uma lacuna em vez de
  inventar um modelo genérico de SaaS que não faz sentido para uma solução
  de bem público digital em código aberto.
- O "diferencial competitivo" deve comparar com algo real: o processo atual
  do CAR sem a solução, ou uma alternativa óbvia que o jurado pensaria
  primeiro — não comparar com um concorrente fictício.
- Mantenha a narração em linguagem simples mesmo no pitch para jurados —
  jargão técnico não impressiona neste edital, clareza sim.
