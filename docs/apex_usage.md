# Nitzap — API Apex para Desenvolvedores

A classe `nitzap20.NitzapApi` expõe as operações do Nitzap para o seu código Apex: enviar mensagens de texto e mídia, listar templates Meta, enviar templates com variáveis e ler o histórico das conversas — sempre informando **qual conexão (número de WhatsApp)** origina a operação.

## Pré-requisitos

- Pacote Nitzap instalado e configurado no org (backend conectado).
- O número da conexão que vai enviar (ex.: `5514981770936`). Você encontra os números conectados na tela de conexões do Nitzap, ou via Apex:

```apex
for(nitzap20.NitzapApi.ConnectionInfo c : nitzap20.NitzapApi.listConnections()){
    // c.connectionNumber, c.label, c.channel (NITZAP | WABA_COEX), c.active, c.memberCount
}
```

Para saber as conexões de usuários específicos (ex.: descobrir por qual número cada atendente envia), use `getUserConnections` — todo userId pedido volta na resposta, com lista vazia se não tiver conexão:

```apex
List<nitzap20.NitzapApi.UserConnections> result =
    nitzap20.NitzapApi.getUserConnections(new List<String>{ userA.Id, userB.Id });

for(nitzap20.NitzapApi.UserConnections uc : result){
    // uc.userId, uc.connections -> List<ConnectionInfo> (connectionNumber, label, channel, active)
}
```

O caminho inverso, descobrir quem atende por um número, é `getConnectionMembers`. Recebe o número da conexão e devolve os usuários vinculados a ela, com o Id e o nome do usuário Salesforce e as permissões de cada um na conexão:

```apex
List<nitzap20.NitzapApi.ConnectionMember> membros =
    nitzap20.NitzapApi.getConnectionMembers('5514981770936');

for(nitzap20.NitzapApi.ConnectionMember m : membros){
    // m.userId (Id do User), m.name, m.isOwner, m.canSend, m.canReceive
}
```

Usuários integradores aparecem na lista com o próprio identificador no lugar do Id, já que não são usuários Salesforce. Número em branco lança `NitzapApiException` antes do callout.
- Recursos Meta (templates) exigem que a conexão seja um canal WABA/Coex.
- **Autenticação**: a API usa a **credencial do sistema** (usuário integrador salvo nas configurações — criado automaticamente na primeira abertura da tela de Configurações pelo admin, ou salvo manualmente pelo botão "Salvar nas credenciais do sistema" na aba Usuários Integradores). Com ela configurada, os envios funcionam de qualquer contexto — flows, batches, usuários que nunca conectaram ao Nitzap. Sem ela, a API cai no token do usuário que está executando, que precisa estar conectado e ativo.

Todos os métodos são estáticos. Em caso de entrada inválida a API lança `nitzap20.NitzapApi.NitzapApiException` **antes** de qualquer callout; o resultado dos envios vem num `SendResult`:

```apex
nitzap20.NitzapApi.SendResult r = ...;
r.success;       // Boolean
r.statusCode;    // Integer (HTTP)
r.errorMessage;  // String, preenchida quando success = false
r.responseBody;  // String, corpo cru da resposta
```

---

## 1. Obter o access token de um usuário

Para chamadas customizadas direto ao backend (a maioria dos casos não precisa disso — os métodos abaixo já autenticam sozinhos):

```apex
String token = nitzap20.NitzapApi.getAccessToken(UserInfo.getUserId());
```

## 2. Enviar mensagem de texto

```apex
nitzap20.NitzapApi.SendResult r =
    nitzap20.NitzapApi.sendText('5514981770936', '5527997019622', 'Olá! Seu pedido saiu para entrega.');

if(!r.success){
    System.debug('Falhou: ' + r.errorMessage);
}
```

O número de destino aceita formatação (`+55 (27) 99701-9622`) — a API normaliza.

## 3. Enviar mídia a partir de um arquivo do Salesforce

Passe o Id de um `ContentVersion`. A API sobe o arquivo para o storage do Nitzap e infere o tipo (`image`, `video`, `audio`, `document`) pelo mimeType:

```apex
ContentVersion cv = [SELECT Id FROM ContentVersion WHERE Title = 'boleto' LIMIT 1];

nitzap20.NitzapApi.sendMedia('5514981770936', '5527997019622', cv.Id, 'Segue o boleto 📎');
```

