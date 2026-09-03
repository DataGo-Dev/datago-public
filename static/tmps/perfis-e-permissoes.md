# Nitzap API — Perfis, credenciais e permissões

Este documento complementa a collection Postman. Ele descreve **quem pode fazer o quê** na API, para servir de referência ao avaliar controle de acesso. Qualquer comportamento observado que divirja do descrito aqui deve ser tratado como achado.

---

## 1. Tipos de credencial

| Credencial | Como é obtida | Como é enviada | Validade |
|---|---|---|---|
| **App Key** | Fornecida pelo Nitzap na implantação. Não há endpoint para criar, apenas para rotacionar. | Header `X-App-Key` | Até ser rotacionada |
| **Token de login** | `POST /whatsapp/login` com `username` + `password` | Header `Authorization: Bearer <token>` (SSE: query `?token=`) | 1 hora |
| **Token delegado** | `POST /tokens/delegated-tokens`, emitido por quem tem token de login | Header `Authorization: Bearer <token>` | Definida na emissão; revogável |
| **Token de conexão** | `POST /users/connections/token`, emitido por admin para um número específico | Header `Authorization: Bearer <token>` | 1 hora |

### Token de login
O `username` pode ser:
- **Usuário comum** ou **admin**: o token fica vinculado às conexões (números) das quais o usuário é membro.
- **Conta de integração**: o token não fica preso a um número. É a credencial de aplicativos externos.
- **Número + secret**: o próprio número de WhatsApp conectado faz login com o `secret` entregue na primeira conexão. O token fica vinculado a esse único número.

### Token delegado
Recorte de um token de login com menos poder. Carrega:
- `scopes`: um ou mais de `read`, `send`, `manage`, `connection`.
- `numbers` (opcional): subconjunto dos números do emissor ao qual o token fica restrito.

Um token delegado nunca deve conseguir mais do que quem o emitiu. Tokens delegados não acessam as rotas de `/tokens`.

### Token de conexão
Token delegado com scope `connection`, emitido por admin, usado para administrar configurações de um único número (opções de sessão, opt-in, prompts). Não envia nem lê mensagens.

---

## 2. Papéis

| Papel | Descrição |
|---|---|
| **Usuário comum** | Membro de uma ou mais conexões. Opera exclusivamente sobre os seus números. |
| **Admin** | Usuário comum com poderes de gestão: cadastra e gerencia usuários, conexões e contas de integração, cria tokens em nome de integrações, cadastra webhooks, acessa logs e rotaciona a App Key. Para enviar ou ler, continua limitado às conexões das quais é membro. |
| **Conta de integração** | Identidade de aplicativo. Pode enviar e ler por qualquer número da instância, listar sessões, gerenciar usuários e conexões e cadastrar webhooks. **Não** promove admins, não reseta secret de usuários e não cria nem apaga outras contas de integração. |
| **App Key** | Credencial de servidor. Usada no bootstrap (antes de existir o primeiro admin) e em operações de plataforma. Depois que existe um admin, `/users` deixa de aceitar App Key. |

**Regra geral:** toda rota autenticada opera apenas sobre os números do próprio chamador, salvo onde a tabela indicar "qualquer número". Um usuário comum jamais deve ler, enviar, editar, apagar ou receber eventos de um número do qual não é membro.

---

## 3. Matriz de permissões

Legenda:
- **próprios** = permitido apenas sobre os números vinculados ao token
- **qualquer** = permitido sobre qualquer número da instância
- **✅** = permitido
- **❌** = deve retornar `401`/`403`
- **scope** = token delegado permitido se tiver o scope indicado; sem indicação, token delegado não é previsto na rota

### 3.1 Público (sem credencial)

| Rota | Observação |
|---|---|
| `GET /health` | |
| `GET /config/authorized-connections` | |
| `POST /whatsapp/login` | Rate limit por usuário |
| `POST /announcements/:id/read` | Requer token de login |

### 3.2 Conexão de números

| Rota | Comum | Admin | Integração | App Key | Delegado |
|---|---|---|---|---|---|
| `GET /whatsapp/connect/:number` | ✅ | ✅ | ✅ | ✅ | ❌ |
| `GET /whatsapp/status/:sessionID` | ✅ | ✅ | ✅ | ✅ | ❌ |
| `POST /whatsapp/logout/:sessionID` | próprios | próprios | qualquer | ❌ | ❌ |
| `POST /whatsapp/unlink-connection` | próprios | próprios | qualquer | ❌ | ❌ |
| `POST /whatsapp/remove-waba-session/:sessionID` | próprios | próprios | qualquer | ❌ | ❌ |
| `GET /whatsapp/sessions` | ❌ | ❌ | ✅ | ✅ | ❌ |
| `POST /whatsapp/send-message-to-all-clients` | ❌ | ❌ | ❌ | ✅ | ❌ |
| `POST /whatsapp/disconnect-alerts/claim` | ❌ | ❌ | ❌ | ✅ | ❌ |

