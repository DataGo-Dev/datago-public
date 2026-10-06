# Configuração do Einstein Bot/AgentForce no Nitzap

Configuração inicial. 
Obs: A configuração abaixo é apenas um Start do requerido para rodar o Bot. Pode ser que ao configurar como abaixo será necessário ainda 
habilitar e desabilitar funções que dependem de cada fluxo de segurança de cada Organização. Para obter consultoria personalizada consulte a Datago.

Para iniciar a configuração deve-se criar um aplicativo conectado externo no Salesforce para realizar a comunicação do Nitzap com o Salesforce
Para isso 
1. clique em Configurações
2. Na busca rápida pesquise por "Gerenciador de aplicativo de cliente externo".
3. Clique em "Novo aplicativo cliente externo"

Na criação Habilite OAuth e selecione os escopos da imagem abaixo
<img width="1253" height="607" alt="image" src="https://github.com/user-attachments/assets/73ed3b5b-3709-4142-bbef-062a4aa80871" />


ou contato a Datago para consultoria personalizada.

Entre os escopos, o **"Gerenciar dados do usuário via APIs (api)"** é obrigatório: além de falar com o agente, o Nitzap usa esse aplicativo para chamar a API do próprio pacote no Salesforce, por exemplo para concluir a tarefa de atendimento quando a mensagem por falta de resposta encerra a conversa. Sem esse escopo, o bot funciona, mas o atendimento fica aberto no Salesforce depois do aviso.

Você deve habilitar o fluxo de credencias do cliente

<img width="420" height="213" alt="image" src="https://github.com/user-attachments/assets/56824720-9165-4803-8bb4-a376175ee988" />

Na parte de Segurança habilite: "Emitir tokens de acesso com base em Token da Web do JSON (JWT) para usuários nomeados".
<img width="671" height="303" alt="image" src="https://github.com/user-attachments/assets/cbbe53aa-7082-4f24-ae19-9bff956696c6" />

Clique em criar.

Adicionalmente relaxe os IPS como abaixo (Apenas se sua organização permitir, caso contrário você pode liberar os IPS):
<img width="1249" height="343" alt="image" src="https://github.com/user-attachments/assets/06f0c519-38a0-46a7-a2f9-e7aa6dd1fb1d" />
Ou libere IPS do Nitzap
178.156.203.218
178.156.194.8
178.156.205.98
178.156.196.62
178.156.193.203
178.156.140.66

Também deve adicionar o usuário que irá executar em Politicas OAuth
<img width="673" height="506" alt="Screenshot 2026-08-27 at 09 30 55" src="https://github.com/user-attachments/assets/8257e3ff-d507-4a9f-9031-1b58cd79a642" />

Esse usuário de execução precisa do conjunto de permissões **Nitzap 2.0** (`Nitzap_20`): é com ele que o Nitzap lê e conclui as tarefas de atendimento pela API do pacote.

Se você ainda não configurou um usuário integração na sua organização consulte:

https://help.salesforce.com/s/articleView?id=platform.integration_user.htm&type=5

Ao criar vá em configurações e em Configurações do OAuth > Chave e segredo do consumidor
<img width="653" height="707" alt="image" src="https://github.com/user-attachments/assets/3efd0146-974d-410a-8841-3287ede71355" />

Copia as chaves e vá em Nitzap COnfig > Configurações
<img width="678" height="159" alt="image" src="https://github.com/user-attachments/assets/e7b5b112-9652-4eb1-a31e-973f3bbb01d0" />

Coloque em Credenciais Salesforce e clique em Salvar Configurações
<img width="567" height="519" alt="image" src="https://github.com/user-attachments/assets/a83f93fc-a7f3-48f7-b6ed-888ede2362d5" />

Confira se em:
"Configurações do OAuth e do OpenID Connect" 
esteja habilitado:
Permitir código de autorização e fluxo de credenciais

# Configurando o Agente/Bot

Em **Nitzap Config › Conexões › Conexões**, escolha a conexão que vai usar o agente. Cada número é uma conexão, e o agente é configurado por conexão: números diferentes podem ter agentes diferentes, ou nenhum.

![Lista de conexões do Nitzap](images/agentforce-conexoes.png)

