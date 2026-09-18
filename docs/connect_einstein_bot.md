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
Em Nitzap Config vá até Conexões > Conexões, Escolha uma conexão com a Meta Oficial (Ou adicione). 
Obs: Essa configuração só funciona com Api Oficial do Nitzap.
<img width="1146" height="338" alt="image" src="https://github.com/user-attachments/assets/36c64af3-9651-4415-9775-eaa1cc85cad9" />

Clique na conexão e vá em configurações > Resposta Automática (bot/agent)
<img width="1112" height="200" alt="image" src="https://github.com/user-attachments/assets/dd83b7cb-eb9a-4f3e-8eeb-7144c0bf0064" />

Escolha o tipo de Bot
<img width="1102" height="268" alt="image" src="https://github.com/user-attachments/assets/bc32bced-fc03-4595-a103-f6ebb7640669" />
Ao escolher coloque o Agente ou Bot no campo Agentforce: agente desta conexão

Pronto, você configurou seu Bot!

Agora quando Alguém enviar mensagem para seu Bot, ele entrará em ação. 

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

# Avisando o Nitzap quando o bot abre ou transfere um atendimento

Se o seu bot cria a tarefa de atendimento direto no Salesforce, a conversa só aparece como atendida no Omni de quem estiver com a tela aberta depois de recarregar. Para avisar na hora, chame:

```apex
nitzap20.NitzapApi.notifyServiceDeskChangeAsync(atendimento.Id);
```

Ele publica o mesmo aviso que a tela do chat manda ao iniciar, transferir ou encerrar um atendimento. A ação é deduzida da própria tarefa: dona usuário abre atendimento, dona fila manda para a fila e tarefa encerrada fecha o atendimento. A versão assíncrona é a que serve depois de criar ou atualizar a tarefa na mesma transação.

A tarefa precisa ter o tipo `SERVICE_DESK` e o campo `nitzap20__Connection_Number__c` com o número da conexão. Os detalhes estão na seção 13 de:
https://github.com/DataGo-Dev/datago-public/blob/main/docs/apex_usage.md

Para personalizar ainda mais seu bot leia:
https://github.com/DataGo-Dev/datago-public/blob/main/docs/apex_usage.md

Para quaisquer dúvidas entre em contato com a Datago +55 27 99997-0276

- João