## 4. Controle total com `Message`

Para citar mensagem, aplicar delay, usar URL de mídia externa ou enviar como outro usuário:

```apex
nitzap20.NitzapApi.Message msg =
    new nitzap20.NitzapApi.Message('5514981770936', '5527997019622', 'legenda opcional');
msg.mediaUrl = 'https://exemplo.com/catalogo.pdf';
msg.mediaMimeType = 'application/pdf';   // obrigatório com mediaUrl (ou informe msg.type)
msg.quotedMessageKey = 'ABCD1234';       // opcional: responde citando
msg.delay = 2;                           // opcional: segundos entre envios
msg.senderUserId = ownerId;              // opcional: default é o usuário atual

nitzap20.NitzapApi.send(msg);
```

## 5. Envio em lote e envio assíncrono

`sendBatch` agrupa tudo em um callout por remetente:

```apex
List<nitzap20.NitzapApi.Message> msgs = new List<nitzap20.NitzapApi.Message>();
for(Contact c : contatos){
    msgs.add(new nitzap20.NitzapApi.Message('5514981770936', c.nitzap20__WhatsAppId__c, 'Olá ' + c.FirstName + '!'));
}
nitzap20.NitzapApi.sendBatch(msgs);
```

**Importante — callout depois de DML:** se a sua transação já fez `insert`/`update`, um envio síncrono lança `CalloutException`. Use a variante assíncrona, que enfileira um Queueable:

```apex
update minhasContas;
nitzap20.NitzapApi.sendBatchAsync(msgs);  // retorna o Id do job
```

## 6. Listar templates Meta de uma conexão

```apex
List<nitzap20.NitzapApi.MetaTemplate> tpls = nitzap20.NitzapApi.getMetaTemplates('5514981770936');

for(nitzap20.NitzapApi.MetaTemplate t : tpls){
    System.debug(t.name + ' [' + t.status + '] formato=' + t.parameterFormat
        + ' variáveis=' + t.placeholders);
}
```

Campos úteis do `MetaTemplate`:

| Campo | Conteúdo |
|---|---|
| `name`, `language`, `status`, `category` | Metadados do template na Meta (`status` deve ser `APPROVED` para envio) |
| `parameterFormat` | `POSITIONAL` (variáveis `{{1}}`, `{{2}}`) ou `NAMED` (`{{cliente}}`) |
| `placeholders` | Lista das variáveis do body, ex.: `['1','2']` ou `['cliente','cidade_cliente']` |
| `headerFormat` | `TEXT`, `IMAGE`, `VIDEO`... quando o template tem header |
| `bodyText` | Texto do body com os placeholders |

## 7. Enviar template Meta com variáveis

As variáveis vão num `Map<String, String>`. Use o `parameterFormat` do template para saber o formato das chaves:

**Template posicional** (`Olá {{1}}, seu pedido {{2}} saiu`):

```apex
nitzap20.NitzapApi.TemplateMessage tpl =
    new nitzap20.NitzapApi.TemplateMessage('5514981770936', '5527997019622', 'pedido_enviado', 'pt_BR');
tpl.bodyParams = new Map<String, String>{ '1' => 'João', '2' => 'Pedido 123' };

nitzap20.NitzapApi.sendMetaTemplate(tpl);
```

**Template nomeado** (`Oi {{cliente}}, bem-vindo a {{cidade_cliente}}!`):

```apex
tpl.bodyParams = new Map<String, String>{
    'cliente' => 'João',
    'cidade_cliente' => 'Bauru'
};
```

Regras validadas antes do envio (lançam `NitzapApiException` com a variável exata no erro):

- Não misture chaves numéricas com nomeadas no mesmo mapa.
- Posicional deve ser contíguo: com 3 variáveis, informe `1`, `2` e `3`.

**Template com header de mídia** — por arquivo do Salesforce ou URL:

```apex
tpl.headerFileId = contentVersionId;              // sobe pro storage e infere image/video

// ou
tpl.headerMediaUrl = 'https://exemplo.com/banner.png';
tpl.headerMediaType = 'image';                    // obrigatório com headerMediaUrl
```

### Lote de templates (`sendMetaTemplateBatch`)

Para envio em massa, monte uma lista da mesma `TemplateMessage` do envio unitário — cada item com seu destinatário e suas próprias variáveis. A API valida item a item **antes** de qualquer callout (se um item estiver inválido, nada é enviado), agrupa por conexão/remetente e faz 1 callout por grupo.

