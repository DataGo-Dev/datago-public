# Nitzap — API Apex para Desenvolvedores

A classe `nitzap20.NitzapApi` expõe as operações do Nitzap para o seu código Apex: enviar mensagens de texto e mídia, listar templates Meta e enviar templates com variáveis — sempre informando **qual conexão (número de WhatsApp)** origina o envio.

## Pré-requisitos

- Pacote Nitzap instalado e configurado no org (backend conectado).
- O número da conexão que vai enviar (ex.: `5514981770936`). Você encontra os números conectados na tela de conexões do Nitzap, ou via `nitzap20.Connect.listConnections()`.
- Recursos Meta (templates) exigem que a conexão seja um canal WABA/Coex.

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

**Lote de templates:**

```apex
nitzap20.NitzapApi.sendMetaTemplateBatch(listaDeTemplateMessages);
```

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
