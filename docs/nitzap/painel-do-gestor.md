# 07. Painel do gestor (Agent Monitor)

O Painel do gestor mostra, em uma tela só, o que está acontecendo no atendimento do WhatsApp: as conversas de cada conexão, quem está atendendo agora, quem está esperando resposta, os números do período e o desempenho de cada agente. O gestor acompanha qualquer conversa em tempo real sem que o cliente perceba e, se for administrador, pode sussurrar para o agente, transferir, encerrar ou abrir um atendimento.

O painel trabalha com os atendimentos do Nitzap. Para entender como eles abrem, passam de mão e fecham, veja o guia de [Atendimento](atendimento.md).

<!-- sumario:inicio -->
**Neste artigo:**

- [Onde fica o painel](#nitzap/painel-do-gestor/onde-fica-o-painel)
- [Quem vê o quê](#nitzap/painel-do-gestor/quem-ve-o-que)
- [O topo do painel](#nitzap/painel-do-gestor/o-topo-do-painel)
- [Os filtros](#nitzap/painel-do-gestor/os-filtros)
- [Aba Chats](#nitzap/painel-do-gestor/aba-chats)
- [Aba Ao vivo](#nitzap/painel-do-gestor/aba-ao-vivo)
- [Aba Atendimentos](#nitzap/painel-do-gestor/aba-atendimentos)
- [Aba Equipe](#nitzap/painel-do-gestor/aba-equipe)
- [Acompanhar uma conversa](#nitzap/painel-do-gestor/acompanhar-uma-conversa)
- [Problemas comuns](#nitzap/painel-do-gestor/problemas-comuns)

<!-- sumario:fim -->

## Onde fica o painel

O painel é a aba **Nitzap - Painel do Gestor**. Ela vem liberada para os usuários do Nitzap, mas não aparece sozinha na barra do aplicativo: procure por **Painel do Gestor** no **Iniciador de aplicativos** (os nove pontinhos) ou peça ao administrador para incluir a aba na navegação do app.

<!-- PRINT 1: Iniciador de aplicativos com a busca "Painel do Gestor" (ou a aba já na barra do app). -->

## Quem vê o quê

| Usuário | O que vê | O que pode fazer |
| --- | --- | --- |
| **Administrador** (perfil de administrador do Salesforce ou administrador do Nitzap) | Todas as conexões e todos os atendimentos. | Acompanhar, **sussurrar**, **transferir**, **encerrar** e **abrir atendimento** pelo painel. |
| **Demais usuários** | Só as conversas das conexões em que é membro. Com **Respeitar Hierarquia** ligado, vê os próprios atendimentos, os de quem está abaixo dele na hierarquia e os das suas filas; desligado, os de toda a equipe. | Só acompanhar. |

Para quem não é administrador, o painel mostra um aviso no topo explicando esse alcance. A opção **Respeitar Hierarquia** fica em **Nitzap Config** > **Configuração** > **Preferências**; quem tem a permissão **Nitzap: Ver todas as conversas** vê toda a equipe mesmo com ela ligada.

<!-- PRINT 2 (opcional): aviso azul "Você vê os seus atendimentos..." visto por um usuário que não é administrador. -->

## O topo do painel

<!-- PRINT 3: topo do painel com as abas (Chats, Ao vivo, Atendimentos, Equipe), o indicador "Ao vivo" e o botão Atualizar. -->

| O que é | Para que serve |
| --- | --- |
| **Abas** | **Chats**, **Ao vivo**, **Atendimentos** e **Equipe**, explicadas abaixo. **Ao vivo** mostra quantos atendimentos estão abertos; **Atendimentos**, quantos houve no período. |
| **Indicador ao vivo** | Nas abas Chats e Ao vivo, mostra se o painel está recebendo as mensagens na hora: **Ao vivo · tempo real**, **Ao vivo · tempo real nas suas conexões** ou o horário da última atualização. Nas outras abas aparece **Base do CRM**, porque os números vêm das Tarefas de atendimento. |
| **Atualizar** | Recarrega tudo na hora. |

O painel também se atualiza sozinho: as mensagens chegam em tempo real, a lista de atendimentos abertos e as conexões são relidas a cada minuto e os números do período, a cada 5 minutos.

## Os filtros

A barra de filtros aparece nas abas **Ao vivo**, **Atendimentos** e **Equipe**. A aba **Chats** tem filtros próprios.

<!-- PRINT 4: barra de filtros na aba Atendimentos (Período, De, Até, Agente ou fila, Conexão, Status, Buscar, Limpar). -->

| Filtro | O que faz |
| --- | --- |
| **Período** | **Hoje**, **7 dias**, **30 dias** ou **90 dias**, ou datas livres em **De** e **Até**. Só nas abas Atendimentos e Equipe. O navegador lembra o último período escolhido. |
| **Agente ou fila** | Escolha o **Tipo** (**Usuário** ou **Fila**) e busque o nome. |
| **Conexão** | Mostra só um número de WhatsApp. |
| **Status** | **Aberta** ou **Finalizada**. Só na aba Atendimentos. |
| **Buscar** | Procura por contato, empresa ou número. |
| **Limpar** | Volta para os últimos 7 dias, sem filtros. |

## Aba Chats

Mostra todas as conversas de uma conexão, como a lista do WhatsApp, com ou sem atendimento. É a aba que abre primeiro.

<!-- PRINT 5: aba Chats com o seletor de conexão, os filtros rápidos, a busca e a lista de conversas. -->

Escolha a conexão no seletor; o painel começa pela primeira em ordem alfabética e depois lembra a última escolhida. Ao lado ficam:

- **Filtros rápidos:** **Todas**, **Não lidas**, **Sem atendimento**, **Em atendimento** e **Grupos**. Eles filtram as conversas já carregadas na tela.
- **Buscar nome ou número:** procura em toda a conexão, a partir de 3 letras.
- **Carregar mais 100:** traz as conversas mais antigas.

| Coluna | O que mostra |
| --- | --- |
| **Contato** | Nome e, embaixo, o tipo de registro e a empresa. Número sem cadastro aparece com **#**; grupo, com o ícone de grupo. |
| **Última mensagem** | O começo da última mensagem. **↓** quando foi do contato, **↑** quando foi da equipe. |
| **Quando** | Horário da última mensagem. |
| **Não lidas** | Mensagens do contato que ninguém leu. |
| **Situação** | Veja a tabela abaixo. |
| **Último atendente** | O último usuário que mandou mensagem nessa conversa. |
| **Ações** | O olho abre a conversa no [painel lateral](#nitzap/painel-do-gestor/acompanhar-uma-conversa). |

| Situação | Quando aparece |
| --- | --- |
| **Em atendimento · (nome)** | Há um atendimento aberto com esse usuário. |
| **Na fila · (fila)** | Há um atendimento aberto esperando na fila. |
| **Sem atendimento** | O contato está no CRM, escreveu por último, tem mensagens não lidas e ninguém abriu atendimento. |
| **Sem cadastro no CRM** | O número não está em nenhum registro do Salesforce. |
| **Grupo** | Conversa de grupo. |

Quando chega uma mensagem, a conversa sobe para o topo da lista e fica destacada por um instante.

Conversa de número **sem cadastro no CRM** e sem atendimento aberto não mostra o texto da última mensagem (aparece **oculta**) e não abre no painel.

## Aba Ao vivo

Mostra o que precisa de atenção agora: todos os atendimentos abertos e as conversas em que o cliente escreveu e ninguém assumiu.

### Os indicadores

<!-- PRINT 6: os cartões do topo da aba Ao vivo. -->

| Indicador | O que conta |
| --- | --- |
| **Conversas abertas** | Atendimentos abertos e quantos agentes estão envolvidos. |
| **Aguardando na fila** | Atendimentos na fila, sem agente responsável. |
| **Sem atendimento** | Conversas em que o cliente escreveu e ninguém assumiu, nas últimas 48 horas. |
| **Clientes aguardando resposta** | Atendimentos em que o cliente falou por último, com o total de mensagens não lidas. |
| **Maior espera do cliente** | A espera mais longa entre quem está na fila, sem atendimento ou sem resposta do agente. |
| **Aguardando o contato** | Atendimentos em que o agente falou por último. |
| **Paradas há mais de 24h** | Atendimentos sem movimento há mais de um dia: candidatos a encerrar. |
| **Conexões no ar** | Quantas conexões estão conectadas. Se alguma cair, o cartão avisa que ninguém recebe mensagens por ela. |

Os cartões ficam destacados quando pedem atenção, por exemplo quando há conversas na fila ou conexões fora do ar. Os de espera mudam de cor conforme o tempo: amarelo depois de 2 minutos e vermelho depois de 10.

### A lista

<!-- PRINT 7: a lista da aba Ao vivo com os filtros rápidos e algumas situações diferentes. -->

Os filtros rápidos são **Todas**, **Cliente esperando**, **Sem atendimento**, **Na fila**, **Aguardando contato** e **Paradas +24h**. A lista põe primeiro os clientes que estão esperando, da espera mais longa para a mais curta.

| Coluna | O que mostra |
| --- | --- |
| **Contato** | Nome, tipo de registro e empresa. |
| **Agente** | Quem está com o atendimento e o papel dele, ou a fila. |
| **Situação** | Veja a tabela abaixo. |
| **Não lidas** | Mensagens do cliente que o agente ainda não leu. |
| **Espera** | Há quanto tempo a conversa está parada na situação atual. Na fila, conta desde que entrou na fila; nos demais, desde a última mensagem. |
| **Desde** | Quando o atendimento abriu (ou, sem atendimento, quando chegou a última mensagem). |
| **Conexão** | O número de WhatsApp. |
| **Ações** | O olho abre a conversa no painel lateral. |

| Situação | O que significa |
| --- | --- |
| **Na fila** | Ninguém puxou ainda. |
| **Aguardando agente** | O cliente falou por último ou tem mensagem não lida. Fica verde até 2 minutos, amarela até 10 e vermelha depois disso. |
| **Aguardando contato** | O agente respondeu e a conversa espera o cliente. |
| **Parada +24h** | Mais de um dia sem movimento. |
| **Em andamento** | Atendimento aberto ainda sem mensagens para avaliar, ou a última mensagem foi uma nota interna. |
| **Sem atendimento** | O cliente escreveu e ninguém abriu atendimento. Sai da lista quando alguém responde ou lê a conversa. |

Filtrando por **Agente ou fila**, as conversas **Sem atendimento** somem da lista, porque ainda não têm responsável.

## Aba Atendimentos

Mostra os números do período e a lista de todos os atendimentos, abertos e finalizados.

### Os indicadores e o gráfico

<!-- PRINT 8: os cartões de indicadores e o gráfico "Atendimentos por dia", com o mouse sobre um dia. -->

| Indicador | O que mostra |
| --- | --- |
| **Atendimentos** | Total do período e a média por dia. |
| **1ª resposta em até 2 min** | Porcentagem dos atendimentos respondidos em até 2 minutos, com o tempo médio. |
| **Encerrados em até 1 hora** | Dos atendimentos encerrados, quantos duraram até 1 hora, com a duração média. |
| **Finalizadas** | Porcentagem de atendimentos já fechados e quantos continuam abertos. |
| **Transferidos** | Quantos atendimentos foram transferidos e a porcentagem do total. |

A **1ª resposta** conta da primeira mensagem do cliente até a primeira resposta do agente. Quando foi a empresa que puxou a conversa, conta desde a abertura do atendimento.

O gráfico **Atendimentos por dia** mostra o volume de cada dia e o pico do período. Passe o mouse sobre um ponto para ver o dia e a quantidade.

### A lista de atendimentos

<!-- PRINT 9: a tabela da aba Atendimentos, com atendimentos abertos e finalizados. -->

| Coluna | O que mostra |
| --- | --- |
| **Data** | Quando o atendimento abriu. |
| **Conexão** | Nome e número da conexão. |
| **Contato** e **Empresa** | O cliente e a conta dele. |
| **Registro** | Se o cliente é um **Contato** ou um **Lead**. |
| **Agente** e **Papel** | Quem está ou esteve com o atendimento e o papel dele no Salesforce. |
| **1ª resp.** | Tempo da primeira resposta: verde até 2 minutos, amarelo até 10, vermelho acima disso. |
| **Duração** | Da abertura ao fechamento. Vazio enquanto está aberto. |
| **Status** | **Aberta** ou **Finalizada**. |
| **Ações** | O olho abre o atendimento no painel lateral. |

A lista mostra 100 atendimentos por vez; use **Carregar mais 100** para ver os seguintes.

Em períodos muito grandes (mais de 40 mil atendimentos), os indicadores consideram só os mais recentes e o painel avisa. Diminua o período para ver tudo.

## Aba Equipe

Mostra o desempenho de cada agente no período, agrupado pelo **papel** do usuário no Salesforce.

<!-- PRINT 10: aba Equipe com um papel aberto mostrando os agentes, as bolinhas de presença e o grupo Filas. -->

Cada linha de papel mostra quantos agentes tem e quantos atendimentos o grupo fez. Clique no papel para mostrar ou esconder os agentes. Usuários sem papel ficam em **Sem papel**, e os atendimentos que estão com filas ficam no grupo **Filas**. Os agentes do Nitzap aparecem mesmo sem atendimentos no período.

| Coluna | O que mostra |
| --- | --- |
| **Papel / agente** | O nome do agente, com uma bolinha de presença: verde se usou o Salesforce nos últimos 5 minutos, amarela até 30 minutos, cinza depois disso. |
| **Abertas agora** | Atendimentos abertos com o agente neste momento. |
| **Atendimentos** | Quantos atendimentos o agente teve no período. |
| **Carga** | Barra com a parte do total que ficou com ele. |
| **1ª resp. (média)** | Tempo médio da primeira resposta. |
| **Encerra em até 1h** | Dos atendimentos que ele encerrou, quantos duraram até 1 hora. |
| **Finalizadas** | Porcentagem dos atendimentos dele que já foram fechados. |

## Acompanhar uma conversa

Clique no olho de qualquer lista para abrir o painel lateral. Para fechar, clique fora dele, no **×** ou aperte **Esc**.

### Atendimento aberto ou finalizado

<!-- PRINT 11: painel lateral de um atendimento aberto: o aviso "Modo acompanhamento", a conversa com a etiqueta "ao vivo", a linha do tempo e os dados do registro. -->

O painel abre em **Modo acompanhamento**: você lê a conversa como gestor e nada do que fizer aqui chega ao cliente.

| Parte | O que mostra |
| --- | --- |
| **Conversa** | As mensagens do atendimento. Com a etiqueta **ao vivo**, as novas mensagens aparecem na hora. |
| **Linha do tempo do atendimento** | Abertura, primeira mensagem do contato, primeira mensagem do agente, transferência e encerramento, com data e hora. Em um atendimento finalizado sem resposta, aparece **Contato nunca respondeu** ou **Agente ainda não respondeu**. |
| **Dados do registro** | Tipo de registro, conexão, situação e há quanto tempo, mensagens não lidas pelo agente, 1ª resposta, duração, WhatsAppId e Id da Tarefa. |
| **Abrir tarefa no CRM** | Abre a [Tarefa do atendimento](#nitzap/atendimento/a-tarefa-do-atendimento). |

Com o atendimento aberto, o **administrador** vê também:

<!-- PRINT 12: parte de baixo do painel lateral: Transferir atendimento, Encerrar atendimento e Sussurrar para o agente. -->

| Ação | Como funciona |
| --- | --- |
| **Transferir atendimento** | Escolha o **Tipo** (**Usuário** ou **Fila**) e o **Novo responsável**, escreva o motivo se quiser e clique em **Transferir atendimento**. O novo responsável assume com o próprio nome; numa fila, o atendimento volta a esperar alguém puxar. O motivo entra na conversa como sussurro para o agente. |
| **Encerrar atendimento** | Clique e depois em **Confirmar encerramento**. O atendimento sai da lista de abertos e, se a conexão tiver bot, ele volta a atender o cliente. |
| **Sussurrar para (agente)** | Escreva uma orientação e clique em **Enviar sussurro**. O agente vê a mensagem na conversa, no Omni, assinada como **(seu nome) sussurrou como gestor**. O cliente não recebe. |

O painel não envia mensagens ao cliente nem responde em nome do agente, de propósito: quem fala com o cliente é sempre o agente.

<!-- PRINT 13: o sussurro do gestor como aparece para o agente dentro da conversa no Omni. -->

Veja também o [Modo sussurro](#nitzap/omni/modo-sussurro) no guia do Omni.

### Conversa sem atendimento

<!-- PRINT 14: painel lateral de uma conversa sem atendimento: o aviso, a conversa, os dados e o bloco "Abrir atendimento". -->

Para conversas que vieram de **Sem atendimento** ou da aba **Chats**, o painel mostra a conversa, os **Dados da conversa** (registro, conexão, não lidas, há quanto tempo chegou a última mensagem e o WhatsApp) e o bloco **Abrir atendimento**.

O **administrador** escolhe o **Tipo** (**Usuário** ou **Fila**) e o **Responsável** e clica em **Abrir atendimento**. O atendimento nasce com esse responsável, como se tivesse sido aberto pelo Omni; numa fila, fica esperando alguém puxar.

Quando não dá para abrir, o painel explica o motivo:

| Motivo | O que fazer |
| --- | --- |
| A conversa é de grupo. | Grupos não têm atendimento; dá só para acompanhar. |
| O usuário não é administrador. | Abra o atendimento pelo Omni, pelo botão direito na conversa. |
| O número está só em uma **Conta**. | Cadastre o WhatsApp também em um Contato ou Lead. |
| O número não está em nenhum Contato ou Lead. | Cadastre o contato no Salesforce com esse WhatsApp. |

Se a conversa já tem atendimento aberto, o olho abre direto o modo acompanhamento.

## Problemas comuns

| Situação | O que fazer |
| --- | --- |
| A aba **Painel do Gestor** não aparece. | Procure no **Iniciador de aplicativos**. Se não encontrar, confira se o usuário tem o conjunto de permissões do Nitzap. |
| Não aparecem os botões de transferir, encerrar e sussurrar. | Essas ações são só para administradores, e só aparecem em atendimentos abertos. |
| Faltam conversas ou conexões. | Quem não é administrador vê só as conexões em que é membro e, com **Respeitar Hierarquia**, só a própria equipe. |
| A conversa não abre pelo olho na aba Chats. | O número não está cadastrado no Salesforce e não tem atendimento aberto. Cadastre o contato. |
| Aparece **Base do CRM** em vez de **Ao vivo**. | É o normal nas abas Atendimentos e Equipe. Nas abas Chats e Ao vivo, clique em **Atualizar**. |
| Aviso de que parte das conversas não pôde ser lida. | O painel não conseguiu ler a última mensagem de algumas conversas; para elas, a espera conta desde a abertura do atendimento. Atualize em alguns instantes. |
| Aviso de que os indicadores consideram só os mais recentes. | O período tem atendimentos demais. Diminua o período. |