### 3.3 Envio

| Rota | Comum | Admin | Integração | App Key | Delegado |
|---|---|---|---|---|---|
| `POST /whatsapp/send-message` | próprios | próprios | qualquer | ❌ | scope `send` |
| `POST /whatsapp/send-multiples` | próprios | próprios | qualquer | ❌ | scope `send` |
| `POST /whatsapp/enque-multiples` | próprios | próprios | qualquer | ❌ | scope `send` |
| `POST /whatsapp/supress-message` | próprios | próprios | qualquer | ❌ | scope `send` |
| `POST /whatsapp/send-reaction` | próprios | próprios | qualquer | ❌ | scope `send` |
| `POST /whatsapp/close-agentforce-attendance` | próprios | próprios | qualquer | ❌ | scope `send` |
| `POST /whatsapp/scheduled-messages` | próprios | próprios | qualquer | ❌ | scope `send` |
| `GET /whatsapp/scheduled-messages` | próprios | próprios | qualquer | ❌ | scope `read` |
| `DELETE /whatsapp/scheduled-messages/:id` | próprios | próprios | qualquer | ❌ | scope `send` |
| `DELETE /whatsapp/delete-messages` | próprios | próprios | qualquer | ❌ | ❌ |
| `DELETE /whatsapp/revoke-message` | próprios | próprios | qualquer | ❌ | ❌ |
| `PUT /whatsapp/edit-message` | próprios | próprios | qualquer | ❌ | ❌ |

O campo `from` (ou `vFrom`) escolhe o número remetente. Para usuário comum e admin, só é aceito se for um dos seus números. Para token delegado com `numbers`, só se estiver na lista.

### 3.4 Leitura de mensagens e chats

| Rota | Comum | Admin | Integração | App Key | Delegado |
|---|---|---|---|---|---|
| `POST /whatsapp/get-messages` | próprios | próprios | qualquer | ❌ | scope `read` |
| `POST /whatsapp/get-range-messages` | próprios | próprios | qualquer | ❌ | scope `read` |
| `POST /whatsapp/get-media` | próprios | próprios | qualquer | ❌ | scope `read` |
| `POST /whatsapp/search-messages` | próprios | próprios | qualquer | ❌ | scope `read` |
| `GET /whatsapp/get-chat-metadata/:chatID` | próprios | próprios | qualquer | ❌ | scope `read` |
| `GET /whatsapp/get-chat-metadata` | próprios | próprios | qualquer | ❌ | scope `read` |
| `GET /whatsapp/list-chats-metadata` | próprios | próprios | qualquer | ❌ | scope `read` |
| `POST /whatsapp/get-chats-metadata` | próprios | próprios | qualquer | ❌ | scope `read` |
| `GET /whatsapp/get-my-chats-metadata` | próprios | próprios | qualquer | ❌ | ❌ |
| `POST /whatsapp/get-my-chats-metadata` | próprios | próprios | qualquer | ❌ | ❌ |
| `POST /whatsapp/update-chat-metadata` | próprios | próprios | qualquer | ❌ | ❌ |
| `POST /whatsapp/update-unread-chat-messages` | próprios | próprios | qualquer | ❌ | ❌ |
| `GET /whatsapp/get-who-talked` | próprios | próprios | qualquer | ❌ | ❌ |
| `POST /whatsapp/get-who-talked-recently` | próprios | próprios | qualquer | ❌ | ❌ |
| `POST /whatsapp/get-summary` | próprios | próprios | qualquer | ❌ | ❌ |
| `POST /whatsapp/get-events` | próprios | próprios | qualquer | ❌ | ❌ |
| `GET /whatsapp/my-events` | próprios | próprios | qualquer | ❌ | ❌ |
| `POST /whatsapp/get-occurrences` | próprios | próprios | qualquer | ❌ | ❌ |
| `GET /whatsapp/getprofilephoto` | próprios | próprios | qualquer | ❌ | ❌ |
| `GET /whatsapp/mygroups` | próprios | próprios | qualquer | ❌ | ❌ |
| `GET /whatsapp/mycontacts` | próprios | próprios | qualquer | ❌ | ❌ |
| `GET /whatsapp/fetch-contacts` | próprios | próprios | qualquer | ❌ | ❌ |
| `GET /whatsapp/export-contacts-csv` | próprios | próprios | qualquer | ❌ | ❌ |
| `GET /whatsapp/check-number` | ✅ | ✅ | ✅ | ❌ | ❌ |
| `POST /whatsapp/check-is-on-whatsapp` | ✅ | ✅ | ✅ | ❌ | ❌ |
| `GET /whatsapp/me` | ✅ | ✅ | ✅ | ❌ | ❌ |

