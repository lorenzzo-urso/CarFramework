# ENTREGA 1 - IDEAÇÃO

> Versão oficial redigida pela equipe — submetida na plataforma haCARthon.
> Manter separada de `1-ideacao.md` (versão gerada pela IA) para comparação.

## Número da equipe

229

## Desafio escolhido

Desafio 1: Simplificar o CAR para o usuário.

Escolhemos esse desafio porque nosso foco é facilitar a jornada de quem está na ponta: o agricultor. A solução também conversa com dados geoespaciais e legislação ambiental, só que esses pontos entram como camadas de apoio para simplificar a experiência do usuário.

## 1. BRAINSTORM

A equipe começou o haCARthon olhando para uma pergunta simples: se o CAR já existe, por que tantos agricultores ainda sentem medo, insegurança e dificuldade para lidar com ele?

No começo, surgiram várias ideias. Pensamos em criar um assistente para tirar dúvidas do produtor, um painel para técnicos e analistas, uma ferramenta para organizar documentos ambientais, uma integração com APIs de consulta do CAR e uma solução educativa para traduzir o Código Florestal.

A pesquisa com agricultores mudou nossa visão. Todos os respondentes já possuíam CAR. Isso mostrou que a maior dificuldade estava em entender regras, organizar documentos, reduzir custos, acompanhar mudanças e ter segurança para agir corretamente.

Também percebemos que já existem APIs e bases capazes de consultar dados importantes sobre CAR, bioma, aptidão agrícola, score e território rural. A lacuna está em transformar essas consultas em orientação prática para o agricultor.

A ideia escolhida foi construir o CarFramework: um protocolo aberto, agnóstico a plataformas, com uma ontologia do CAR como núcleo, um hub de agentes, agentes nativos e um padrão de integração para APIs e agentes criados por terceiros.

O primeiro agente nativo é o Compadre, criado para conversar com o agricultor em linguagem simples. Ele é a parte mais visível da solução, porque aparece no WhatsApp ou no widget de chat. O valor central, porém, está na Terra Comum: uma camada semântica que organiza conceitos, regras, relações, dados e evidências do CAR por meio de ontologia.

Essa ideia venceu porque une uma experiência simples para o agricultor com uma infraestrutura reutilizável para todo o ecossistema. O Seu Raimundo pode entrar no hub da sua comunidade, abrir o Compadre para entender o CAR e acessar outros agentes criados por técnicos ou parceiros, como em uma loja de agentes do território.

A lógica é parecida com o Android. O valor está na plataforma que permite que muitas pessoas criem soluções diferentes, para problemas diferentes, sobre uma base comum. O Compadre prova que o protocolo funciona. A Terra Comum é o protocolo.

## 2. PROBLEMA

O problema que queremos resolver é a dificuldade de pequenos agricultores para entender, manter, corrigir e usar o CAR com segurança, mesmo quando já possuem o cadastro.

Na pesquisa com agricultores, todos os respondentes já possuíam CAR. Isso mostrou que a dor principal está em compreender o que o cadastro significa, manter a documentação organizada, lidar com regras ambientais, acompanhar mudanças, reduzir custos e saber qual próximo passo tomar.

Esse recorte é muito importante no contexto da CSA Brasil. A CSA trabalha com uma relação de confiança entre agricultores e coagricultores. A comunidade sustenta a produção, valoriza alimento saudável, agroecologia, permanência no campo e cuidado com a terra. Nesse modelo, o agricultor precisa produzir, organizar entregas, prestar contas, participar de editais, lidar com certificações, manter registros e acompanhar exigências ambientais.

Os produtores da pesquisa atuam em São Paulo, Pernambuco, Rio Grande do Sul, Bahia e Minas Gerais. As propriedades variam de até 10 hectares a áreas acima de 100 hectares. As atividades incluem agrofloresta, agricultura, silvicultura, café, hortaliças, frutas, plantas medicinais, sistemas agroflorestais, produção orgânica e educação.

Mesmo com realidades diferentes, as dores se repetem. As principais preocupações citadas foram falta de informação, custos, multas e mudanças nas regras. Ao lidar com documentação ambiental, apareceram dificuldades como entender regras, acessar informações, enfrentar burocracia, lidar com portal pouco funcional e ter segurança sobre o que precisa ser feito.

