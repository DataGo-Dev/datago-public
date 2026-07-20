# Nitzap — API Apex para Desenvolvedores

A classe `nitzap20.NitzapApi` expõe as operações do Nitzap para o seu código Apex: enviar mensagens de texto e mídia, listar templates Meta e enviar templates com variáveis — sempre informando **qual conexão (número de WhatsApp)** origina o envio.

## Pré-requisitos

- Pacote Nitzap instalado e configurado no org (backend conectado).
- O número da conexão que vai enviar (ex.: `5514981770936`). Você encontra os números conectados na tela de conexões do Nitzap, ou via Apex:

```apex
for(nitzap20.NitzapApi.ConnectionInfo c : nitzap20.NitzapApi.listConnections()){
    // c.connectionNumber, c.label, c.channel (NITZAP | WABA_COEX), c.active, c.memberCount
}
```
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

## 9. Listar conversas (`getChats`)

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
}
```

A condição vai direto para o banco do backend — monte valores com cuidado (números sem formatação, datas em UTC no formato `YYYY-MM-DD HH:MM:SS+00`). Erro de sintaxe retorna como `NitzapApiException` com a mensagem do servidor.

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
- Em triggers e flows com DML, use sempre `sendBatchAsync`.
- Templates Meta só enviam por conexão WABA/Coex e com template `APPROVED`.
- Para automações declarativas (Flow), continue usando a ação **"NITZAP 2.0: Enviar Mensagem WhatsApp"** — esta API é a superfície para código Apex.
