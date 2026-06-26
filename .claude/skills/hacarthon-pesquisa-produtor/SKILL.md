---
name: hacarthon-pesquisa-produtor
description: Use esta skill para processar dados brutos de entrevistas com produtores rurais (ou analistas ambientais) e estruturá-los no arquivo dados/raimundo-research.md. Usa as personas oficiais do Briefing dos Desafios como referência-mestra e extrai citações, dores concretas e dados que desbloqueiam as demais skills do haCARthon.
---

# Pesquisa com produtor — estruturar dados reais da entrevista

## Por que esta skill existe

Todas as outras skills do haCARthon (ideação, roteiro, pitch, banca) ficam
genéricas enquanto `dados/raimundo-research.md` estiver vazio. Esta skill
transforma notas brutas de entrevista em dado estruturado e imediatamente
usável nas demais entregas.

## Personas de referência (fonte: Briefing dos Desafios, pág. 5-6)

Estas são as personas **oficiais** do haCARthon. Use-as como régua para
classificar e qualificar os dados coletados.

### Seu Raimundo — Produtor Rural (Persona 1)

**Quem é:** pequeno ou médio produtor que depende diretamente da propriedade
para renda, sustento e estabilidade familiar.

**Objetivo principal:** manter o imóvel regularizado, documentos em dia, sem
impacto na rotina — para evitar multas, embargos e conflitos, preservar seus
direitos sobre a terra e acessar linhas de crédito.

**Dificuldades centrais:**
- Entender as regras do Código Florestal (APP, Reserva Legal, limites do imóvel)
- Usar plataformas digitais como o CAR
- Georreferenciar áreas de preservação sozinho e com precisão
- Medo de cometer erros que resultem em sanções ou prejuízos

**Como decide:** orientado por pessoas e instituições de confiança — vizinhos,
sindicatos, cooperativas, líderes comunitários, técnicos agrícolas, gerentes de banco.

**Como se informa:** rádio, televisão, WhatsApp, TikTok. Confia mais em
exemplos concretos do que em orientações abstratas.

**O que é sucesso para ele:** não ter prejuízos, não ser incomodado por
fiscalizações, trabalhar com tranquilidade, garantir o futuro da família.

**Maiores medos:** perda da terra, falta de recursos financeiros, incerteza.

---

### Luana — Analista Ambiental (Persona 2)

**Quem é:** analista dos órgãos estaduais do CAR, trabalha com regularização
ambiental. Lida com dados, sistemas e com produtores rurais no dia a dia.

**Responsabilidades:** corrigir e validar informações do CAR, PRA e CRA;
fazer a ponte entre governo, produtores e outras instituições.

**Dificuldades:** sistemas complexos, desafios no acesso a dados, equilibrar
cumprimento estrito da lei com orientação acessível ao produtor.

**O que valoriza:** clareza, organização, ferramentas que facilitem seu trabalho
e o atendimento ao público.

---

## Os 3 gargalos oficiais do Desafio 1 (referência para qualificar as dores)

Use estes gargalos para categorizar o que o entrevistado relatou:

1. **Exclusão digital e técnica** — acesso limitado à internet, dificuldade de
   georreferenciar APP/RL, incapacidade de usar o SICAR sozinho
2. **Ciclo de retificações infinitas** — dados autodeclarados com erros,
   vai-e-vem com OEMAs, produtor não sabe como corrigir
3. **Ruído na comunicação Estado-produtor** — notificações de erro viram fonte
   de medo, linguagem inacessível, falta de canal confiável

---

## Processo

### Passo 1 — Receber os dados brutos

Peça ao usuário para colar os dados da entrevista em qualquer formato:
respostas do Google Forms, transcrição de áudio, notas de WhatsApp, anotações
livres. Não exija formato estruturado — a skill organiza a partir do bruto.

Se houver dados de múltiplos entrevistados, processe um de cada vez e pergunte
qual é o principal (o que será usado como referência nas entregas).

### Passo 2 — Identificar a persona