**Caso típico — campanha com variáveis por registro:**

```apex
List<Contact> contatos = [
    SELECT FirstName, nitzap20__WhatsAppId__c, Account.Name
    FROM Contact
    WHERE nitzap20__WhatsAppId__c != null AND Aceita_WhatsApp__c = true
];

List<nitzap20.NitzapApi.TemplateMessage> lote = new List<nitzap20.NitzapApi.TemplateMessage>();
for(Contact c : contatos){
    nitzap20.NitzapApi.TemplateMessage tpl = new nitzap20.NitzapApi.TemplateMessage(
        '5514981770936',                 // conexão que envia
        c.nitzap20__WhatsAppId__c,       // destinatário
        'boas_vindas',                   // template aprovado na Meta
        'pt_BR');
    tpl.bodyParams = new Map<String, String>{
        'cliente' => c.FirstName,
        'empresa' => c.Account.Name
    };
    lote.add(tpl);
}

nitzap20.NitzapApi.SendResult r = nitzap20.NitzapApi.sendMetaTemplateBatch(lote);
if(!r.success){
    System.debug('Falha no lote: ' + r.errorMessage);
}
```

**Misturando templates diferentes no mesmo lote** — cada item é independente; dá pra variar template, formato de variável e até a conexão:

```apex
List<nitzap20.NitzapApi.TemplateMessage> lote = new List<nitzap20.NitzapApi.TemplateMessage>();

// item 1: template posicional
nitzap20.NitzapApi.TemplateMessage cobranca = new nitzap20.NitzapApi.TemplateMessage(
    '5514981770936', '5527997019622', 'lembrete_pagamento', 'pt_BR');
cobranca.bodyParams = new Map<String, String>{ '1' => 'João', '2' => 'R$ 149,90', '3' => '25/07' };
lote.add(cobranca);

// item 2: template nomeado com imagem no header
nitzap20.NitzapApi.TemplateMessage promo = new nitzap20.NitzapApi.TemplateMessage(
    '5514981770936', '5511988887777', 'promo_semana', 'pt_BR');
promo.bodyParams = new Map<String, String>{ 'nome_cliente' => 'Maria' };
promo.headerFileId = bannerContentVersionId;
lote.add(promo);

// item 3: outra conexão (vira um segundo callout, agrupado automaticamente)
lote.add(new nitzap20.NitzapApi.TemplateMessage(
    '5527997419613', '5531977776666', 'follow_up', 'en'));

nitzap20.NitzapApi.sendMetaTemplateBatch(lote);
```

**Validação em massa antes de montar o lote** — cruze com `getMetaTemplates` para pular registros que não casam com o template (em vez de deixar o lote inteiro falhar na validação):

```apex
Map<String, nitzap20.NitzapApi.MetaTemplate> porNome = new Map<String, nitzap20.NitzapApi.MetaTemplate>();
for(nitzap20.NitzapApi.MetaTemplate t : nitzap20.NitzapApi.getMetaTemplates('5514981770936')){
    if(t.status == 'APPROVED'){ porNome.put(t.name, t); }
}

nitzap20.NitzapApi.MetaTemplate alvo = porNome.get('boas_vindas');
System.assert(alvo != null, 'Template não aprovado ou inexistente');
// alvo.parameterFormat -> 'NAMED' | 'POSITIONAL'
// alvo.placeholders    -> chaves exatas que o bodyParams precisa preencher
```

Pontos de atenção no lote:

- **Volume**: o backend enfileira os envios (resposta `{"enqueued": N}`) e a Meta aplica os limites de messaging da WABA — o lote retornar `success = true` significa "aceito na fila", não "entregue".
- **Callouts**: itens da mesma conexão+remetente compartilham 1 callout; cada `headerFileId` distinto adiciona 2 callouts (upload). Para lotes grandes dentro de transações com DML, dispare de um Queueable/Batch seu.
- **Falha parcial**: se um grupo falhar (ex.: conexão inativa), o `SendResult.errorMessage` acumula os erros separados por `|` e `success` fica `false`, mas os grupos que deram certo já foram aceitos.