### 3.5 Tempo real (SSE)

Token vai na query string: `?token=<token de login>`.

| Rota | Comum | Admin | Integração | App Key | Delegado |
|---|---|---|---|---|---|
| `GET /whatsapp/new-messages` | próprios | próprios | qualquer | ❌ | ❌ |
| `GET /whatsapp/chats-update` | próprios | próprios | qualquer | ❌ | ❌ |

### 3.6 IA e mídia

| Rota | Comum | Admin | Integração | App Key | Delegado |
|---|---|---|---|---|---|
| `POST /whatsapp/transcribe-audio` | próprios | próprios | qualquer | ❌ | ❌ |
| `POST /whatsapp/set-audio-transcription` | próprios | próprios | qualquer | ❌ | ❌ |
| `POST /whatsapp/set-message-summary` | próprios | próprios | qualquer | ❌ | ❌ |
| `POST /whatsapp/ai-summary` | próprios | próprios | qualquer | ❌ | ❌ |
| `POST /whatsapp/ai-summary-mass` | próprios | próprios | qualquer | ❌ | ❌ |
| `GET /whatsapp/ai-summary-mass/:id` | próprios | próprios | qualquer | ❌ | ❌ |
| `POST /whatsapp/ai-summary-mass/status` | próprios | próprios | qualquer | ❌ | ❌ |
| `POST /whatsapp/s3/generate-presigned-url` | ✅ | ✅ | ✅ | ❌ | ❌ |
| `POST /whatsapp/s3/sign-urls` | próprios | próprios | qualquer | ❌ | ❌ |

### 3.7 Métricas e logs

| Rota | Comum | Admin | Integração | App Key | Delegado |
|---|---|---|---|---|---|
| `POST /whatsapp/metrics/messages-by-connection` | próprios | próprios | qualquer | ❌ | scope `read` |
| `POST /whatsapp/metrics/response-time` | próprios | próprios | qualquer | ❌ | scope `read` |
| `POST /whatsapp/get-logs` | ❌ | ✅ | ❌ | ❌ | ❌ |
| `POST /whatsapp/export-logs-csv` | ❌ | ✅ | ❌ | ❌ | ❌ |
| `POST /whatsapp/chat-origins` | ❌ | ✅ | ❌ | ❌ | ❌ |
| `POST /whatsapp/chat-origins/detail` | ❌ | ✅ | ❌ | ❌ | ❌ |

### 3.8 Gestão de usuários e conexões (`/users`)

App Key só é aceita aqui enquanto **não existe nenhum admin** na instância.

| Rota | Comum | Admin | Integração | App Key (bootstrap) | Delegado |
|---|---|---|---|---|---|
| `POST /users/register` | ❌ | ✅ | ✅ | ✅ | ❌ |
| `POST /users/provision-group` | ❌ | ✅ | ✅ | ✅ | ❌ |
| `GET /users/list` | ❌ | ✅ | ✅ | ✅ | ❌ |
| `GET /users/active-count` | ❌ | ✅ | ✅ | ✅ | ❌ |
| `POST /users/active-filter` | ❌ | ✅ | ✅ | ✅ | ❌ |
| `GET /users/connections` | ❌ | ✅ | ✅ | ✅ | ❌ |
| `POST /users/connections/by-users` | ❌ | ✅ | ✅ | ✅ | ❌ |
| `POST /users/connections/context` | ❌ | ✅ | ✅ | ✅ | ❌ |
| `POST /users/connections` (adicionar membro) | ❌ | ✅ | ✅ | ✅ | ❌ |
| `POST /users/connections/remove` | ❌ | ✅ | ✅ | ✅ | ❌ |
| `POST /users/connections/remove-all` | ❌ | ✅ | ✅ | ✅ | ❌ |
| `POST /users/connections/disconnect` | ❌ | ✅ | ✅ | ✅ | ❌ |
| `POST /users/connections/label` | ❌ | ✅ | ✅ | ✅ | ❌ |
| `GET /users/connections/:number/members` | ❌ | ✅ | ✅ | ✅ | ❌ |
| `POST /users/connections/token` | ❌ | ✅ | ✅ | ✅ | ❌ |
| `POST /users/contact-threads` | ❌ | ✅ | ✅ | ✅ | ❌ |
| `POST /users/delete-member` | ❌ | ✅ | ✅ | ✅ | ❌ |
| `GET /users/integration` | ❌ | ✅ | ✅ | ✅ | ❌ |
| `POST /users/set-admin` | ❌ | ✅ | ❌ | ❌ | ❌ |
| `POST /users/reset-secret` | ❌ | ✅ | ❌ | ❌ | ❌ |
| `POST /users/integration` (criar conta de integração) | ❌ | ✅ | ❌ | ❌ | ❌ |
| `DELETE /users/integration/:username` | ❌ | ✅ | ❌ | ❌ | ❌ |