Funciona nos dois tipos de conexão: **API oficial da Meta** e **QR Code**. Na conexão por QR Code, o agente mostra "digitando..." por alguns segundos antes de cada resposta, não responde em grupos e ignora mensagens recebidas há mais de 5 minutos. Isso evita que, quando o número volta depois de um tempo desconectado, o agente dispare respostas para tudo o que chegou nesse intervalo.

Clique na engrenagem da conexão e vá na aba **Configurações**. O bloco **Bot e agente** tem tudo o que importa:

![Configurações da conexão, bloco Bot e agente](images/agentforce-configuracoes-conexao.png)

| Campo | O que fazer |
|---|---|
| **Resposta automática (bot/agente)** | Escolha `Agentforce (agente)` ou `Einstein Bot`. Só um por conexão |
| **Agentforce: agente desta conexão** | Busque e selecione o agente do Salesforce. **Obrigatório**: com a resposta automática ligada e sem agente escolhido, aparece o aviso amarelo e nada é respondido |
| **Ociosidade da sessão do bot (min)** | Tempo sem mensagem do cliente após o qual o agente esquece a conversa e começa uma sessão nova na próxima mensagem. Se houver mensagem por falta de resposta, ela é enviada neste momento. Vazio usa 30 minutos |
| **Pausa após atendimento humano (min)** | Quando o agente transfere o atendimento ou alguém da equipe manda mensagem pelo Nitzap, o agente para de triar e só volta depois desses minutos sem mensagem da equipe. Vale também quando é a equipe que inicia a conversa: o vendedor manda a saudação, o cliente responde e quem recebe é o vendedor, não o agente. Disparos em massa não pausam o agente, para que ele possa triar as respostas. Se houver mensagem por falta de resposta, ela é enviada quando este tempo vence sem o cliente responder ao vendedor. Vazio usa 8 horas. **É este campo que controla quanto tempo o cliente pode esperar na fila sem o agente reassumir a conversa** |
| **Mensagem por falta de resposta** | Texto enviado quando o contato para de responder. Na conversa com o agente, sai ao fim da ociosidade da sessão. Depois que um vendedor responde, sai ao fim da pausa após atendimento humano, contada da última mensagem do vendedor. Enquanto o cliente espera na fila, sem resposta de um vendedor, nada é contado. Com qualquer um desses tempos em 24 horas ou mais, a mensagem não é enviada naquele caso. Vazio desliga |

Pronto. A partir daí, mensagem recebida nesse número é respondida pelo agente.

# Como as opções do bot aparecem no WhatsApp

Quando o Einstein Bot oferece opções para o cliente escolher, o Nitzap as entrega do jeito que o WhatsApp permite em cada canal:

| Situação | O que o cliente vê |
|---|---|
| API oficial, até 3 opções | Botões de resposta abaixo da pergunta |
| API oficial, de 4 a 10 opções | Uma lista: o cliente toca em "Ver opções" e escolhe |
| API oficial, mais de 10 opções | Lista numerada em texto, e o cliente responde com o número ou o texto |
| Conexão por QR Code | Lista numerada em texto, porque botões não são confiáveis fora da API oficial |

Limites do WhatsApp: título de botão com até 20 caracteres e item de lista com até 24. Rótulos mais longos são encurtados no título e aparecem por inteiro na descrição do item da lista. Vale a pena escrever os rótulos das opções do bot já curtos.

Tocar em um botão ou item vale como a resposta do cliente: o bot recebe a opção escolhida, não um texto solto, mesmo que o rótulo tenha sido encurtado. No chat do Nitzap a mensagem aparece como a pergunta seguida da lista numerada, e a resposta do cliente aparece com o texto da opção. Se o WhatsApp recusar a mensagem interativa por algum motivo, o Nitzap envia a versão em texto.

Agentforce responde em texto livre e não oferece opções, então nada disso se aplica a ele.

# O que o Nitzap envia para o bot

O Nitzap manda os dados do contato no começo da conversa, uma única vez por sessão. O que muda é a forma, conforme o tipo escolhido.

## Einstein Bot: variáveis

Ao abrir a sessão, o Nitzap envia estas variáveis. Crie cada uma no seu bot, do tipo texto e com exatamente o mesmo nome:

| Variável | Conteúdo |
|---|---|
| `nitzap_contact_phone` | Telefone do contato no WhatsApp |
| `nitzap_contact_name` | Nome que o contato usa no WhatsApp |
| `nitzap_connection_number` | Número da conexão que recebeu a mensagem |