A pesquisa também mostrou que o WhatsApp é a principal ferramenta digital usada por todos os produtores respondentes. Muitos também usam email, Google Maps e planilhas. Isso mostra que a solução precisa nascer em canais simples e familiares.

Durante a análise de soluções existentes, encontramos outro ponto relevante. Já existem APIs e serviços para consultar dados do CAR e do território rural. A lacuna está na camada de uso. As APIs entregam dados, enquanto o agricultor precisa de contexto, tradução, confiança e próximo passo.

Assim, o problema tem duas camadas. Para o agricultor, falta uma experiência simples para entender o CAR, organizar documentos e agir com segurança. Para o ecossistema, falta um protocolo comum para transformar APIs, dados públicos, ontologias e conhecimento técnico em agentes úteis dentro das comunidades.

Esse problema importa porque o CAR é base para regularização ambiental, crédito rural, PSA, editais, certificações, segurança jurídica e cumprimento do Código Florestal. No contexto CSA, ele também pode virar uma ponte entre cuidado com a terra, transparência para a comunidade, fortalecimento da agricultura ecológica e geração de oportunidades para quem produz alimento saudável.

## 3. SOLUÇÃO

A solução proposta é o CarFramework, um protocolo aberto e agnóstico a plataformas para simplificar a criação de agentes relacionados ao CAR e ao território rural.

O núcleo do CarFramework é a ontologia. Ela modela as regras do Código Florestal uma vez só, organizando conceitos como APP, Reserva Legal, biomas, documentação, regularização, benefícios, crédito rural, PSA e certificações.

A ontologia resolve a camada da verdade. A camada semântica expõe essa verdade como protocolo. O hub permite que técnicos, desenvolvedores, cooperativas, órgãos públicos e comunidades publiquem agentes sobre essa base.

Isso simplifica a construção de novos agentes. O desenvolvedor foca no comportamento do agente e no problema que deseja resolver. A regra, o conceito e a estrutura do CAR já estão organizados no grafo.

O primeiro agente nativo é o Compadre. Ele conversa com o agricultor em linguagem simples, por WhatsApp ou widget de chat, ajudando a entender dúvidas, notificações, documentos, regras ambientais e próximos passos relacionados ao CAR.

O hub organiza esses agentes como uma loja de agentes do território. Uma comunidade como a CSA Brasil pode ter seu próprio hub. Nele, o agricultor encontra agentes para CAR, documentação ambiental, APP, Reserva Legal, editais, certificações, crédito rural, PSA e regularização.

O CarFramework também permite que a linguagem dos agentes seja adaptada ao contexto de cada comunidade. Uma CSA pode falar de alimento saudável, coagricultores, cuidado com a terra e transparência. Um assentamento pode falar de permanência no campo e organização coletiva. Uma comunidade quilombola pode adaptar a linguagem para sua história, vocabulário e relação com o território.

O protocolo é agnóstico de canal. O mesmo agente pode rodar no WhatsApp, no app de um banco, no portal de um governo, no site de uma cooperativa ou em uma API. O conhecimento permanece o mesmo. A janela de acesso muda conforme a realidade do usuário.

A solução também propõe uma camada de reputação interoperável integrada ao login do hub. Interações relevantes podem gerar tokens blockchain, registrando participação, aprendizado, validações, uso de agentes e contribuições. Essa reputação pode acompanhar agricultores, técnicos e comunidades entre diferentes hubs, criando histórico verificável para editais, certificações, PSA, crédito rural e programas de incentivo.

## 4. PÚBLICO-ALVO

O público-alvo principal são pequenos e médios agricultores rurais ligados à agroecologia, agricultura familiar, sistemas agroflorestais, produção orgânica e redes como a CSA Brasil.

Escolhemos esse público porque ele vive uma combinação intensa de responsabilidades. Precisa produzir alimento saudável, cuidar da terra, manter relação com a comunidade, organizar entregas, buscar editais, lidar com certificações, manter documentação e acompanhar exigências ambientais.