Classifique o entrevistado:
- **Perfil Raimundo** (produtor/posseiro rural) → usar como fonte primária da dor
- **Perfil Luana** (analista/técnico/extensionista) → valioso para o contexto
  sistêmico, mas não substitui a voz do produtor na abertura do pitch
- **Híbrido** (ex: técnico agrícola que é também produtor) → registrar os dois ângulos

### Passo 3 — Extrair e estruturar as informações

Para cada entrevistado, extraia e preencha as seções abaixo. Se a informação
não estiver nos dados brutos, marque como `[NÃO COLETADO]`.

#### 3.1 — Identificação
- Nome (ou apelido se preferir anonimato)
- Região / Estado
- Tipo de propriedade (área, cultura principal)
- Situação atual no CAR (nunca fez / fez mas irregular / regular / em retificação)

#### 3.2 — Dores concretas com o CAR
- O que já tentou fazer no CAR e não conseguiu?
- Qual etapa do processo causou mais dificuldade?
- Precisou pagar alguém para fazer o CAR? Quanto? Valeu a pena?
- Já recebeu notificação ou teve imóvel embargado por causa do CAR?
- Classifique cada dor reportada em um dos 3 gargalos oficiais

#### 3.3 — Relação com tecnologia
- Tem smartphone? Usa internet (4G, Wi-Fi)?
- Usa WhatsApp? TikTok? Acessa serviços do governo online?
- Já tentou acessar o portal do SICAR? O que achou?

#### 3.4 — Fontes de confiança
- Quem ele pergunta quando tem dúvida sobre terra/documentação?
- Já usou EMATER, sindicato, cooperativa, extensionista?
- Tem banco ou cooperativa de crédito que orienta sobre regularização?

#### 3.5 — Citações diretas usáveis
Extraia **até 5 frases** ditas pelo entrevistado que:
- Descrevem a dor com palavras simples e concretas
- Poderiam abrir o vídeo de protótipo ou o pitch com impacto emocional
- Expressam o que ele quer (não o que ele não quer)

Marque cada uma com o tempo estimado de fala (para o roteiro do vídeo):
> `"[frase exata ou parafraseada]"` — ~X segundos falado

#### 3.6 — Tentativas anteriores de resolver o problema
- Já tentou alguma solução diferente do SICAR? Qual?
- Por que não funcionou ou foi insuficiente?
- O que ele faria diferente se pudesse começar de novo?

#### 3.7 — Visão de sucesso
- Como seria o processo ideal do CAR para ele?
- O que precisaria acontecer para ele conseguir fazer sozinho?
- O que é "ter o CAR em dia" na prática, para a vida dele?

### Passo 4 — Gerar o arquivo estruturado

Produza o conteúdo completo para sobrescrever `dados/raimundo-research.md`,
no formato markdown, com todas as seções acima preenchidas com os dados reais.

Inclua no topo do arquivo:
```
# Dados reais do produtor entrevistado
Data da entrevista: [data]
Processado por: hacarthon-pesquisa-produtor
```

### Passo 5 — Ranking de citações para as entregas

Ao final, destaque as **3 melhores citações** ordenadas por potencial de impacto,
explicando onde cada uma se encaixa melhor:
- Citação A → abertura do vídeo de protótipo (gancho emocional)
- Citação B → slide "Problema" do pitch
- Citação C → campo Problema da ideação

### Passo 6 — Gap report

Liste explicitamente o que **não foi coletado** e que faria diferença nas
entregas. Priorize os gaps mais críticos para o jurado do haCARthon.

## Cuidados

- Nunca invente ou extrapole uma frase que o entrevistado não disse. Use
  `[PARÁFRASE]` se a frase foi resumida, e `[CITAÇÃO DIRETA]` se é literal.
- Se o entrevistado não se encaixa no perfil Raimundo (ex: é um grande
  fazendeiro ou um pesquisador), registre isso claramente — os dados ainda
  são úteis como contexto, mas não representam o público-alvo principal.
- A Luana é uma persona valiosa para o pitching do impacto sistêmico, mas
  a dor central do Desafio 1 vem do Raimundo. Se só houver dados de Luana,
  avise o time que a voz do produtor ainda está faltando.