**Modo avançado (`sendMetaTemplateRaw`)** — para componentes que o `TemplateMessage` não cobre (botões com `sub_type`/`index`, flows com `flow_token`, carrossel), monte o payload da [Cloud API da Meta](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates) você mesmo; a API cuida da autenticação, do `vFrom` e preenche `messaging_product`/`recipient_type`/`type` se você omitir:

```apex
Map<String, Object> payload = new Map<String, Object>{
    'to' => '5527997019622',
    'template' => new Map<String, Object>{
        'name' => 'nps_pesquisa',
        'language' => new Map<String, Object>{ 'code' => 'pt_BR' },
        'components' => new List<Object>{
            new Map<String, Object>{
                'type' => 'button',
                'sub_type' => 'flow',
                'index' => '0',
                'parameters' => new List<Object>{
                    new Map<String, Object>{
                        'type' => 'action',
                        'action' => new Map<String, Object>{ 'flow_token' => 'meu-token' }
                    }
                }
            }
        }
    }
};

nitzap20.NitzapApi.sendMetaTemplateRaw('5514981770936', new List<Map<String, Object>>{payload});
```

## 8. Resumo de uma conversa em um período (`getChatSummary`)

Retorna totais e primeiras mensagens de cada conversa dentro de uma janela de tempo — útil para medir se o contato respondeu a uma campanha, tempo de primeira resposta etc. Aceita várias conversas por chamada (1 callout só):

```apex
nitzap20.NitzapApi.ChatSummaryRequest req = new nitzap20.NitzapApi.ChatSummaryRequest(
    '5514981770936',                      // conexão
    '5527997019622',                      // contato
    DateTime.newInstance(2026, 7, 1),     // início da janela
    System.now());                        // fim da janela
req.referenceId = contato.Id;             // opcional: eco para correlacionar em lote

List<nitzap20.NitzapApi.ChatSummaryResult> results =
    nitzap20.NitzapApi.getChatSummary(new List<nitzap20.NitzapApi.ChatSummaryRequest>{req});

nitzap20.NitzapApi.ChatSummaryResult r = results[0];
r.totalSentMessages;      // enviadas na janela
r.totalReceivedMessages;  // recebidas na janela
r.firstSentAt;            // DateTime da primeira enviada (null se nenhuma)
r.firstReceivedAt;        // DateTime da primeira recebida (null se nenhuma)
r.contactAnswered;        // true se o contato mandou ao menos 1 mensagem na janela
r.firstMessageWasMine;    // true se a primeira mensagem da janela foi sua
```

## 9. Listar conversas (`listChats` / `getChats`)

### Sem filtro, só paginando (`listChats`)

Passe o **número da conexão** e receba as conversas dela, da mais recente para a mais antiga (50 por página por padrão, máximo 200):

```apex
List<nitzap20.NitzapApi.ChatInfo> chats =
    nitzap20.NitzapApi.listChats('5514981770936');            // conexão

List<nitzap20.NitzapApi.ChatInfo> pagina =
    nitzap20.NitzapApi.listChats('5514981770936', 100);       // com take
```

A paginação usa o mesmo cursor por `sequence` do `getMessages` (seção 10): guarde o `sequence` do **último** chat da página e peça o que vier antes dele:

```apex
List<nitzap20.NitzapApi.ChatInfo> pagina = nitzap20.NitzapApi.listChats('5514981770936', 100);
while(!pagina.isEmpty()){
    // processar...
    Long cursor = pagina[pagina.size() - 1].sequence;
    pagina = nitzap20.NitzapApi.listChats('5514981770936', 100, cursor);
}
```

Pare quando a página vier vazia ou com menos itens que o `take`.

### Metadados de uma conversa específica (`getChatMetadata`)

Quando você já sabe a conexão e o contato, busque direto os metadados daquela conversa:

```apex
nitzap20.NitzapApi.ChatInfo chat =
    nitzap20.NitzapApi.getChatMetadata('5514981770936', '5527997019622');   // conexão, contato
```

O contato aceita formatação (`+55 (27) 99701-9622`) ou um id de grupo (`120363...@g.us`); as variações do 9º dígito brasileiro são resolvidas no servidor. Se a conversa não existir, o retorno é `null` — não é erro.

### Com filtro customizado (`getChats`)

Busca os metadados das conversas (última mensagem, totais, não lidas) passando a condição `where` diretamente — flexível e customizável:

```apex
List<nitzap20.NitzapApi.ChatInfo> chats = nitzap20.NitzapApi.getChats(
    'mywhatsid = \'5514981770936@s.whatsapp.net\' AND isgroup = false');
```

