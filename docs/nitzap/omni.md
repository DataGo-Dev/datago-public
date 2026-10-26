# 02. Nitzap Omni: conversas dentro do Salesforce

O Nitzap Omni é onde você conversa com os clientes pelo WhatsApp sem sair do Salesforce. Ele mostra as conversas de todas as conexões das quais você é membro, indica por qual número cada cliente falou com você e liga cada conversa ao Lead, Contato ou Conta correspondente. Este guia mostra as formas de abrir o Omni, como filtrar e ler a lista de conversas, as opções dentro de uma conversa, os recursos de IA e as suas preferências.

**Como ler as imagens:** os círculos vermelhos numerados apontam para a parte da tela que está sendo explicada. O número no círculo é o mesmo da coluna **Nº** da tabela ou da lista logo abaixo da imagem.

## Formas de visualizar as conversas

O Omni pode ser usado de três jeitos. As conversas são as mesmas nos três; muda o espaço na tela e o que acontece quando você clica em um cliente.

| Forma | Onde fica | Quando clicar em um cliente |
| --- | --- | --- |
| **Compacto** | Item **Nitzap** na barra de utilitários, no canto inferior esquerdo de qualquer página do Salesforce. | Se o número está salvo como Lead, Contato ou Conta, abre direto o registro no Salesforce. Se não está salvo, abre a conversa em uma janela. |
| **Ampliado** | O mesmo painel da barra de utilitários, aumentado pelo botão de ampliar. | A conversa abre em abas ao lado da lista, dentro do painel. Você continua navegando no Salesforce com o painel aberto. |
| **Nitzap Web** | Aba **Nitzap Web**, em tela cheia, no estilo do WhatsApp Web. | A conversa abre em abas ao lado da lista. A tela fica fixa, e o botão **i** mostra as informações do cliente sem sair da conversa. |

### Compacto

Clique em **Nitzap**, no canto inferior esquerdo (onde a seta aponta), para abrir o painel.

![Omni compacto na barra de utilitários](images/omni-compacto.png)

### Ampliado

No painel compacto, clique no botão de ampliar, no topo da lista. Para voltar ao tamanho compacto, clique no mesmo botão, que passa a se chamar **Reduzir painel**. O Nitzap lembra no navegador qual tamanho você usou por último.

![Omni ampliado, com a conversa ao lado da lista](images/omni-ampliado.png)

| Nº | O que é |
| :---: | --- |
| 1 | Botão **Ampliar painel / Reduzir painel**. |
| 2 | A conversa aberta, em uma aba ao lado da lista. O resto do Salesforce continua acessível atrás do painel. |

### Nitzap Web