Variável sem valor não é enviada. Por exemplo, um contato sem nome no WhatsApp chega só com telefone e número da conexão.

## Agentforce: mensagem de contexto

O Agentforce não recebe variáveis. Em vez disso, logo depois de abrir a sessão e antes da primeira mensagem do cliente, o Nitzap envia uma mensagem de contexto com os mesmos três dados: nome do contato, telefone no WhatsApp e número da conexão. Ela começa avisando que é contexto do sistema e que não deve ser respondida, e a resposta do agente a ela é descartada, então o cliente nunca a vê.

Uma sessão nova começa quando o contato fala pela primeira vez, quando a sessão anterior fica ociosa pelo tempo configurado na conexão, ou quando o atendimento é fechado no Nitzap. A cada sessão nova o contexto é enviado de novo.

# Encerrando o atendimento automaticamente

Quando a **mensagem por falta de resposta** é enviada, o Nitzap entende que a conversa acabou e faz três coisas, nesta ordem:

1. Encerra a sessão do agente e libera o número, para que a próxima mensagem do cliente comece uma conversa nova em vez de cair na fila antiga.
2. Envia a mensagem ao contato.
3. Avisa o Salesforce: a `Task` do atendimento é concluída, o Omni é atualizado e fica registrado no chat o aviso interno "Atendimento encerrado por inatividade do contato", visível só para os atendentes.

O passo 3 é o que fecha a janela do atendimento no Salesforce, e é o único que depende de configuração da sua organização. Ele usa o **mesmo aplicativo conectado** do agente, chamando a API do próprio pacote Nitzap. Não há nada para preencher no Nitzap: se as permissões abaixo estiverem corretas, funciona sozinho.

Para reagir a esse fechamento, por exemplo encerrar o Caso vinculado ou disparar uma pesquisa de satisfação, crie um Flow disparado pela `Task` quando `nitzap20__Date_Time_End_Chat__c` for preenchido.

## Permissões que só você pode liberar

O usuário que o aplicativo conectado usa para executar precisa conseguir chamar a API do pacote. Isso é concedido dentro da sua organização, e nem a Datago nem o pacote conseguem fazer por você.

**Se o usuário de execução tem licença Salesforce comum:** atribua a ele o conjunto de permissões **Nitzap 2.0**, que já vem no pacote. É só isso.

**Se o usuário de execução tem licença Salesforce Integration**, que é o padrão recomendado pela Salesforce para integrações:

1. O conjunto **Nitzap 2.0** não pode ser atribuído a essa licença, porque inclui acesso a uma página Visualforce que a licença não aceita. A org recusa a atribuição com a mensagem "A licença do usuário não permite Acesso à página do Visualforce".
2. Crie um conjunto de permissões próprio, por exemplo "Nitzap: Integração", com **apenas** o acesso à classe Apex **`NitzapServiceDeskRest`** do pacote, e atribua ao usuário. Nenhuma permissão de objeto, de campo ou licença adicional é necessária: o pacote grava o fechamento em contexto de sistema.

Além disso, no aplicativo conectado, o escopo **"Gerenciar dados do usuário via APIs (api)"** precisa estar marcado. Sem ele o agente continua respondendo, mas o atendimento não é concluído no Salesforce.

## Como saber se está funcionando

Depois de um atendimento encerrado por falta de resposta, confira na `Task` do atendimento:

- **Status** concluído e **Data/Hora de fim do chat** preenchida.
- No chat, o aviso interno "Atendimento encerrado por inatividade do contato".

Se a `Task` continuar aberta, a causa quase sempre é permissão. Em **Configuração › Trabalhos do Apex** e nos logs do aplicativo conectado você vê o erro; os mais comuns são:

| Mensagem | O que fazer |
|---|---|
| `You do not have access to the Apex class named: NitzapServiceDeskRest` | Falta o conjunto de permissões com acesso à classe no usuário de execução |
| `INSUFFICIENT_ACCESS_ON_CROSS_REFERENCE_ENTITY` | Pacote desatualizado: atualize para a versão que grava o fechamento em contexto de sistema |
| Nada acontece e o agente segue respondendo | Falta o escopo `api` no aplicativo conectado, ou as credenciais não estão salvas em Nitzap Config › Configurações › Credenciais Salesforce |

