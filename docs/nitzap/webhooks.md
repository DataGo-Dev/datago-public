# Webhooks do Nitzap

O webhook avisa o seu sistema, em tempo real, cada vez que algo acontece no WhatsApp conectado ao Nitzap. A cada evento marcado, o Nitzap faz um POST em JSON para a URL que você cadastrar.

Se você só quer ler mensagens dentro do Salesforce, não precisa de webhook — ele existe para levar os eventos para fora: ERP, site, automação, integração própria.

## Onde configurar

Aba **Nitzap Config → 🔗 Webhooks**, dentro do Gerenciador de Configurações do Nitzap.

- Só **administradores** do Nitzap conseguem criar, editar ou excluir webhooks.
- A **App Key** precisa estar salva na aba Configuração; sem ela a aba fica bloqueada.
- Os webhooks valem para a organização inteira, não para um usuário só.

![Formulário de cadastro de webhook](images/webhook-formulario.png)

## Campo a campo

### Ativo

Liga e desliga o webhook sem perder a configuração. Desativado, ele continua na lista mas não recebe nenhuma chamada. Use para pausar durante uma manutenção do seu servidor.

### Nome do Webhook

Serve só para você identificar a integração na lista (ex.: `ERP Produção`, `Painel BI`). Não é enviado para o seu servidor.

### URL do Endpoint

O endereço que vai receber o POST.

- Precisa ser **https**. Endereço `http` é recusado no momento de salvar.
- Precisa estar acessível pela internet (não adianta `localhost` nem IP de rede interna).
- Precisa responder com status **2xx**. Qualquer outra coisa conta como falha.

### Secret (Chave de Autenticação)

Um texto livre que você inventa. Ele vai no cabeçalho `Authorization` de toda requisição, exatamente como foi digitado (sem `Bearer`, sem assinatura).

O seu servidor deve comparar esse cabeçalho com o valor esperado e recusar o que não bater — é o que impede alguém de descobrir a sua URL e mandar eventos falsos.

### Eventos

Marque o que o seu servidor precisa receber. **Sem nenhum evento marcado, nada é enviado.**

| Evento na tela | Chave no JSON | Quando dispara |
| --- | --- | --- |
| Quando Envia e Recebe mensagem | `ON_MESSAGE` | Toda mensagem individual, enviada ou recebida (texto, mídia, áudio, documento). |
| Quando Envia e Recebe mensagem em grupo | `ON_GROUP_MESSAGE` | Mesma coisa, só que em conversas de grupo. |
| Quando há alteração na mensagem (leitura, edição, etc) | `MESSAGE_UPDATE` | Mudança em mensagem que já existe: leitura, edição, exclusão, presença no chat. O campo `update_type` diz qual foi (`READ_DATE`, `FAILED`, entre outros). |
| Quando uma mensagem falha ao ser entregue | `ON_ERROR` | Mensagem recusada ou não entregue no canal oficial (Meta). O motivo vem em `error`. |
| Quando um botão de ação é clicado (Meta) | `BUTTON_CLICK` | Clique em botão de template ou mensagem interativa do canal oficial. |
| Quando há alteração na conexão | `CONNECTION_UPDATE` | Reservado para mudança de status da conexão (conectou, caiu). **Ainda não gera chamada** — marcar não quebra nada, só não chega nada por enquanto. |

### Usuários Rastreados

Este é o campo que mais confunde: os números aqui são os **números das conexões do Nitzap** (a linha de WhatsApp conectada), **não** os números dos contatos que conversam com você.

- Um número por linha, só dígitos, com DDI e DDD: `5511999999999`.
- **Digite `ALL` para receber os eventos de todas as conexões da organização** — inclusive as que forem conectadas depois. É o jeito mais simples de não esquecer nenhuma linha.
- **Lista vazia não recebe nada.** Cadastrar o webhook e deixar este campo em branco é o motivo mais comum de "configurei e não chega nada".
- `ALL` não diferencia maiúscula de minúscula, e pode ser a única linha do campo.

## Como a chamada chega no seu servidor

```
POST https://seu-servidor.com/webhook
Content-Type: application/json
Authorization: <o secret que você cadastrou>
```

```json
{
  "username": "5511999999999",
  "event_type": "ON_MESSAGE",
  "payload": {
    "msgkey": "3EB0C767D26B8A1E2C",
    "chatid": "5521888888888",
    "mywhatsid": "5511999999999",
    "sender": "5521888888888",
    "text": "Bom dia, consegue me passar o orçamento?",
    "type": "text",
    "isent": false,
    "isgroup": false,
    "channel": "NITZAP",
    "pushname": "Maria Souza",
    "message_timestamp": 1758800000,
    "sessionid": "..."
  }
}
```

- `username`: o número da conexão que gerou o evento — é este valor que o campo **Usuários Rastreados** filtra.
- `event_type`: a chave da tabela de eventos acima.
- `payload`: o conteúdo do evento. Em eventos de mensagem, é a própria mensagem; os campos variam conforme o tipo (mídia traz `url` e `mimetype`, atualização traz `isupdate` e `update_type`, falha traz `error`).
- `isent`: `true` quando a mensagem saiu da sua conexão, `false` quando foi recebida.

### Entrega e novas tentativas

- Tempo limite de **15 segundos** por tentativa.
- Até **3 tentativas**, com espera de 1s, 2s e 4s entre elas.
- Só status **2xx** encerra a entrega; depois da terceira falha o evento é descartado (fica registrado no log do Nitzap).
- Responda rápido, com `200`, e processe depois. Se o seu endpoint demorar para responder, o Nitzap vai reenviar o mesmo evento — trate repetição usando o `msgkey` como chave de idempotência.

## Exemplo de validação do secret

```js
app.post('/webhook', (req, res) => {
  const secretRecebido = req.header('Authorization');
  const secretEsperado = process.env.NITZAP_WEBHOOK_SECRET;

  if (secretRecebido !== secretEsperado) {
    return res.sendStatus(401);
  }

  res.sendStatus(200);
  processarEventoEmSegundoPlano(req.body);
});
```

## Não está chegando nada?

1. O campo **Usuários Rastreados** está preenchido? Vazio não entrega nada — use `ALL` ou o número da conexão.
2. O número digitado é o **da conexão**, com DDI e DDD, só dígitos?
3. Algum **evento** está marcado?
4. O webhook está com **Ativo = Sim**?
5. A URL é **https**, pública, e responde `200` em menos de 15 segundos?
6. O seu servidor está recusando por causa do `Authorization`? Confira se o secret é idêntico ao cadastrado.