Na pesquisa, os respondentes atuam com agrofloresta, educação, agricultura, silvicultura, café, hortaliças, frutas, plantas medicinais, PANCs, sistemas agroflorestais e produção orgânica. Alguns fazem parte de associação, movimento de pequenos agricultores, coletivo ou CSA. Isso mostra aderência a agricultores conectados a práticas regenerativas, produção comunitária e cuidado territorial.

Também se beneficiam técnicos e extensionistas, que podem reduzir dúvidas repetitivas e atender casos com melhor contexto. Cooperativas e associações podem oferecer agentes padronizados para seus membros. Comunidades CSA ganham transparência sobre documentação, território e cuidado ambiental. Órgãos ambientais recebem informações com melhor organização. Desenvolvedores e empresas de API ganham um canal para transformar serviços técnicos em agentes utilizáveis. Bancos, seguradoras e programas de incentivo podem consultar agentes especializados para apoiar crédito rural, PSA e análise territorial.

Começamos pelo agricultor porque ele está na ponta da dor. Ao mesmo tempo, a arquitetura já nasce preparada para atender outros públicos que constroem sobre a mesma base: técnicos, analistas, órgãos públicos, cooperativas, bancos, seguradoras, universidades e desenvolvedores.

## 5. IMPACTO

Para o agricultor, o impacto esperado é transformar o CAR de uma fonte de medo e burocracia em uma ferramenta de organização, regularização e acesso a oportunidades.

O agricultor passa a entender regras ambientais em linguagem simples, organizar documentos da propriedade, preparar informações para técnicos, participar de editais, avançar em certificações e acessar melhor oportunidades como crédito rural, PSA e programas de incentivo.

Para comunidades CSA e redes agroecológicas, o impacto esperado é aumentar a transparência sobre o cuidado com o território. A comunidade que sustenta a produção pode enxergar o CAR como parte de uma jornada de regeneração, confiança, permanência no campo e valorização do agricultor.

Para o CAR e os órgãos ambientais, o impacto esperado é melhorar a qualidade das informações desde a origem. Agricultores melhor orientados geram cadastros com contexto, reduzem retrabalho e ajudam a tornar a regularização ambiental mais fluida.

Para técnicos, o impacto é reduzir tarefas repetitivas. Em vez de explicar os mesmos conceitos várias vezes, eles podem transformar conhecimento em agentes e focar nos casos que exigem análise especializada.

Para desenvolvedores e empresas de API, o impacto é criar um caminho para que serviços técnicos cheguem ao usuário final. Uma API de consulta pode virar um agente útil dentro do hub.

Para o ecossistema, o impacto é ainda maior. A partir da Terra Comum, mil agentes podem resolver mil problemas do território: crédito rural, licenciamento, carbono, seguro agrícola, fiscalização, regularização, certificações e planejamento rural. Cada agente pode ser escrito por quem entende daquele problema, usando o mesmo modelo de conhecimento.

Em escala, o CarFramework pode se tornar uma infraestrutura cognitiva do território rural.

## 6. DIFERENCIAL

O principal diferencial do CarFramework é colocar a ontologia no centro da solução.

Hoje, muitas soluções dependem de textos soltos, prompts, atendimentos manuais, vídeos, manuais, consultorias ou APIs isoladas. Esses recursos ajudam, só que cada um interpreta o CAR de uma forma e fica difícil manter tudo atualizado.

O CarFramework faz diferente porque cria uma camada comum de conhecimento. A ontologia organiza conceitos como APP, Reserva Legal, déficit, retificação, pendência, documentação, crédito rural, PSA, certificação, regularização, biomas e benefícios.

Com essa base, novos agentes podem ser criados com maior velocidade, menor custo e melhor consistência. Quando uma regra muda, a atualização acontece na ontologia e os agentes que dependem dela passam a trabalhar com a nova referência.

O Compadre é a parte mais visível. Ele prova que a experiência funciona. O valor estrutural está na Terra Comum, porque ela permite que outros agentes sejam criados por diferentes atores, para diferentes problemas, usando o mesmo modelo.

Outro diferencial é permitir que os agentes sejam publicados dentro dos portais das próprias comunidades. Isso torna o agente mais próximo, confiável e contextual. A mesma dúvida sobre CAR pode ser explicada com a linguagem de uma CSA, de uma cooperativa, de um assentamento, de uma comunidade quilombola ou de uma associação rural.