### 3.9 Tokens (`/tokens`)

Somente token de login. Token delegado não entra em nenhuma rota deste grupo.

| Rota | Comum | Admin | Integração | App Key | Delegado |
|---|---|---|---|---|---|
| `GET /tokens/scopes` | ✅ | ✅ | ✅ | ❌ | ❌ |
| `POST /tokens/delegated-tokens` | próprios | próprios | qualquer | ❌ | ❌ |
| `GET /tokens/delegated-tokens` | próprios | próprios | próprios | ❌ | ❌ |
| `DELETE /tokens/delegated-tokens/:jti` | próprios | próprios | próprios | ❌ | ❌ |
| `POST /tokens/integration-tokens/:username` | ❌ | ✅ | ❌ | ❌ | ❌ |
| `GET /tokens/integration-tokens/:username` | ❌ | ✅ | ❌ | ❌ | ❌ |
| `DELETE /tokens/integration-tokens/:username/:jti` | ❌ | ✅ | ❌ | ❌ | ❌ |

"próprios" aqui significa: o emissor só pode incluir em `numbers` números que ele próprio alcança, e só lista ou revoga tokens que ele mesmo emitiu.

### 3.10 Webhooks, agentes, prompts, tags

| Rota | Comum | Admin | Integração | App Key | Delegado |
|---|---|---|---|---|---|
| `GET /webhook/get` | ❌ | ✅ | ✅ | ❌ | ❌ |
| `POST /webhook/post` | ❌ | ✅ | ✅ | ❌ | ❌ |
| `DELETE /webhook/delete/:id` | ❌ | ✅ | ✅ | ❌ | ❌ |
| `GET /webhook/allowed-events` | ✅ | ✅ | ✅ | ❌ | ❌ |
| `POST /agent/upsert` | próprios | próprios | qualquer | ❌ | ❌ |
| `GET /agent/get` | próprios | próprios | qualquer | ❌ | ❌ |
| `DELETE /agent/delete-by-phone` | próprios | próprios | qualquer | ❌ | ❌ |
| `POST /userinfo/prompts` | próprios | próprios | qualquer | ❌ | scope `connection` |
| `GET /userinfo/prompts` | próprios | próprios | qualquer | ❌ | scope `connection` |
| `GET /userinfo/prompts/:id` | próprios | próprios | qualquer | ❌ | scope `connection` |
| `DELETE /userinfo/prompts/:id` | próprios | próprios | qualquer | ❌ | scope `connection` |
| `POST /session/upsert-options` | próprios | próprios | qualquer | ❌ | scope `connection` |
| `GET /session/get-options` | próprios | próprios | qualquer | ❌ | scope `connection` |
| `POST /session/update-opt-in` | próprios | próprios | qualquer | ❌ | scope `connection` |
| `GET /session/get-opt-in` | próprios | próprios | qualquer | ❌ | scope `connection` |
| `POST /tags/upsert` | próprios | próprios | qualquer | ❌ | ❌ |
| `GET /tags` | próprios | próprios | qualquer | ❌ | ❌ |

### 3.11 Plataforma

| Rota | Comum | Admin | Integração | App Key | Delegado |
|---|---|---|---|---|---|
| `POST /whatsapp/rotate-app-key` | ❌ | ✅ | ❌ | ❌ | ❌ |
| `POST /organization/upsert` | ❌ | ❌ | ❌ | ✅ | ❌ |
| `GET /announcements` | ❌ | ❌ | ❌ | ✅ | ❌ |
| `POST /announcements` | ❌ | ❌ | ❌ | ✅ | ❌ |
| `DELETE /announcements/:id` | ❌ | ❌ | ❌ | ✅ | ❌ |
| `POST /announcements/:id/approve` | ❌ | ❌ | ❌ | ✅ | ❌ |
| `GET /announcements/:id/reads` | ❌ | ❌ | ❌ | ✅ | ❌ |

---

## 4. Invariantes que devem valer sempre

1. Um usuário comum nunca lê, envia, edita, apaga ou recebe eventos de um número do qual não é membro.
2. Um usuário comum nunca se torna admin, nunca cria conta de integração e nunca altera o secret de outro usuário.
3. Um token delegado nunca alcança rota, número ou scope que o emissor não tinha.
4. Um token delegado revogado ou expirado é rejeitado em toda rota.
5. Uma conta de integração nunca promove admin, nunca reseta secret e nunca cria ou apaga contas de integração.
6. Depois do primeiro admin, a App Key não opera `/users`.
7. O `secret` de um número é entregue uma única vez, na primeira conexão, e nunca é recuperável pela API.
8. Um webhook cadastrado só recebe eventos dos números da instância que o cadastrou.