Clique no botão **Abrir Nitzap Web** (nº 3 em [Botões do topo](#nitzap/omni/botoes-do-topo)) ou abra a aba **Nitzap Web** pelo menu de aplicativos do Salesforce.

![Nitzap Web em tela cheia](images/omni-web.png)

| Nº | O que é |
| :---: | --- |
| 1 | **Abas das conversas abertas.** Clique na aba para trocar de conversa e no **×** para fechá-la. Ficam abertas no máximo 10 abas: ao abrir a 11ª, a que está há mais tempo sem uso fecha sozinha. |
| 2 | Botão **i**: abre os detalhes do cliente (veja abaixo). |

#### Detalhes do cliente (botão i)

O botão **i** aparece quando a conversa está ligada a um Lead, Contato ou Conta. Ele abre o painel **Detalhes** ao lado da conversa, com os dados do registro.

![Painel Detalhes com os dados do contato ao lado da conversa](images/omni-web-detalhes.png)

| Nº | O que é |
| :---: | --- |
| 1 | Botão **i**, que abre e fecha o painel. |
| 2 | **Lápis:** edita o campo ali mesmo, sem sair da conversa. |
| 3 | Abre o registro completo em uma nova aba. |
| 4 | Fecha o painel. |

No fim do painel aparecem até 10 Casos, Oportunidades e Tarefas ligados ao registro. Clique em um item para ver os detalhes e em **Voltar ao registro** para retornar.

## A lista de conversas

### Botões do topo

![Botões do topo da lista de conversas](images/omni-topo-lista.png)

| Nº | Botão | O que faz |
| :---: | --- | --- |
| 1 | **Conexões** | Filtra a lista por conexão. Veja [Filtrar por conexão](#nitzap/omni/filtrar-por-conexao). |
| 2 | **Ampliar painel / Reduzir painel** | Alterna entre o compacto e o ampliado. Só aparece na barra de utilitários. |
| 3 | **Abrir Nitzap Web** | Abre a aba Nitzap Web. Não aparece quando você já está nela. |
| 4 | **Ajuda e Recursos** | Links para as notas de lançamento, a documentação, a configuração de bot e o canal do Nitzap no YouTube. |
| 5 | **Preferências** | Abre as suas preferências. Veja [Preferências](#nitzap/omni/preferencias). |
| 6 | **Chamadas Recebidas** | Lista as ligações de WhatsApp recebidas e feitas. Em vermelho, as recusadas ou perdidas; em verde, as atendidas. Clique em uma para abrir a conversa. Não aparece se todas as suas conexões forem oficiais (Coex ou Cloud). |
| 7 | **Meus Contatos** | Abre a lista de contatos para começar uma conversa nova. A aba **Internos** traz os colegas, para o chat interno. |
| 8 | **Pesquisar** | Encontra conversas pelo nome, pelo número ou pelo nome da empresa. |
| 9 | **Arquivadas** | Mostra quantas conversas estão arquivadas. Clique para ver a lista e em **<** para voltar. |
| 10 | **Todas** | Mostra todas as conversas que não estão arquivadas. |
| 11 | **Não Lidas** | Mostra só as conversas com mensagens não lidas. O número ao lado é a quantidade dessas conversas. |

### Filtrar por conexão

Quando você participa de mais de uma conexão, o botão **Conexões** aparece no topo. Passe o mouse ou clique nele e escolha o que quer ver.

![Filtro de conexões](images/omni-filtro-conexoes.png)

| Nº | Opção | O que mostra |
| :---: | --- | --- |
| 1 | **Todas as conexões** | Conversas de todos os números. |
| 2 | **Interno** | Conversas com a equipe (chat interno entre colegas). |
| 3 | **Uma conexão específica** | Só as conversas daquele número. Embaixo do nome aparecem o número e o tipo de conexão: **Nitzap** para conexões via QR Code, **Coex (Meta)** ou **Cloud API (Meta)** para as oficiais. |
| 4 | **Bolinha colorida** | Não indica se a conexão está online: é só a cor que identifica a conexão. A mesma cor aparece na etiqueta da conexão em cada conversa da lista (nº 6 em [O que cada conversa mostra](#nitzap/omni/o-que-cada-conversa-mostra)). |

Só dá para escolher uma opção por vez. A escolhida fica marcada com ✓ e o botão passa a mostrar o nome dela. O Nitzap lembra a sua escolha na próxima vez.

### O que cada conversa mostra

![Elementos de cada conversa na lista](images/omni-conversas-lista.png)

| Nº | Elemento | O que significa |
| :---: | --- | --- |
| 1 | **👤 Nome · 🏢 Empresa** | O proprietário do registro no Salesforce e a empresa (do Lead, ou da Conta do Contato). Só aparece quando o número está salvo. Dá para esconder nas [Preferências](#nitzap/omni/preferencias). |
| 2 | **Cartão roxo** antes do nome | O número está salvo como **Contato**. |
| 3 | **Pessoa laranja** antes do nome | O número está salvo como **Lead**. Um **prédio azul** indica **Conta**. Sem ícone, o número não está salvo no Salesforce. |
| 4 | **Seta verde para baixo** | A última mensagem foi **recebida** do cliente. |
| 5 | **Seta cinza para cima** | A última mensagem foi **enviada** por você e ainda não foi lida. Depois de lida, vira um ✓ azul. |
| 6 | **Etiqueta colorida** (ex.: **Niter**, **Interno**) | A **conexão por onde o cliente falou**, ou seja, para qual número ele mandou a mensagem. **Interno** indica uma conversa com um colega. Só aparece quando você participa de mais de uma conexão. |
| 7 | **Número verde** | Quantidade de mensagens não lidas na conversa. |
| 8 | **✓ azul ao lado do nome** | Canal oficial de anúncios do Nitzap. |

### Botão direito na conversa

Clique com o botão direito em uma conversa da lista para ver as ações rápidas. O menu abre logo abaixo da conversa.

![Menu do botão direito em uma conversa](images/omni-menu-direito.png)

| Nº | Ação | O que faz |
| :---: | --- | --- |
| 1 | **Marcar como lido** / **Marcar como não lido** | Zera o contador de não lidas da conversa ou volta a marcá-la como não lida, para lembrar de responder depois. O texto muda conforme a conversa já está lida ou não. |
| 2 | **Fixar** / **Desfixar** | Prende a conversa no topo da lista, com um alfinete. |
| 3 | **Etiquetas** | Abre a lista de etiquetas da conexão da conversa para você aplicar à conversa. As etiquetas aparecem coloridas na lista, acima da última mensagem. Se a conexão não tiver etiquetas, aparece **Nenhuma etiqueta disponível nesta conexão**. Veja [Etiquetas](#nitzap/omni/etiquetas). |
| 4 | **Arquivar** / **Desarquivar** | Tira a conversa da lista principal e a guarda nas **Arquivadas** (nº 9 em [Botões do topo](#nitzap/omni/botoes-do-topo)). Para trazer de volta, abra as arquivadas e use **Desarquivar**. |
| 5 | **Criar atendimento** | Abre um atendimento para o cliente. Veja [Atendimento](#nitzap/omni/atendimento). |

As ações de atendimento mudam conforme a situação da conversa:

- **Criar atendimento** aparece quando o número está salvo no Salesforce, não há atendimento aberto e a conversa não é de grupo.
- **Puxar atendimento** aparece quando a conversa está na fila de uma equipe.
- **Fechar Atendimento** aparece quando a conversa está em atendimento.

## Dentro da conversa

### Cabeçalho

![Cabeçalho e menu de opções da conversa](images/omni-menu-conversa.png)

| Nº | O que é |
| :---: | --- |
| 1 | **Foto e nome do cliente.** Mostram também quando ele está digitando ou online. |
| 2 | **Foto do usuário com seta:** escolhe **de qual usuário e de qual conexão** é a conversa que você está vendo. Quando mais de uma pessoa já falou com o cliente, cada uma aparece aqui com os números que usou. Não é transferência de atendimento. |
| 3 | **Menu ⋮:** mais opções da conversa (tabela abaixo). |

| Opção do menu ⋮ | O que faz |
| --- | --- |
| **Excluir conversa** | Apaga as mensagens com esse cliente na conexão selecionada, depois de uma confirmação. Só aparece se o administrador liberou a exclusão. |
| **Copiar Número** | Copia o número do cliente, só com os dígitos. |
| **Copiar ChatID** | Copia o identificador da conversa. |
| **Mídias** | Abre a galeria com as fotos, vídeos e arquivos trocados na conversa. |
| **Buscar** | Procura um texto nas mensagens da conversa. |
| **Novo Lead / Novo Contato / Nova Conta** | Abre o cadastro do Salesforce já preenchido com o nome e o número do WhatsApp. Não aparece quando o cliente pertence a outro usuário e o seu acesso é limitado. Nesse caso, o cabeçalho mostra quem é o proprietário. |

### Opções da mensagem

Passe o mouse sobre uma mensagem e clique na seta que aparece no canto do balão.

![Opções da mensagem recebida e da mensagem enviada](images/omni-opcoes-mensagem.png)

- **1:** seta de uma mensagem **recebida** e o menu que ela abre.
- **2:** seta de uma mensagem **enviada** e o menu que ela abre.

| Opção | Recebida (1) | Enviada (2) | O que faz |
| --- | :---: | :---: | --- |
| **Lida (data e hora)** | | ✓ | Não é um botão: mostra quando o cliente leu a mensagem. |
| **✨ IA: Resumir** | ✓ | ✓ | Resume a mensagem (texto, áudio, imagem ou documento). Veja [Recursos de IA](#nitzap/omni/recursos-de-ia). |
| **Responder** | ✓ | ✓ | Responde citando a mensagem. |
| **Encaminhar** | ✓ | ✓ | Seleciona a mensagem para encaminhar. Você pode marcar outras e depois escolher o contato. |
| **Reagir** | ✓ | | Envia uma reação com emoji. |
| **Copiar** | ✓ | ✓ | Seleciona a mensagem para copiar. Você pode marcar outras e copiar todas de uma vez, em ordem. |
| **Copiar ID** | ✓ | ✓ | Copia o identificador da mensagem, útil para o suporte. |
| **Editar** | | ✓ | Altera o texto da mensagem enviada. Até **10 minutos** depois do envio. |
| **Apagar** | | ✓ | Apaga a mensagem para todos, depois de uma confirmação. Até **2 dias** depois do envio. |

**Editar** e **Apagar** não existem nas conexões oficiais (Coex e Cloud API), só nas conexões via QR Code. Em imagens também aparece a opção de **download**.

### Caixa de mensagem

Escreva a mensagem e tecle **Enter** para enviar. Para pular uma linha sem enviar, use **Shift + Enter**. Em grupos, digite **@** para mencionar um participante.

![Botões da caixa de mensagem](images/omni-caixa-mensagem.png)

| Nº | Botão | O que faz |
| :---: | --- | --- |
| 1 | **Arquivos** (+) | Envia um arquivo do computador ou do Salesforce. Veja [Arquivos](#nitzap/omni/enviar-arquivos). |
| 2 | **Emoji** | Insere um emoji no texto. |
| 3 | **Enviar contato** | Envia um cartão de contato. Veja [Enviar contato](#nitzap/omni/enviar-contato). |
| 4 | **Modo sussurro** | Escreve uma nota interna na conversa: só a equipe vê, o cliente não recebe. |
| 5 | **Registrar histórico** | Cria uma Tarefa no Salesforce com um trecho da conversa. Veja [Registrar histórico](#nitzap/omni/registrar-historico). |
| 6 | **Templates** | Veja [Templates](#nitzap/omni/templates). |
| 7 | **Agendar envio** | Veja [Agendar envio](#nitzap/omni/agendar-envio). |
| 8 | **Microfone** | Grava um áudio. Antes de enviar, dá para ouvir e descartar. |
| 9 | **Enviar** | Envia a mensagem (o mesmo que **Enter**). |
| 10 | **Gerar com IA** | Escreve uma sugestão de resposta. Veja [Recursos de IA](#nitzap/omni/recursos-de-ia). |
| 11 | **Correção ortográfica** | Corrige o texto que você está escrevendo. Veja [Recursos de IA](#nitzap/omni/recursos-de-ia). |
| 12 | **Resumir conversa** | Resume a conversa em um período. Veja [Recursos de IA](#nitzap/omni/recursos-de-ia). |

### Enviar arquivos

Clique no **+** (indicado pela seta embaixo). O botão vira um **×**, que fecha o menu.

![Envio de arquivos](images/omni-anexo.png)

| Nº | Opção | O que faz |
| :---: | --- | --- |
| 1 | **Do Salesforce** | Envia um arquivo que já está salvo no Salesforce. |
| 2 | **Selecionar** ou arrastar | Envia um arquivo do computador. Também dá para arrastar o arquivo para dentro da área tracejada. |

O limite é de 100 MB por arquivo; vídeos aceitam até 40 MB, pelo limite do WhatsApp.

### Emoji

Clique no ícone de carinha (indicado pela seta) e escolha o emoji. Use **Procurar** para buscar pelo nome.

![Seletor de emoji](images/omni-emoji.png)

### Enviar contato

Clique no ícone de cartão (indicado pela seta embaixo).

![Enviar contato: conexão e busca do contato](images/omni-enviar-contato.png)

| Nº | O que fazer |
| :---: | --- |
| 1 | Escolha por qual conexão o contato vai ser enviado. Já vem selecionada a conexão da conversa. |
| 2 | Busque o contato pelo nome ou número. |
| 3 | Clique no contato para enviar o cartão. |

O botão não aparece nas conexões oficiais (Coex e Cloud API) nem no chat interno.

### Registrar histórico

Use para guardar no Salesforce um trecho importante da conversa, como uma negociação ou um atendimento por telefone. O botão só aparece quando o número está salvo como Lead, Contato ou Conta.

![Registrar Histórico do WhatsApp](images/omni-registrar-historico.png)

1. Clique no ícone de telefone (nº 5 da caixa de mensagem).
2. Confira o **Assunto** (o padrão é *Conversa Whatsapp*).
3. Informe o **Início do histórico** e o **Fim do histórico**. O fim precisa ser depois do início.
4. Se quiser, escreva **Comentários**.
5. Clique em **Registrar**.

Os números da imagem são os mesmos dos passos. O Nitzap cria uma Tarefa concluída, do tipo **HISTORY**, ligada ao cliente, e abre a Tarefa em seguida.

## Recursos de IA

Os recursos de IA só aparecem quando o administrador configurou a IA no Nitzap.

| Recurso | Onde fica | O que faz |
| --- | --- | --- |
| **Gerar com IA** | Botão nº 10 da caixa de mensagem | Escreve uma sugestão de resposta. |
| **Correção ortográfica** | Botão nº 11 da caixa de mensagem | Corrige o texto que você está escrevendo. |
| **Resumir conversa** | Botão nº 12 da caixa de mensagem | Resume a conversa em um período. |
| **IA: Resumir** | [Opções da mensagem](#nitzap/omni/opcoes-da-mensagem) | Resume uma mensagem só. |
| **Transcrição de áudio** | Embaixo de cada áudio | Transforma o áudio em texto. |

### Gerar com IA

Clique na varinha. A IA lê as últimas 10 mensagens da conversa, inclusive imagens e áudios, e escreve uma sugestão de resposta na caixa de mensagem.

![Botão Gerar com IA](images/ia-gerar.png)

A mensagem **não é enviada sozinha**: leia, ajuste se precisar e envie.

### Correção ortográfica

Escreva a mensagem e clique no ✓. A IA corrige a ortografia do texto que está na caixa. Com a caixa vazia, o botão não faz nada.

![Botão Correção ortográfica](images/ia-correcao.png)

### Resumir conversa

Clique no raio para abrir a janela **Resumir Conversa**.

![Janela Resumir Conversa](images/ia-resumir-janela.png)

| Nº | O que fazer |
| :---: | --- |
| 1 | **Início:** data e hora a partir das quais a conversa entra no resumo. O padrão é hoje, à meia-noite. |
| 2 | **Fim:** data e hora finais. O padrão é agora. |
| 3 | O resumo gerado: principais assuntos, decisões, pendências e tom da conversa. |
| 4 | **Copiar:** copia o resumo. |
| 5 | **Enviar:** manda o resumo para o cliente, como mensagem. |
| 6 | **Sussurrar:** salva o resumo na conversa como nota interna. Só a equipe vê. |

Um resumo sussurrado fica na conversa com fundo amarelo, para quem assumir o atendimento depois:

![Resumo salvo como nota interna (sussurro)](images/ia-resumo-sussurro.png)

- **1:** botão **Resumir conversa**.
- **2:** o resumo salvo como sussurro. O cliente não recebe.

### Transcrição de áudio

A IA transforma os áudios em texto, que aparece entre aspas embaixo do áudio (indicado pela seta).

![Transcrição de um áudio](images/ia-transcricao.png)

Há dois jeitos de usar:

- **Automático:** ligue a preferência **IA: Transcrever e exibir automaticamente áudios** (nº 11 em [Preferências](#nitzap/omni/preferencias)). Todo áudio é transcrito sozinho. Se o administrador deixou a transcrição obrigatória, ela já vem ligada.
- **Um áudio por vez:** com a preferência desligada, clique em **Transcrever**, embaixo do áudio que você quer ler.

A transcrição fica salva na mensagem: quem abrir a conversa depois vê o texto sem transcrever de novo.

## Preferências

Clique no botão **Preferências** (nº 5 em [Botões do topo](#nitzap/omni/botoes-do-topo)). As preferências são suas: valem em qualquer computador e não mudam nada para os outros usuários.

![Preferências do Omni](images/omni-preferencias.png)

| Nº | Preferência | O que faz |
| :---: | --- | --- |
| 1 | **🎨 Cor do meu balão** | Muda a cor dos balões das mensagens que você envia. Nas conversas que já estavam abertas, clique em **Atualizar agora** para aplicar. |
| 2 | **Silenciar todos os grupos** | Desliga o som, a notificação e o alerta de mensagens novas em grupos. O contador de não lidas continua funcionando. |
| 3 | **Silenciar todos os chats individuais** | O mesmo, para as conversas individuais. |
| 4 | **Assinar mensagens com meu nome** | Coloca o seu primeiro nome em negrito no início de cada mensagem enviada (ex.: **#Thiago:**). |
| 5 | **Exibir proprietário** | Mostra o 👤 proprietário do registro acima do nome de cada conversa. |
| 6 | **Exibir nome da empresa** | Mostra a 🏢 empresa acima do nome de cada conversa. |
| 7 | **Marcar como lida apenas ao responder** | Ligada: abrir a conversa não zera as não lidas, só responder. Desligada: abrir a conversa já marca como lida. |
| 8 | **Abrir conversas em uma nova guia do navegador** | No modo compacto, quando o clique na conversa abre o registro do cliente, ele abre em uma nova guia do navegador. |
| 9 | **Habilitar filtros de atendimento** | Troca o botão **Não Lidas** pelos filtros de atendimento. Veja [Filtros de atendimento](#nitzap/omni/filtros-de-atendimento). |
| 10 | **Receber notificações apenas de quem eu estiver atendendo** | Só avisa sobre conversas cujo atendimento aberto é seu. |
| 11 | **IA: Transcrever e exibir automaticamente áudios** | Transcreve os áudios sozinho. Veja [Transcrição de áudio](#nitzap/omni/transcricao-de-audio). Se o administrador deixou obrigatório, aparece **Ativado pelo administrador** e não dá para desligar. |

Ao mudar **Assinar mensagens com meu nome**, **IA: Transcrever** ou **Habilitar filtros de atendimento**, o Nitzap pede confirmação e recarrega a página.

Veja a diferença na lista com **Exibir proprietário** e **Exibir nome da empresa** ligados e desligados:

![Lista de conversas com e sem proprietário e empresa](images/omni-proprietario-comparacao.png)