O framework também é agnóstico a plataformas. Pode rodar em servidores públicos, sites oficiais, portais comunitários, WhatsApp, widgets de chat, aplicativos de bancos e sistemas parceiros. Isso permite soberania de dados, adoção por diferentes estados e adaptação por comunidades.

A camada de reputação interoperável também diferencia a proposta. O hub pode registrar interações relevantes por meio de tokens blockchain vinculados ao login do usuário. Assim, ações dispersas viram histórico verificável de participação, aprendizado, contribuição e avanço na jornada ambiental.

A diferença central é entre produto e infraestrutura. Produto atende uma persona. Infraestrutura permite que qualquer pessoa crie soluções em cima dela.

## 7. VIABILIDADE

A solução é viável em termos legais, tecnológicos, operacionais e econômicos, desde que comece com um MVP bem definido.

Do ponto de vista legal, o CarFramework atua como apoio informativo, educativo e organizacional. Ele orienta o agricultor, ajuda a organizar documentos e traduz conceitos do CAR em linguagem simples. A responsabilidade técnica segue com profissionais habilitados, órgãos ambientais e canais oficiais. A solução deve deixar claro quando uma resposta é orientação geral, quando existe evidência consultada e quando o agricultor precisa buscar apoio técnico.

Também é importante seguir princípios de LGPD. Dados sensíveis da propriedade devem ficar protegidos. O login do hub pode controlar permissões de acesso. A camada de tokens deve registrar eventos verificáveis da jornada, como conclusão de etapas, participação e validações, preservando dados privados da propriedade.

Do ponto de vista tecnológico, a viabilidade é alta porque o framework pode começar simples. O MVP precisa de quatro peças principais: ontologia inicial da Terra Comum, com conceitos prioritários de CAR, APP e Reserva Legal; Compadre como agente nativo para linguagem simples; widget de chat instalado em portal de comunidade; fluxos guiados para dúvidas, documentação e próximos passos.

A partir dessa base, entram novas camadas: WhatsApp, APIs externas, agentes criados por técnicos, instalação em servidores públicos e reputação interoperável.

Do ponto de vista operacional, o caminho mais viável é começar por uma comunidade parceira, como CSA Brasil, cooperativa ou associação. O hub aparece dentro de um ambiente que o agricultor já reconhece. Isso aumenta confiança e facilita adoção. Técnicos da comunidade podem ajudar a validar respostas, criar agentes simples e indicar ajustes de linguagem.

Do ponto de vista econômico, protocolo aberto ainda tem custo de operação. Os principais custos esperados são desenvolvimento do hub, widget, agente Compadre e ontologia inicial; hospedagem, banco de dados, logs e monitoramento; uso de IA para conversas e interpretação de dúvidas; integração com WhatsApp Business, caso esse canal seja ativado; integrações com APIs públicas e privadas; curadoria da ontologia e atualização das regras; revisão técnica e jurídica das respostas; suporte aos usuários e treinamento de técnicos; governança do repositório aberto e da comunidade de contribuidores.

Para o MVP, a equipe pode reduzir custos começando com widget web, base inicial da Terra Comum e poucos fluxos prioritários. WhatsApp, tokens e loja de agentes entram depois, conforme validação e recursos disponíveis.

Quem pode pagar essa conta: comunidades, cooperativas e associações podem manter hubs para seus membros; prefeituras e órgãos públicos podem instalar o protocolo em servidores próprios para atendimento ao cidadão; editais, fundos climáticos e inovação pública podem financiar a fase inicial; desenvolvedores e empresas de API podem publicar agentes pagos por uso, assinatura ou contrato com organizações; agricultores podem acessar agentes essenciais de forma gratuita dentro da comunidade, enquanto serviços especializados podem ter cobrança definida pelo operador do hub.

Assim, o modelo combina bem público digital com sustentabilidade operacional. O core aberto permite reuso e auditoria. A operação local pode ser financiada por organizações que se beneficiam da melhoria da jornada do CAR.

## 8. IMPLEMENTAÇÃO

A implementação deve começar com um MVP pequeno, claro e útil.

O MVP sugerido após a mentoria é: Compadre em widget de chat, dentro de um portal comunitário, usando uma base inicial da Terra Comum para responder dúvidas sobre CAR, APP, Reserva Legal e documentação ambiental.