# Dúvidas frequentes sobre os tempos

As perguntas abaixo são as que mais aparecem na hora de parametrizar o bloco **Bot e agente** da conexão.

## Se o cliente demora a responder ao bot, em quanto tempo o bot recomeça do zero?

![Campo Ociosidade da sessão do bot](images/bot-ociosidade-sessao.png)

No tempo do campo **Ociosidade da sessão do bot**, e não no da pausa. Com 10 minutos configurados, se o cliente ficar 10 minutos sem responder, o bot encerra a conversa; em branco vale 30 minutos. Havendo mensagem por falta de resposta, ela é enviada nesse momento. Quando o cliente escrever de novo, o bot começa do zero.

## Nesse momento a tarefa é fechada no Salesforce?

Só se ela já estiver vinculada ao cliente. O Nitzap localiza o atendimento pelo Contato, Lead ou Conta que tem aquele telefone, e fecha a tarefa de atendimento aberta ligada a esse registro. Uma tarefa criada pelo bot na primeira mensagem, antes do cadastro, não aponta para ninguém e por isso continua aberta. Se o seu bot cria tarefas assim e você quer vê-las concluídas, use um Flow agendado na sua organização para fechar as que ficaram sem contato e sem movimentação.

Sem mensagem por falta de resposta configurada, nada é enviado e nada é fechado: a sessão do bot apenas expira.

## O bot transferiu para a fila e ninguém atendeu. O atendimento expira?

Não. Ele fica na fila até alguém puxar. O encerramento automático só começa a contar depois que um vendedor responde ao cliente; enquanto o cliente espera na fila, nada é enviado e nada é fechado.

São dois relógios independentes. O atendimento, que é a tarefa na fila do Salesforce, não tem prazo. O silêncio do bot tem: é a **Pausa após atendimento humano**. Quando ela vence, nada é encerrado; o bot só deixa de ficar calado e responde se o cliente escrever de novo.

Por isso o valor da pausa deve ser maior que o tempo máximo que um cliente pode esperar na fila. O padrão de 8 horas costuma cobrir um dia de trabalho.

## Se a pausa vencer com o cliente ainda na fila, o bot cria outro atendimento?

Quando o cliente escreve depois da pausa vencida, o bot recomeça a triagem do zero, e o atendimento anterior continua aberto na fila. O que acontece no fim da nova triagem depende de como o seu bot abre o atendimento:

| Como o bot abre o atendimento | Resultado |
|---|---|
| Com `createServiceDesk` do Nitzap | Não duplica. O método encontra o atendimento que já está aberto para aquele contato na conexão e devolve o mesmo; o cliente continua na fila em que estava |
| Criando a `Task` direto no Flow | Cria outra. Ficam duas tarefas de atendimento abertas para o mesmo cliente, e a antiga permanece na fila até alguém fechar |

É uma situação rara, porque exige que a pausa inteira passe sem ninguém puxar o atendimento. Para evitá-la, mantenha a pausa maior que a espera máxima na fila e prefira `createServiceDesk` para abrir o atendimento.

## Para que serve, afinal, a Pausa após atendimento humano?

![Campo Pausa após atendimento humano](images/bot-pausa-atendimento-humano.png)

É o tempo que o bot fica em silêncio para não atrapalhar o atendimento humano. Ela começa quando o bot transfere para a fila e recomeça a cada mensagem de um vendedor. O que acontece quando ela vence depende do momento:

| Momento | Quando a pausa vence |
|---|---|
| Cliente na fila, sem resposta de vendedor | Nada é enviado e o atendimento continua aberto. O bot apenas volta a atender, caso o cliente escreva de novo |
| Depois que um vendedor respondeu | Se o cliente não respondeu ao vendedor até o fim do tempo, a mensagem por falta de resposta é enviada e o atendimento é encerrado |

## Quando a mensagem por falta de resposta é enviada?

![Campo Mensagem por falta de resposta](images/bot-mensagem-falta-de-resposta.png)

Em dois momentos, sempre que o cliente para de responder:

- na conversa com o bot, ao fim da ociosidade da sessão;
- depois que um vendedor respondeu, ao fim da pausa após atendimento humano, contada da última mensagem do vendedor.

