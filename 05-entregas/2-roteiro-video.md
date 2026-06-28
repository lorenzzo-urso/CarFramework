# Roteiro — Vídeo de Protótipo

**Solução:** Car Framework (Compadre + Agent Hub)
**Formato:** Telas navegáveis (compadre.html + hub.html) com narração em áudio
**Limite:** ≤ 120s · Meta de segurança: **107s**

> **Princípio deste roteiro:** mostrar primeiro o resultado (Compadre/Raimundo),
> depois abrir o capô e explicar **como funciona** — ontologia, fontes abertas,
> protocolo de agentes. Os jurados avaliam inovação pelo mecanismo, não só pela interface.

---

## Roteiro completo

---

### [0:00 – 0:08] GANCHO · 8s

**Tela:** Print de notificação técnica do órgão ambiental (dados pessoais cobertos)

**Narração:**
> "8,2 milhões de imóveis no CAR.
> E nenhum sistema sabe dizer ao produtor, em português, o que está errado no dele."

---

### [0:08 – 0:15] PROBLEMA · 7s

**Tela:** Imagem simples — notificação incompreensível, gaveta, telefone

**Narração:**
> "A linguagem técnica paralisa. O crédito fica bloqueado.
> O ciclo de correções pode durar meses."

---

### [0:15 – 0:40] O QUE O RAIMUNDO VÊ · 25s

> _Mostrar: compadre.html_

**[0:15 – 0:21] · 6s — Raimundo manda "oi"**
Tela: Chat abre, digita "oi", envia
> "O Seu Raimundo manda um 'oi' pro Compadre, pelo WhatsApp."

---

**[0:21 – 0:33] · 12s — Resposta traduzida + rastreabilidade**
Tela: Resposta em linguagem simples + TraceSeal `📖 Lei 12.651/2012, Art. 4º, I, a`
> "O Compadre traduz a pendência em linguagem simples.
> E mostra a regra exata por trás — rastreável, verificável.
> Não é o modelo inventando. É a lei."

---

**[0:33 – 0:40] · 7s — Déficit descoberto antes do envio**
Tela: 4,19 ha de déficit de mata ciliar calculado
> "Antes de enviar: 4,19 hectares de déficit detectados com dado aberto.
> O produtor descobriu o problema antes da fiscalização."

---

### [0:40 – 1:35] COMO FUNCIONA · 55s

> _Mostrar: hub.html — páginas Protocolo, Agentes, Ecossistemas_

---

**[0:40 – 0:55] · 15s — A ontologia: a fonte de verdade**
Tela: Hub → página **Protocolo** → conceitos da ontologia (`car:FaixaAPP_ate10`, `car:ReservaLegal`)
> "A resposta não saiu do LLM.
> Saiu daqui — uma ontologia do Código Florestal.
> Cada regra é um nó no grafo. Quando a lei muda, muda um nó.
> Todos os agentes ficam corretos automaticamente."

---

**[0:55 – 1:07] · 12s — As fontes abertas**
Tela: Protocolo → seção "Origens dos dados" (SIGEF, MapBiomas, RER, SICAR, Lei 12.651)
> "As fontes são todas públicas: SIGEF, MapBiomas, o RER do governo federal.
> Nenhum dado inventado. Nenhuma API proprietária.
> Os mesmos dados que o analista usa para validar."

---

**[1:07 – 1:22] · 15s — O protocolo de agentes**
Tela: Hub → página **Agentes** → 7 cards — câmera passa por eles
> "O Car Framework é um protocolo de agentes.
> Cada agente é um manifesto YAML sobre a mesma camada de conhecimento.
> O Compadre serve o produtor.
> O Auditor serve o analista do OEMA.
> O Crédito serve a cooperativa.
> Um protocolo. Múltiplas personas. Zero retrabalho."

---

**[1:22 – 1:35] · 13s — O território em escala**
Tela: Hub → página **Ecossistemas** — mapa com imóveis, zonas, nós coloridos
> "E em escala: imóveis conformes, déficits detectados, áreas de APP mapeadas —
> tudo sobre dado aberto, antes mesmo de qualquer fiscalização."

---

### [1:35 – 1:47] ENCERRAMENTO · 12s

**Tela:** Logo / Hub com o nome da solução

**Narração:**
> "Car Framework.
> O território já tinha fronteiras.
> Faltava a linguagem para lê-las.
> A plataforma é aberta. Qualquer agente pode ser publicado.
> A estrada é de todos."

---

## Contagem de tempo

| Bloco | Duração |
|---|---|
| Gancho | 8s |
| Problema | 7s |
| Compadre (resultado) | 25s |
| **Como funciona** | **55s** |
| Encerramento | 12s |
| **Total** | **107s** |

Margem de segurança: **13 segundos** antes do limite de 120s.

---

## Por que essa estrutura

O vídeo responde às quatro perguntas dos jurados, nessa ordem:

| Pergunta do jurado | Bloco que responde |
|---|---|
| "Qual é o problema?" | Gancho + Problema |
| "O que o produtor vê?" | Compadre |
| "Como funciona de verdade?" | Protocolo + Fontes + Agentes |
| "Qual é a escala possível?" | Ecossistemas + Encerramento |

A seção **Como funciona** é o que diferencia de qualquer chatbot genérico —
é onde a inovação se torna visível para os jurados.

---

## Lista de produção — checklist

### Telas a capturar (screencast)
- [ ] `compadre.html` — chat abrindo, Raimundo digitando "oi"
- [ ] `compadre.html` — resposta + TraceSeal (`Lei 12.651/2012, Art. 4º, I, a`)
- [ ] `compadre.html` — 4,19 ha de déficit calculado
- [ ] `hub.html` → **Protocolo** — conceitos da ontologia (`car:FaixaAPP_ate10`, etc.)
- [ ] `hub.html` → **Protocolo** — seção "Origens dos dados" (5 fontes abertas)
- [ ] `hub.html` → **Agentes** — câmera passando pelos 7 cards
- [ ] `hub.html` → **Ecossistemas** — mapa com nós e zonas

### Assets visuais
- [ ] Print de notificação técnica real (dados pessoais cobertos) para o gancho
- [ ] Imagem estática simples para o bloco Problema (10s)

### Áudio
- [ ] Narração gravada — voz calma, ritmo firme (~130 palavras/min)
- [ ] Música de fundo opcional: suave, não competindo com a narração

---

## Dicas de corte se passar do tempo

Se passar de 115s, cortar nesta ordem:

1. **Ecossistemas** — reduzir de 13s para 8s (câmera mais rápida)
2. **Encerramento** — cortar "A estrada é de todos" (−3s)
3. **Fontes abertas** — listar só 3 fontes em vez de 5 (−4s)

---

## Requisitos técnicos de entrega

- Postar no YouTube como **"Público"** ou **"Não listado"** (nunca Privado)
- Inserir o link do YouTube na plataforma de entrega
- Medir com cronômetro antes de publicar — não ultrapassar 120s