Esse recorte evita dispersão e ajuda a banca a visualizar a primeira entrega real.

### Etapa 1: Preparação do MVP, 2 semanas

A equipe define o escopo inicial: público prioritário, temas principais, canal inicial, agente inicial, core técnico e critérios de segurança.

O público prioritário são pequenos agricultores ligados à CSA Brasil ou comunidade parceira. Os primeiros temas são CAR, APP, Reserva Legal, documentação e próximos passos. O canal inicial é widget de chat em portal da comunidade. O agente inicial é o Compadre. O core técnico é a ontologia inicial da Terra Comum.

Nesta etapa, a equipe também define quem revisa o conteúdo: técnico ambiental, especialista jurídico e representante da comunidade.

### Etapa 2: Construção da Terra Comum inicial, 3 a 4 semanas

A equipe organiza a ontologia inicial do CAR. Essa etapa é o centro do framework.

A ontologia deve mapear conceitos principais como CAR, APP, Reserva Legal, imóvel rural, déficit, retificação, documentação e regularização. Também deve mapear relações entre conceitos, fontes de referência, linguagem comunitária e limites da resposta.

Essa etapa facilita a criação de novos agentes no futuro. Em vez de cada agente começar do zero, todos usam a mesma base conceitual atualizada.

### Etapa 3: Construção do Compadre, 3 a 4 semanas

Com a ontologia inicial pronta, a equipe desenvolve o Compadre como primeiro agente nativo.

O Compadre deve ser capaz de receber dúvidas do agricultor, explicar termos técnicos em linguagem simples, montar checklist básico de documentação, orientar próximos passos, sugerir quando buscar técnico, adaptar linguagem ao contexto da comunidade e registrar dúvidas frequentes para melhorar a Terra Comum.

A primeira versão deve focar em conversas simples e úteis.

### Etapa 4: Widget e hub comunitário, 2 a 3 semanas

A equipe instala o widget de chat em um portal comunitário ou ambiente de demonstração.

O hub deve mostrar o agente Compadre disponível, explicação simples sobre o que ele faz, termos de uso e privacidade, login básico do usuário, registro de interações essenciais e possibilidade futura de novos agentes.

O objetivo é que o agricultor acesse a solução em um ambiente familiar, como portal de CSA, cooperativa, associação ou prefeitura.

### Etapa 5: Teste com agricultores e técnicos, 2 semanas

A equipe testa o MVP com um grupo pequeno de agricultores e técnicos.

As métricas iniciais são: quantidade de dúvidas respondidas, termos que geraram maior confusão, tempo para o usuário entender o próximo passo, respostas que precisaram de revisão técnica, temas que devem virar novos agentes e adequação da linguagem à comunidade.

Com esses dados, a equipe ajusta a ontologia, o Compadre e os fluxos do hub.

### Evolução pós MVP, 3 a 6 meses

Depois do primeiro teste, entram novas camadas: WhatsApp como canal de acesso e alerta; agente de documentação ambiental; agente de APP e Reserva Legal; agente de editais e oportunidades; primeiras APIs conectadas; painel simples para técnicos; login com reputação inicial; manual para criação de agentes por terceiros.

### Fase de sustentação, 12 a 24 meses

Na fase de sustentação, o CarFramework evolui como ecossistema aberto.

As atividades principais são governança da ontologia, revisão periódica de regras e fontes, curadoria de agentes publicados, suporte para comunidades instalarem seus hubs, integração com servidores públicos, criação de biblioteca de agentes reutilizáveis, modelo econômico para manter infraestrutura, IA, revisão técnica e suporte, e reputação interoperável por tokens integrada ao login do hub.

A estratégia de adoção começa por comunidades organizadas, como CSA Brasil, cooperativas e associações. Depois pode avançar para prefeituras, órgãos ambientais, redes de assistência técnica, bancos e universidades.

## 9. CÓDIGO ABERTO

O CarFramework nasce como protocolo aberto para evoluir como Bem Público Digital.

Como Bem Público Digital, o ativo principal a ser aberto é a ontologia. Ela é o core do framework e permite que diferentes organizações criem agentes sobre a mesma base de conhecimento, com liberdade para adaptar linguagem, canais e fluxos ao seu território.