Ao ser enviada, ela encerra o atendimento, fecha a tarefa vinculada ao cliente e devolve a conversa ao bot. É cancelada se o cliente responder ou se o atendimento for fechado antes. Deixando o texto em branco, não existe encerramento automático.

Se o seu texto citar um tempo, como "nos últimos 5 minutos", confira se ele bate com os dois campos acima. O mesmo vale para a mensagem de transferência do bot: não prometa encerramento por tempo a quem vai esperar na fila, porque na fila nada é contado.

## E o campo "Tempo sem resposta (min)"?

Foi removido. O tempo da mensagem passou a ser o da ociosidade e o da pausa. Em pacotes anteriores o campo ainda aparece na tela, mas deixa de ter efeito assim que o servidor do Nitzap é atualizado.

## Posso deixar a pausa bem curta para encerrar rápido quem não responde ao vendedor?

Pode, mas a pausa é também o silêncio do bot na fila. Com pausa de 5 minutos, um cliente que espera 6 minutos por um vendedor e escreve "oi" é atendido pelo bot de novo. Escolha o valor pensando nas duas situações.

## O bot transferiu, mas a equipe não vê a conversa na fila. Por quê?

Três causas respondem por quase todos os casos:

- **O usuário não é membro da conexão.** Ser membro da fila no Salesforce não basta: o Omni só mostra conversas das conexões em que o usuário foi incluído, em Nitzap Config › Conexões › Membros.
- **O usuário nunca abriu o Nitzap.** O cadastro dele no servidor nasce no primeiro acesso.
- **A conversa está arquivada.** Conversa arquivada some da lista, da fila e dos alertas para todos os membros, e nada a desarquiva sozinha. Confira a aba Arquivadas.

No Omni, atendimentos que ainda estão em fila aparecem no filtro **Fila**. O filtro **Equipe** mostra os que já estão com uma pessoa, de qualquer atendente, nas conexões do usuário.

# O bot controlando o atendimento pelo Apex

O agente pode abrir, transferir e encerrar o atendimento chamando o Nitzap direto do Apex, de um Flow ou de uma ação invocável. Os três métodos fazem exatamente o que os botões do chat fazem: mexem na `Task`, avisam o Omni de todo mundo na hora e gravam no chat o aviso interno que só os atendentes veem.

Todos recebem o **Id da Task do atendimento**, nunca o do contato nem o da conversa, e podem ser chamados depois de gravar registros na mesma transação.

## Abrir o atendimento

`createServiceDesk` monta a `Task` no formato certo, não duplica atendimento aberto para o mesmo contato na mesma conexão, avisa o Omni e registra "iniciou o atendimento" com o link da tarefa:

```apex
nitzap20.NitzapApi.NewServiceDesk novo = new nitzap20.NitzapApi.NewServiceDesk();
novo.whoId = contato.Id;                  // contato ou lead; use whatId para Caso ou Oportunidade
novo.ownerId = filaComercial.Id;          // usuário ou fila; em branco fica com quem executa
novo.connectionNumber = '5514981770936';  // conexão que recebeu a mensagem
novo.subject = 'Atendimento via bot';     // opcional

nitzap20.NitzapApi.ServiceDeskCreation atendimento = nitzap20.NitzapApi.createServiceDesk(novo);
```

O retorno traz `taskId`, a tarefa do atendimento, e `created`, que vem `false` quando já existia atendimento aberto e nenhum outro foi criado.

Dono usuário abre o atendimento direto para ele; dono fila coloca a conversa na fila para alguém puxar.

## Transferir o atendimento

`transferServiceDesk` troca o responsável, respeita a opção "Fechar tarefa ao transferir" das configurações do app, notifica o novo responsável e registra "transferiu o atendimento de A para B":

```apex
nitzap20.NitzapApi.ServiceDeskTransfer movido =
    nitzap20.NitzapApi.transferServiceDesk(atendimento.Id, filaComercial.Id);   // usuário ou fila
```

O retorno diz qual `Task` segue como atendimento, útil quando a opção de fechar ao transferir cria uma nova.

## Encerrar o atendimento

`closeServiceDesk` conclui a `Task`, avisa o Omni, encerra a sessão do agente e, só depois disso, envia a mensagem de despedida ao contato:

```apex
nitzap20.NitzapApi.closeServiceDesk(
    atendimento.Id,
    'Nossa conversa foi encerrada. Qualquer problema pode me chamar por aqui novamente.'
);
```

