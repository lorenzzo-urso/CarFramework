# Entrega 1 — Ideação (rascunho final, 10 campos)

> Gerado pela skill `hacarthon-entrega-ideacao`. Cada campo tem versão curta e
> expandida. **Reescrever com as palavras do time antes de colar na plataforma**,
> especialmente os campos 1 e 10.
>
> ⚠️ O formulário exige que as respostas reflitam o entendimento da equipe —
> use estes rascunhos como ponto de partida, não como texto final.

---

## Campo 1 — BRAINSTORM

**Versão curta**
O time partiu de 3 direções: app para o produtor, painel para o governo e
infraestrutura de dados. A ideia que venceu uniu as três — o Compadre como
prova e a Terra Comum como plataforma — porque era a única que resolvia o
individual e o coletivo ao mesmo tempo.

**Versão expandida**
No início do haCARthon, exploramos caminhos distintos: um assistente simples
para o produtor, um painel analítico para os órgãos ambientais e uma camada de
integração de dados abertos. Cada ideia resolvia parte do problema — mas nenhuma
resolvia o Desafio 1 por inteiro, que pede explicitamente "benefícios individuais
e coletivos". A virada veio quando percebemos que o problema não é falta de dados
— é falta de contexto e tradução. Os dados existem (SIGEF, MapBiomas, base SFB,
RER), mas estão fragmentados e escritos numa linguagem que o Seu Raimundo não
consegue usar. A solução escolhida foi a única que atacava os três gargalos ao
mesmo tempo: o Compadre (o assistente pelo WhatsApp, que o produtor vê) sobre a
Terra Comum (a camada semântica aberta, que o jurado ouve no pitch). Venceu
porque é a única resposta que não termina num produto fechado para uma persona
— é infraestrutura que multiplica.

> ⚠️ **Reescrever com o que realmente aconteceu:** um momento de virada, uma
> ideia descartada, quem sugeriu o quê. Isso é o que diferencia do genérico.

`[Jurado] Critério: autenticidade + pertinência | Nota estimada: 8/10 | Para subir: incluir detalhe real — nome de ideia descartada, momento de virada`

---

## Campo 2 — PROBLEMA

**Versão curta**
O Seu Raimundo recebe uma notificação do governo sobre a terra dele e não
entende uma palavra. Tem medo de multa, guarda o papel na gaveta e paga um
técnico para resolver. Enquanto isso, o crédito rural fica bloqueado. Com 8,2
milhões de imóveis no CAR, esse ciclo se repete em escala nacional.