Colunas disponíveis para o filtro:

| Coluna | Conteúdo | Exemplo |
|---|---|---|
| `chat_id` | `<conexão>_<contato>` (só dígitos) | `chat_id = '5514981770936_5527997019622'` |
| `mywhatsid` | conexão, com sufixo `@s.whatsapp.net` | `mywhatsid = '5514981770936@s.whatsapp.net'` |
| `secondwhatsappid` | contato (`@s.whatsapp.net`) ou grupo (`@g.us`) | `secondwhatsappid LIKE '5527997019622@%'` |
| `isgroup`, `archived` | booleanos | `isgroup = false` |
| `dt_lastmessage` | timestamp da última mensagem | `dt_lastmessage >= '2026-07-01 00:00:00+00'` |
| `unread_messages` | não lidas | `unread_messages > 0` |
| `last_salesforce_user` | último usuário SF que interagiu | `last_salesforce_user = '005...'` |

Campos do `ChatInfo` retornado:

```apex
for(nitzap20.NitzapApi.ChatInfo c : chats){
    c.chatId;               // '5514981770936_5527997019622'
    c.connectionNumber;     // lado da conexão
    c.contactNumber;        // lado do contato (ou id do grupo)
    c.name;                 // nome do contato (pushname)
    c.isGroup; c.groupName;
    c.lastMessageAt;        // DateTime da última mensagem
    c.lastMessageText;      // prévia do texto
    c.lastMessageType;      // text, image, video...
    c.lastMessageFromMe;    // true se a última foi enviada por você
    c.totalMessages; c.totalSent; c.totalReceived;   // podem vir null em chats antigos
    c.unreadMessages;
    c.lastSalesforceUserId; // último usuário SF que interagiu
    c.sequence;             // Long — cursor de paginação do listChats
    c.lastCtwaClid;         // click id do último anúncio Click-to-WhatsApp (CTWA), se houver
}
```

A condição vai direto para o banco do backend — monte valores com cuidado (números sem formatação, datas em UTC no formato `YYYY-MM-DD HH:MM:SS+00`). Erro de sintaxe retorna como `NitzapApiException` com a mensagem do servidor.

---

## 10. Ler as mensagens de uma conversa (`getMessages`)

Enquanto o `listChats`/`getChats` listam as conversas, o `getMessages` devolve as **mensagens** de uma delas. O primeiro parâmetro é sempre o **número da conexão** (o seu número no Nitzap) e o segundo é o **número do contato** com quem é a conversa. A chamada mais simples traz a última página (50 mensagens, da mais recente para a mais antiga):

```apex
List<nitzap20.NitzapApi.ChatMessage> msgs = nitzap20.NitzapApi.getMessages(
    '5514981770936',    // conexão: o SEU número (o mesmo de listConnections)
    '5527997019622');   // contato: o número da outra ponta da conversa
```

Com `take` para limitar a quantidade:

```apex
List<nitzap20.NitzapApi.ChatMessage> ultimas10 =
    nitzap20.NitzapApi.getMessages('5514981770936', '5527997019622', 10);
```

O contato aceita formatação (`+55 (27) 99701-9622`) ou um id de grupo (`120363...@g.us`). Se a conversa não existir, a resposta é uma lista vazia — não é erro.

Campos do `ChatMessage`:

```apex
for(nitzap20.NitzapApi.ChatMessage m : msgs){
    m.id;                 // id interno, use para deduplicar
    m.messageKey;         // msgkey do WhatsApp (o mesmo usado em respostas/reações)
    m.chatId;             // '5514981770936_5527997019622'
    m.connectionNumber;   // lado da conexão
    m.contactNumber;      // lado do contato (ou id do grupo)
    m.sender; m.receiver; m.participant;   // participant preenchido em grupo
    m.type;               // text, image, video, audio, document, location...
    m.text;               // texto ou legenda da mídia
    m.sentAt;             // DateTime da mensagem
    m.sequence;           // Long — o cursor de paginação (veja abaixo)
    m.fromMe;             // true se foi você quem enviou
    m.isGroup; m.pushName;
    m.mediaUrl;           // link S3 pré-assinado, válido ~2h — não persista
    m.mediaMimeType; m.mediaFileName;
    m.transcription; m.summary;   // quando existirem (áudio transcrito, resumo)
    m.status; m.channel; m.origin;
    m.salesforceUserId;   // Id do usuário Salesforce que enviou; em mensagens enviadas por fora do Nitzap (celular, WhatsApp Web) é o usuário principal da conexão; null nas recebidas ou sem usuário
    m.deleted; m.forwarded; m.edited;
    m.readAt;             // DateTime da leitura, null se não lida
    m.quotedMessageKey;   // msgkey da mensagem citada
    m.quotedMessage;      // a mensagem citada inteira (ChatMessage), quando houver
    m.reactions;          // List<MessageReaction>: messageKey, reaction, participant, pushName
    m.ctwaClid;           // click id do anúncio Click-to-WhatsApp que originou a mensagem, se houver
}
```