A despedida é opcional: passando em branco, o atendimento encerra sem enviar nada.

Se o seu bot cria a Task de atendimento logo na primeira mensagem, antes de cadastrar o cliente, ela ainda não tem contato vinculado quando o cliente desiste, e o Nitzap não consegue descobrir qual conversa encerrar. Nesse caso use a forma com objeto e informe o telefone, que o bot já tem na variável `nitzap_contact_phone`:

```apex
nitzap20.NitzapApi.ServiceDeskClosure fechamento = new nitzap20.NitzapApi.ServiceDeskClosure();
fechamento.taskId = atendimento.Id;
fechamento.farewellMessage = 'Tudo bem! Se mudar de ideia, é só chamar.';
fechamento.contactPhone = telefoneDoCliente;   // variável nitzap_contact_phone
nitzap20.NitzapApi.closeServiceDesk(fechamento);
```

Sem contato na Task e sem telefone, o método recusa a chamada com erro claro, em vez de fechar a Task e deixar o bot sem responder.

**Não envie a despedida por conta própria em paralelo.** Se ela sair antes de o Nitzap encerrar a sessão do agente, conta como mensagem de atendimento e reinicia a contagem da mensagem por falta de resposta, e o cliente recebe "conversa encerrada por inatividade" minutos depois de já ter sido despedido. Deixando o texto no `closeServiceDesk`, a ordem fica garantida.

Os três métodos estão detalhados, com todas as regras e mensagens de erro, nas seções 14 a 16 de:
https://github.com/DataGo-Dev/datago-public/blob/main/docs/apex_usage.md

# Alternativa: criar a tarefa por conta própria

Se o seu bot já cria ou atualiza a `Task` do atendimento do jeito dele, use `notifyServiceDeskChangeAsync` para avisar o Nitzap depois. Sem isso, a conversa só aparece como atendida no Omni de quem recarregar a tela.

```apex
nitzap20.NitzapApi.notifyServiceDeskChangeAsync(atendimento.Id);
```

A ação é deduzida do estado da própria tarefa: dona usuário abre atendimento, dona fila manda para a fila e tarefa encerrada fecha o atendimento.

Nesse caminho, três campos precisam estar preenchidos na criação para o Nitzap reconhecer a tarefa e conseguir ler a conversa dentro dela:

| Campo | Valor | Por quê |
|---|---|---|
| `nitzap20__TaskType__c` | `SERVICE_DESK` | É o que marca a tarefa como atendimento. Sem isso o Nitzap não a trata como atendimento e `notifyServiceDeskChange` lança erro |
| `nitzap20__Connection_Number__c` | número da conexão que recebeu a mensagem | Diz de qual conexão é o atendimento. É por ele que o aviso chega no Omni certo e que o chat sabe qual número usar |
| `nitzap20__Date_Time_Start_Chat__c` | momento em que o atendimento começou | Marca o início do histórico. É a partir dessa data que o Nitzap lê as mensagens da conversa dentro da tarefa; em branco, a tarefa abre sem histórico |

Os detalhes desse caminho estão na seção 13 de:
https://github.com/DataGo-Dev/datago-public/blob/main/docs/apex_usage.md

Esse mesmo guia traz tudo o que o bot pode fazer pelo Apex: enviar mensagens e templates, ler conversas, consultar métricas e encontrar o registro de um telefone.

# Testando o agente

Para testar o agente várias vezes com o mesmo telefone, sem esperar a pausa ou a ociosidade acabarem, envie a mensagem `/restart-agent` do celular de teste para o número da conexão. Maiúsculas e espaços antes ou depois não fazem diferença.

O comando faz o seguinte:

- Tira a pausa do agente nessa conversa.
- Marca o atendimento como fechado no Nitzap e cancela a mensagem por falta de resposta que estiver agendada.
- Encerra a sessão do agente. A próxima mensagem começa uma conversa nova, e o contexto do contato é enviado de novo.

Observações:

- A `Task` do atendimento **não é concluída** no Salesforce. Se havia um atendimento aberto, feche-o pelo Nitzap ou pelo `closeServiceDesk`.
- O comando é para testes, mas não é restrito: qualquer contato que enviar `/restart-agent` reinicia o agente na própria conversa.

Para quaisquer dúvidas entre em contato com a Datago +55 27 99997-0276

- João