A solução pode ser publicada com licença aberta, incluindo ontologia inicial do CAR, documentação dos conceitos e relações, regras e referências legais rastreáveis, padrão de manifesto para criação de agentes, agente nativo Compadre como exemplo, código do hub de agentes, widget de chat instalável, guias para técnicos criarem agentes, guias para desenvolvedores conectarem APIs, modelo de instalação em servidores públicos, camada opcional de reputação por tokens e guia para adaptação de linguagem por comunidades.

A ideia é permitir que cada comunidade tenha seu próprio hub de agentes. Uma CSA pode oferecer agentes para seus agricultores. Uma cooperativa pode ativar agentes de crédito e documentação. Um órgão ambiental pode publicar agentes de orientação. Uma universidade pode contribuir com agentes educativos. Um desenvolvedor pode conectar uma API e disponibilizar um agente para uso por agricultores e organizações.

Como protocolo aberto, o CarFramework permite que estados, municípios, cooperativas, associações, comunidades quilombolas, assentamentos e outros países adaptem a solução para suas regras, seus dados e sua realidade territorial.

A camada de reputação interoperável amplia esse potencial. Usuários, técnicos e comunidades podem carregar histórico verificável entre hubs diferentes, sempre com controle sobre permissões e dados sensíveis.

## 10. MENTORIA E FEEDBACK DA SOLUÇÃO

Nome do mentor:

Carlos [preencher sobrenome e organização]

Resumo do feedback recebido:

Apresentamos ao Carlos a proposta do CarFramework como protocolo aberto, agnóstico a plataformas, com hub de agentes para simplificar a jornada do CAR. Também explicamos o Compadre como primeiro agente nativo, a Terra Comum como ontologia central, a integração com APIs existentes, o uso em portais comunitários e a proposta de reputação interoperável por tokens.

O Carlos avaliou que a proposta de valor é forte, principalmente porque o projeto vai além de um chatbot e propõe um protocolo aberto que pode ser instalado em portais de comunidades, prefeituras, órgãos públicos ou parceiros.

Ele também considerou forte a ideia do Compadre como primeiro agente nativo, pois traduz dúvidas do CAR em linguagem simples e aproxima o agricultor de temas como documentação ambiental, APP, Reserva Legal, editais, certificações, crédito rural e regularização.

O principal ponto de atenção foi aprofundar o apelo comercial e econômico, além do processo de implementação. Carlos recomendou detalhar melhor quem é o usuário principal, quem paga a conta, quais custos existem e como o projeto se sustenta ao longo do tempo.

Ele também sugeriu definir um MVP mais objetivo, começando pelo widget do Compadre, uma base inicial da Terra Comum e fluxos prioritários sobre CAR, APP e Reserva Legal, antes da expansão para novos agentes.

Outro ponto importante foi a governança da ontologia. Como a ontologia é o core do framework, a equipe precisa explicar quem atualiza regras, quem valida mudanças, quem revisa respostas e como os agentes seguem alinhados com a realidade.

O que a equipe decidiu ajustar:

A partir do feedback, definimos o agricultor como usuário final principal. Também definimos comunidades, cooperativas, prefeituras e órgãos públicos como operadores possíveis do hub. Técnicos, universidades, órgãos públicos e desenvolvedores entram como criadores de agentes.

Reforçamos que a ontologia é o core do CarFramework. O Compadre é o primeiro agente nativo. O hub é o espaço de distribuição. Widget, WhatsApp, APIs e tokens são camadas de acesso, integração e reputação.

Também reduzimos o MVP para widget do Compadre, Terra Comum inicial e fluxos de CAR, APP e Reserva Legal. A partir disso, vamos detalhar custos de IA, hospedagem, WhatsApp, APIs, revisão técnica, revisão jurídica e curadoria da ontologia.

Por fim, incluímos caminhos de financiamento, estratégia de adoção por comunidades organizadas e governança da ontologia como parte essencial da sustentação.

Com esses ajustes, a equipe passou a apresentar o CarFramework de forma mais simples e convincente: a ontologia é o core, o Compadre é o primeiro uso prático, o hub é a forma de distribuir agentes e a comunidade é o lugar onde o agricultor acessa ajuda em linguagem próxima da sua realidade.