⚠️ **Não guarde o `mediaUrl`** no seu banco: ele expira em ~2h. Guarde o `messageKey`/`id` e releia a mensagem quando precisar do arquivo de novo.

### Paginação — cursor por `sequence`, nunca offset

`sequence` é o carimbo de gravação da mensagem (epoch em milissegundos). Para carregar o histórico, guarde o `sequence` da **última** mensagem da página e peça o que for mais antigo que ele:

```apex
List<nitzap20.NitzapApi.ChatMessage> pagina =
    nitzap20.NitzapApi.getMessages('5514981770936', '5527997019622', 50);

while(!pagina.isEmpty()){
    Long cursor = pagina[pagina.size() - 1].sequence;   // ordem padrão: o último é o mais antigo
    pagina = nitzap20.NitzapApi.getOlderMessages('5514981770936', '5527997019622', cursor, 50);
    // processar...
}
```

Pare quando a página vier vazia ou com menos itens que o `take`. Duas mensagens gravadas no mesmo milissegundo compartilham o `sequence`, então **deduplique por `id`** (um `Set<String>`) do seu lado — o cursor sozinho não garante isso.

Para o caminho inverso — pegar só o que chegou depois da última sincronização — use `getMessagesAfter`, que já pede em ordem crescente e não deixa buraco quando acumulou mais mensagens que o `take`:

```apex
Long ultimoProcessado = 1783966686472L;   // guardado por conversa no seu org

List<nitzap20.NitzapApi.ChatMessage> novas =
    nitzap20.NitzapApi.getMessagesAfter('5514981770936', '5527997019622', ultimoProcessado, 100);
```

### Controle total com `MessageQuery`

Quando precisar de outra combinação (enviar por outro usuário, inverter a ordem, usar outro operador de cursor):

```apex
nitzap20.NitzapApi.MessageQuery q =
    new nitzap20.NitzapApi.MessageQuery('5514981770936', '5527997019622');
q.take = 100;
q.sequence = 1783966686472L;   // cursor
q.follow = 'lt';               // lt | lte | gt | gte — default 'lt' quando há sequence
q.ascending = true;            // true = mais antigas primeiro
q.senderUserId = atendente.Id; // opcional: lê com o token desse usuário

List<nitzap20.NitzapApi.ChatMessage> msgs = nitzap20.NitzapApi.getMessages(q);
```

O `skip` existe (`q.skip`) mas **evite**: com offset, uma mensagem nova chegando entre duas páginas empurra a lista e você lê a mesma mensagem duas vezes (ou pula uma, se alguma for apagada). O cursor por `sequence` é ancorado no dado e não sofre disso.

Erros de leitura (conexão não autorizada para o token, backend fora) vêm como `NitzapApiException` — diferente dos envios, que devolvem `SendResult`.

---

## 11. Utilitário: variações brasileiras de número (`getPossibleBrazilianVariations`)

Números brasileiros existem no WhatsApp com e sem o nono dígito. Ao buscar um contato por telefone (SOQL em `WhatsAppId__c`, montar `where` do `getChats`...), teste todas as variações:

```apex
List<String> variacoes = nitzap20.NitzapApi.getPossibleBrazilianVariations('5527997019622');
// ['5527997019622', '552797019622']  — original sempre primeiro

List<Contact> contatos = [SELECT Id FROM Contact WHERE nitzap20__WhatsAppId__c IN :variacoes];
```

Números não-brasileiros e ids de grupo (`@g.us`) voltam como lista de um item. É lógica local — não faz callout.

---

## 12. Encontrar o registro de um telefone (`findRecordByPhone`)

