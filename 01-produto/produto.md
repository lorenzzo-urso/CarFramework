# O produto — Terra Comum / Compadre

## A ideia

O CAR existe, os dados ambientais existem — mas estão fragmentados e escritos numa
linguagem que o produtor rural não entende. **O problema não é falta de
informação; é falta de contexto.**

A solução tem duas faces que trabalham juntas:

- **Compadre** — um assistente que conversa com o produtor pelo **WhatsApp** e o
  ajuda a entender, declarar e corrigir o CAR em linguagem simples. É a cara
  demonstrável da solução.
- **Terra Comum** — uma **camada semântica aberta** do território rural: ontologia
  do Código Florestal + grafo de conhecimento + Agent Hub, construída sobre o RER
  open-source. É o motor invisível que faz o Compadre (e outros agentes) raciocinarem.

> **Princípio de produto:** esconde a máquina pesada, ensina só o essencial.
> O produtor não vê ontologia, grafo, integração de dados — só recebe a resposta
> na língua dele. Mas aprende o que importa: o que é uma APP, por que veio uma
> pendência, o que o CAR em dia desbloqueia.

---

## O que o jurado vê × o que o jurado ouve

| VÊ (protótipo/vídeo) | OUVE (pitch) |
|---|---|
| O Seu Raimundo no WhatsApp resolvendo o CAR em minutos | A camada aberta (Terra Comum) que sustenta tudo |
| Compadre traduz a pendência, pré-preenche o mapa, mostra benefícios | Ontologia + camada semântica + Agent Hub sobre o RER |
| Telas simples, linguagem acessível | Governo, cooperativas e terceiros constroem agentes na mesma camada |

A arquitetura **nunca aparece no vídeo** — só no pitch. O critério de usabilidade
é julgado pela experiência do produtor.

---

## Os agentes da plataforma

O Compadre é o **primeiro agente** — o produtor-facing. A mesma camada serve outros:

| Agente | Para quem | Papel |
|---|---|---|
| **Compadre** (produtor) | Seu Raimundo | Entender/declarar/corrigir o CAR; descobrir benefícios |
| **Auditor** | Analista do órgão (OEMA) | Explica pendências, gera parecer técnico |
| **Territorial** | Governo | Déficit de Reserva Legal por município, áreas críticas |
| **Crédito** | Cooperativas | Carteira elegível, risco diluído, crédito verde |
| **De terceiros** | Devs, pesquisadores, Embrapa | Criam skills sobre a camada aberta (efeito-rede) |

---

## Modelo de negócio (resumo)

- O **produtor nunca paga** — é usuário e fonte de dados, não cliente.
- O **núcleo é open-source** (Bem Público Digital).
- A receita vem do **acesso à API semântica / aos agentes**, consumido por
  **cooperativas de crédito (B2B)** e **governo (B2G)** — vende-se a inferência
  derivada, não o dado bruto nem o software.
- **Vantagem injusta:** ser o substrato aberto (efeito-rede) + a inteligência
  acumulada + a ontologia do CAR (inédita no ecossistema).

Detalhe em [`../03-frameworks/lean-canvas.md`](../03-frameworks/lean-canvas.md).

---

## Diferencial competitivo

> Diferente do SICAR — que exige que o produtor saiba a regra — e diferente de
> mais um chatbot que adivinha em cima de texto, o Compadre **raciocina sobre um
> modelo semântico aberto** do Código Florestal e do território. Explica o *porquê*,
> com rastreabilidade, e o mesmo modelo serve produtor, governo e cooperativas.
> É infraestrutura aberta, não um aplicativo fechado.

Ver [`../01-produto/narrativa.md`](narrativa.md) e
[`../01-produto/desafio-e-fit.md`](desafio-e-fit.md).