**Versão expandida**
O CAR é pré-requisito para crédito rural, acesso a PSA, isenção fiscal e
suspensão de sanções ambientais — mas o processo de declaração e correção é
inacessível para o pequeno produtor. O Seu Raimundo recebe notificações do órgão
ambiental em linguagem técnica ("sobreposição de polígono em área de APP,
necessária retificação cadastral") e não entende o que fazer. O medo de multa
paralisa. A solução que encontra é pagar um técnico — que cobra e demora. O ciclo
de retificações se repete infinitamente porque o dado autodeclarado erra, o órgão
rejeita, o produtor não sabe corrigir. São três gargalos sobrepostos: exclusão
digital e técnica (o produtor não consegue georreferenciar APP e Reserva Legal
sozinho), ciclo infinito de retificações (vai-e-vem com os OEMAs), e ruído na
comunicação Estado-produtor (a notificação técnica gera medo em vez de
orientação). O problema é urgente: o CAR irregular bloqueia acesso ao Pronaf, ao
Programa de Regularização Ambiental e à CRA — e a raiz não é falta de informação,
é falta de contexto e tradução.

`[Jurado] Critério: Relevância do problema | Nota estimada: 8/10 | Para subir: incluir % de CARs com análise pendente — buscar no Painel de Regularização Ambiental`

---

## Campo 3 — SOLUÇÃO

**Versão curta**
O Compadre é um assistente pelo WhatsApp que traduz as notificações do CAR em
linguagem simples, prepara o produtor para cada etapa e abre o link direto na
tela certa do sistema. Por trás, a Terra Comum — camada semântica aberta que usa
as mesmas bases de dados que o analista usa para validar.

**Versão expandida**
A solução tem duas faces que trabalham juntas. O **Compadre** é o que o produtor
vê: um assistente no WhatsApp que lê a notificação do órgão, traduz em português
simples ("tem uma diferença na área perto do seu rio"), explica o que falta, e
abre o link direto na etapa certa do sistema — sem que o Raimundo precise entender
o SICAR. Ele não substitui o sistema oficial: fica na frente dele, preparando o
produtor para chegar pronto. A **Terra Comum** é o motor invisível: uma camada
semântica aberta construída sobre o RER open-source do governo, que integra SIGEF
(limites oficiais do imóvel), MapBiomas (cobertura e uso do solo), e a Base de
Referência de Uso do Solo do SFB — a mesma base que os analistas dos OEMAs usam
para validar o CAR. Ao usar a mesma base de referência nas duas pontas (produção
e validação), eliminamos a divergência que causa o ciclo de retificações. O
produtor não vê a máquina — só recebe a resposta na língua dele.

> **No vídeo, o jurado verá:** o Seu Raimundo mandando uma notificação do órgão
> pro Compadre no WhatsApp, recebendo a tradução em português simples, entendendo
> o que falta e sendo direcionado para a etapa certa do sistema.

`[Jurado] Critério: Pertinência + Inovação | Nota estimada: 9/10 | Para subir: mostrar no vídeo a cena exata de "tradução da notificação"`

---

## Campo 4 — PÚBLICO-ALVO

**Versão curta**
Pequenos e médios produtores rurais — o Seu Raimundo — que usam WhatsApp como
principal ferramenta digital e dependem de extensionistas (CATI/EMATER) para
assuntos ambientais. Escolhemos esse público porque é o mais vulnerável, o menos
atendido e onde o impacto de uma solução simples é maior.

**Versão expandida**
O público primário são pequenos e médios produtores rurais — o Seu Raimundo do
Briefing. Ele depende da propriedade para o sustento familiar, não tem domínio de
plataformas digitais, e toma decisões com base na confiança: vizinhos, sindicatos,
extensionistas agrícolas. WhatsApp é o seu canal principal — funciona em 2G, não
exige download, e já faz parte da rotina. Validamos esse perfil com um produtor
real de SP: a maior barreira não é a plataforma do SICAR, é entender o que a
regra pede. Escolhemos esse público porque é onde a mudança tem mais impacto:
cada retificação eliminada na origem reduz o retrabalho nos órgãos e libera o
acesso a benefícios que o produtor nem sabe que tem direito. O canal de
distribuição não é governo direto — é o extensionista (CATI, EMATER) e a
cooperativa, que o Raimundo já confia e que têm capilaridade nacional. Benefício
indireto: analistas dos OEMAs, que recebem cadastros mais limpos e com menos
retrabalho.

`[Jurado] Critério: Relevância | Nota estimada: 8/10 | Para subir: número de produtores rurais que usam WhatsApp vs. que já acessaram o SICAR`

---

## Campo 5 — IMPACTO

**Versão curta**
Individual: o Raimundo entende o que fazer, corrige sem pagar despachante, e
descobre que o CAR regularizado desbloqueia crédito e PSA. Coletivo: cada CAR
correto na origem reduz retificações nos órgãos, melhora a base nacional e a
mesma plataforma aberta serve governo e cooperativas.

**Versão expandida**
**Impacto individual (Seu Raimundo):** entende o que a notificação pede sem medo;
corrige o CAR sem pagar técnico; chega no sistema oficial preparado, com os dados
certos em mãos; descobre os benefícios que o CAR regularizado desbloqueia —
Pronaf Eco, PSA, CRA, suspensão de sanções. O CAR deixa de ser ameaça e vira
porta de oportunidade.

**Impacto coletivo (sistema):** cada CAR correto na origem elimina um ciclo de
retificação — menos retrabalho para os analistas dos OEMAs, dados mais confiáveis
na base nacional, melhor conformidade com o Código Florestal. E porque a Terra
Comum é uma plataforma aberta (Bem Público Digital), o impacto se multiplica:
governo usa a mesma camada para priorizar intervenção territorial; cooperativas de
crédito qualificam carteiras de crédito verde; pesquisadores e Embrapa constroem
agentes especializados. Uma única arquitetura resolve o individual e o coletivo —
que é exatamente o que o Desafio 1 pede.

`[Jurado] Critério: Pertinência (individual + coletivo é requisito explícito) | Nota estimada: 9/10 | Para subir: métrica de baseline — tempo médio atual de uma retificação no SICAR`

---

## Campo 6 — DIFERENCIAL

**Versão curta**
Outros times estão construindo um táxi. Nós estamos construindo a estrada. O
Compadre é a prova; a Terra Comum é o protocolo aberto para que qualquer agente
— de qualquer organização — entenda o território rural brasileiro.

**Versão expandida**
A resposta óbvia ao Desafio 1 é um chatbot que ajuda o Raimundo. Essa resposta
existe — e outros times vão entregá-la. Nós entregamos outra coisa: o substrato
aberto para que qualquer agente entenda o território rural. Hoje o produtor acessa
o SICAR sozinho (ou paga técnico), recebe uma notificação técnica, não entende, e
entra no ciclo de retificações. Os assistentes que existem adivinham em cima de
texto — sem rastreabilidade, sem consistência, e servindo só uma persona. O
diferencial da Terra Comum é em três camadas: (1) **Protocolo, não produto** —
uma camada semântica → múltiplos agentes → múltiplas personas. O mesmo
conhecimento serve o Compadre (produtor), o Auditor (analista do OEMA), o
Territorial (governo) e o Crédito (cooperativa). Benefícios individuais e
coletivos em uma única arquitetura. (2) **Raciocina sobre ontologia, não sobre
texto** — não é RAG. Explica o porquê, com rastreabilidade. Não existe
implementação pública de ontologia para o CAR — somos os primeiros. (3) **Sobre
a mesma infraestrutura do governo** — RER open-source e base de referência SFB.
Não recriamos do zero: ampliamos com inteligência o que já existe e é de todos.

`[Jurado] Critério: Inovação ⭐ (desempate) | Nota estimada: 9/10 | Para subir: citar o Auditor do OEMA como segundo agente — prova que a plataforma é real, não só promessa`

---

## Campo 7 — VIABILIDADE

**Versão curta**
Legal: código aberto, dados com licença CC, construído sobre o RER (DPG do
governo). Tecnológico: SIGEF, MapBiomas e base SFB já são públicos; RER roda em
Docker. Operacional: WhatsApp já é o canal do produtor; CATI/EMATER têm
capilaridade nacional.

**Versão expandida**
**Legal:** a solução é código aberto (exigência do edital atendida). Usa bases
públicas com licença Creative Commons (base SFB, MapBiomas). Construída sobre o
RER, que é Bem Público Digital do governo federal — não há conflito de propriedade
intelectual.

**Tecnológico:** todas as bases já existem e são acessíveis — SIGEF com API
pública, MapBiomas com dados históricos por estado, Base de Referência de Uso do
Solo do SFB (1,84 GB para AL, baixada e validada pela equipe), RER self-hostável
via Docker com REST API. A camada semântica usa LLM comercial disponível.
WhatsApp Business API disponível para aprovação no piloto. No hackathon:
demonstramos com interface navegável real e dados do ambiente de testes oficial
do SICAR (car-sus.dataprev.gov.br), com imóvel de teste do sistema do governo.

**Operacional:** o canal CATI/EMATER tem capilaridade nacional e já é o elo de
confiança do produtor. O módulo pré-preenchido do SICAR prova que o governo já
faz o cruzamento de dados que a solução usa — entregamos pelo canal certo.

`[Jurado] Critério: Pertinência + Inovação | Nota estimada: 8/10 | Para subir: confirmar parceiro do piloto [A CONFIRMAR — CATI ou cooperativa]`

---

## Campo 8 — IMPLEMENTAÇÃO

**Versão curta**
Hackathon: protótipo navegável do Compadre com imóvel real de teste. Piloto
(3–6 meses): Terra Comum sobre RER real + WhatsApp Business + parceiro CATI ou
cooperativa. Escala (12–24 meses): integração com CAR nacional e Agent Hub aberto
a terceiros.

**Versão expandida**
**Hackathon (agora — 2,5 dias):** interface navegável simulando WhatsApp, com
fluxo real de tradução de pendência usando imóvel do ambiente de testes oficial
do SICAR; ontologia mínima do CAR (APP, RL, biomas, parâmetros do Código
Florestal); dados da Base SFB de Alagoas pré-computados; arquitetura da Terra
Comum apresentada como diagrama no pitch.

**Piloto (3–6 meses):** Terra Comum sobre instância própria do RER com dados
reais; integração SIGEF + MapBiomas + base SFB por estado; WhatsApp Business API
com aprovação Meta; 1–2 agentes funcionais (Compadre + Auditor); parceria com
extensionista ou cooperativa para chegada ao produtor `[parceiro a confirmar]`.

**Escala (12–24 meses):** integração com o CAR nacional; Agent Hub aberto —
qualquer dev ou órgão publica agentes; primeiras assinaturas B2B (cooperativas
de crédito) e B2G (estados). A ontologia evolui como commons mantida pela
comunidade.

`[Jurado] Critério: Relevância | Nota estimada: 8/10 | Para subir: nomear o parceiro do piloto`

---

## Campo 9 — CÓDIGO ABERTO

**Versão curta**
A Terra Comum é DPG por design: ontologia + camada semântica + Agent Hub
publicados no GitHub com licença aberta. Qualquer estado ou país que use o RER
pode rodar a Terra Comum em cima. É o Android do domínio CAR — qualquer um
publica agentes na mesma plataforma.

**Versão expandida**
A Terra Comum não é um app que pode ser compartilhado — é infraestrutura que foi
desenhada para ser pública desde o primeiro dia. O núcleo (ontologia + camada
semântica + Agent Hub) será publicado no GitHub com licença Apache 2.0. Qualquer
estado brasileiro que queira adaptar a solução ao seu contexto pode fazer isso;
qualquer país com legislação ambiental similar pode criar a ontologia do seu
código florestal e reutilizar o mesmo Agent Hub. A ontologia será alinhada ao
AGROVOC (vocabulário agrícola da FAO) e às bases da Embrapa (OntoAgroHidro,
Agrotermos) — facilitando reutilização internacional e colaboração com
instituições já reconhecidas. O efeito-rede é estrutural: quanto mais organizações
contribuem com agentes e dados, melhor o modelo para todos — o incentivo à adoção
está na arquitetura. É o "Android do domínio CAR": qualquer desenvolvedor, órgão
ou pesquisador publica agentes na mesma plataforma e parte do mesmo conhecimento
base. Construído sobre o RER — que é ele mesmo um Bem Público Digital — a Terra
Comum é a camada de inteligência que o RER não tem, e que qualquer instância do
RER no mundo pode adotar.

`[Jurado] Critério: Inovação | Nota estimada: 9/10 | Para subir: mencionar um país ou organização internacional concreta onde isso faria sentido (ex: Bolívia, Colômbia — também têm CAR equivalente)`

---

## Campo 10 — MENTORIA E FEEDBACK

> ⚠️ **Este campo exige ação humana — não é gerado.** Conversar com pelo menos
> 1 mentor é obrigatório. Entregar sem este campo **elimina pontos**.

Quando tiverem o feedback, pedir para formatar com a estrutura abaixo:

```
Nome: [nome completo, organização]

Feedback recebido:
- [ponto 1]
- [ponto 2]
- [ponto 3 se houver]

O que ajustamos:
- [decisão tomada pelo time]
```

---

## Autoavaliação — olhar do jurado

| Campo | Critério | Nota est. | Ação prioritária |
|---|---|---|---|
| 1. Brainstorm | Autenticidade | 8/10 | **Reescrever com o que aconteceu de verdade** |
| 2. Problema | Relevância | 8/10 | Buscar % de CARs pendentes no Painel BI |
| 3. Solução | Pertinência + Inovação | 9/10 | Provar no vídeo a cena de tradução |
| 4. Público-alvo | Relevância | 8/10 | Dado de uso de WhatsApp no agro |
| 5. Impacto | Pertinência | 9/10 | Métrica de baseline de retificação |
| 6. Diferencial | Inovação ⭐ | 9/10 | Citar o Auditor como 2º agente |
| 7. Viabilidade | Pertinência | 8/10 | Confirmar parceiro do piloto |
| 8. Implementação | Relevância | 8/10 | Confirmar parceiro do piloto |
| 9. Código Aberto | Inovação | 9/10 | Nomear país/org. internacional |
| 10. Mentoria | — | ⚠️ 0 se faltar | **Fazer a mentoria o quanto antes** |
| **Média** | | **8,4/10** | |

**3 ações que mais sobem a média:**
1. Reescrever o campo 1 com o que realmente aconteceu no time
2. Fazer a mentoria (campo 10) — é o que mais arrisca a nota
3. Buscar o % de CARs pendentes para ancorar o campo 2