Dado um telefone, devolve o **Id do registro Salesforce canônico** daquele número — o mesmo que o Nitzap usa para vincular conversas — ou `null` se nenhum registro tiver o número:

```apex
Id recordId = nitzap20.NitzapApi.findRecordByPhone('5527997019622');
if(recordId != null){
    String objectName = recordId.getSObjectType().getDescribe().getName(); // Account, Contact ou Lead
}
```

Como a busca funciona:

- O telefone aceita formatação (`+55 (27) 99701-9622`) e as variações brasileiras do nono dígito são testadas automaticamente.
- Procura em `Account`, `Contact` e `Lead` pelo campo `nitzap20__WhatsAppId__c`.
- Com mais de um registro no mesmo número, o desempate segue a regra canônica do Nitzap: registro com atendimento em andamento vem primeiro; depois Account > Contact > Lead; por fim o mais antigo.
- A preferência **Priorizar Contatos**, nas configurações do Nitzap, inverte só a parte do meio: Contact passa a vir antes de Account. O atendimento em andamento continua vencendo os dois.
- A busca é sempre na base inteira, sem restrição de papéis/visibilidade do omni — o Id volta mesmo que o usuário atual não enxergue o registro. Cheque o acesso antes de expor dados dele (ex.: `UserRecordAccess`).

É consulta local (SOQL) — não faz callout.

---

## 13. Avisar o Omni de um atendimento criado por código (`notifyServiceDeskChange`)

Quando um atendente inicia, transfere ou encerra um atendimento pela tela do Nitzap, o Omni de todo mundo atualiza na hora, porque o chat publica um evento no canal da conexão. Um bot, um Flow ou um agente que cria a `Task` de atendimento direto no banco não dispara esse evento, e o Omni só percebe no próximo recarregar. `notifyServiceDeskChange` publica o mesmo evento a partir de uma `Task`:

```apex
Task atendimento = new Task(
    WhoId = contato.Id,
    OwnerId = filaComercial.Id,                          // usuário ou fila
    Subject = 'Atendimento via bot',
    nitzap20__TaskType__c = 'SERVICE_DESK',
    nitzap20__Connection_Number__c = '5514981770936',    // obrigatório
    nitzap20__Date_Time_Start_Chat__c = System.now()
);
insert atendimento;

nitzap20.NitzapApi.notifyServiceDeskChangeAsync(atendimento.Id);  // retorna o Id do job
```

O método lê a `Task`, monta o evento com o dono atual (usuário ou fila), o registro vinculado (`WhoId`/`WhatId`) e a conexão, e publica no canal dessa conexão. Todo usuário dela com o Omni aberto recebe. A ação é deduzida do estado da `Task`:

| Estado da Task | Ação publicada | Efeito no Omni |
|---|---|---|
| Aberta, dona é usuário, nunca transferida | `create` | Conversa entra em **Meus** e **Atendendo** do dono, com o aviso "Novo atendimento para você" |
| Aberta, dona é usuário, `nitzap20__Date_Transfer_service__c` preenchido | `transfer` | Mesmo efeito de `create` |
| Aberta, dona é fila | `transfer_to_group` | Conversa entra em **Fila** dos membros e o item mostra "Na fila X" |
| `IsClosed` ou `nitzap20__Date_Time_End_Chat__c` preenchido | `close` | Conversa sai dos filtros de atendimento |

Regras:

- O parâmetro é o **Id da `Task` do atendimento** — não o do contato nem o do registro vinculado. Outro tipo de Id lança `NitzapApiException`.
- A `Task` precisa ter `nitzap20__TaskType__c = 'SERVICE_DESK'` e `nitzap20__Connection_Number__c` com o número da conexão do atendimento. Sem isso lança `NitzapApiException`. Com dona usuário e número em branco, o método ainda tenta o `nitzap20__WhatsAppId__c` legado do usuário.
- Preencha também `nitzap20__Date_Time_Start_Chat__c` na criação: é o início do histórico, a data a partir da qual o Nitzap lê as mensagens da conversa dentro da tarefa. Em branco, o atendimento abre sem histórico. O método não exige o campo, mas a tarefa fica sem conversa para o atendente.
- É 1 callout com as credenciais do usuário que executa. Vale a regra de DML da seção 5: se a transação já fez `insert`/`update` (o caso normal, você acabou de criar a `Task`), use `notifyServiceDeskChangeAsync`, que enfileira um Queueable. A versão síncrona serve quando a `Task` foi criada em outra transação.
- O método não altera a `Task` e não manda mensagem no WhatsApp. Se quiser o "Fulano iniciou o atendimento" no chat, mande com `sendText`. Para encerrar, prefira `closeServiceDesk` (seção 14), que já grava o fim, avisa o Omni, reativa o bot e manda a despedida na ordem certa.

---

## 14. Encerrar um atendimento por código (`closeServiceDesk`)

Encerrar um atendimento tem quatro passos que precisam acontecer nesta ordem: gravar o fim na `Task`, avisar o Omni, reativar o bot da conexão para aquele contato e, só então, mandar a mensagem de despedida. Se a despedida sair antes de o bot ser reativado, ela conta como mensagem de atendimento e reagenda o aviso por falta de resposta, e o contato recebe "conversa encerrada por inatividade" minutos depois de já ter sido despedido. `closeServiceDesk` faz os quatro passos na sequência certa:

```apex
Id jobId = nitzap20.NitzapApi.closeServiceDesk(
    atendimento.Id,
    'Nossa conversa foi encerrada. Qualquer problema pode me chamar por aqui novamente.'
);
```

O que acontece:

1. Na sua transação: valida a `Task` (tipo `SERVICE_DESK` e `nitzap20__Connection_Number__c` preenchido), grava `nitzap20__Date_Time_End_Chat__c` e `ActivityDate` e muda o `Status` para um valor fechado da sua org (o `Completed` padrão, ou o primeiro status com `IsClosed` verdadeiro em `TaskStatus`). A `Task` já sai da chamada concluída, também para relatórios e para a linha do tempo de atividades.
2. Num Queueable, depois do commit: publica o evento `close` no Omni (o mesmo de `notifyServiceDeskChange`), reativa o bot da conexão para o contato, envia a despedida pela conexão da `Task` ao telefone do contato e completa as datas da primeira mensagem enviada e recebida a partir do resumo da conversa.

Regras:

- Pode ser chamado de Flow, trigger ou Apex que já fez DML: a parte com callout roda no Queueable. O retorno é o Id do job.
- `farewellMessage` em branco encerra sem mandar nada no WhatsApp.
- O telefone do contato vem do `WhoId`/`WhatId` da `Task` (campo `nitzap20__WhatsAppId__c`). Sem telefone, a despedida é pulada e o encerramento segue.
- Não mande a despedida por fora com `sendText` num `@future` paralelo. É exatamente a corrida que este método existe para evitar.
- `Task` de outro tipo ou sem conexão lança `NitzapApiException` antes de qualquer alteração.

---

## Tratamento de erros — resumo

| Situação | Comportamento |
|---|---|
| Entrada inválida (sem `to`, variável faltando, mix de formatos...) | `NitzapApiException` antes do callout |
| Backend recusou (conexão inativa, sem permissão, rate limit Meta) | `SendResult.success = false` + `errorMessage` |
| Falha de upload do `fileId` | `NitzapApiException` |

Exemplo de padrão recomendado:

```apex
try {
    nitzap20.NitzapApi.SendResult r = nitzap20.NitzapApi.sendText(conn, to, texto);
    if(!r.success){
        // logar/retentar: r.statusCode, r.errorMessage
    }
} catch (nitzap20.NitzapApi.NitzapApiException e) {
    // erro de uso da API: corrigir a chamada
}
```

## Limites e boas práticas

- Cada `sendBatch`/`sendMetaTemplateBatch` consome 1 callout por remetente (limite Salesforce: 100 callouts por transação). Mensagens com `fileId` consomem 2 callouts extras cada (presigned URL + upload).
- Em triggers e flows com DML, use sempre `sendBatchAsync` e `notifyServiceDeskChangeAsync`. Para encerrar atendimento, `closeServiceDesk` já cuida do DML e do callout na ordem certa.
- Cada página de `getMessages` é 1 callout. Para varrer conversas longas, prefira Queueable/Batch encadeado guardando o `sequence` — `take` alto com mídia e mensagem citada consome heap rápido.
- Templates Meta só enviam por conexão WABA/Coex e com template `APPROVED`.
- Para automações declarativas (Flow), continue usando a ação **"NITZAP 2.0: Enviar Mensagem WhatsApp"** — esta API é a superfície para código Apex.
