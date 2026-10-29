# 10. Templates do WhatsApp (modelos da Meta)

O template (na Meta, **modelo de mensagem**) é uma mensagem pronta que precisa ser aprovada pela Meta antes de ser usada. Nas conexões oficiais (**Coexistência** e **API Cloud**), ele é obrigatório para iniciar uma conversa, para retomar uma conversa em que o cliente não escreve há mais de 24 horas e para os [disparos de campanha](#nitzap/disparo-campanha).

Este guia mostra como criar o template no Gerenciador do WhatsApp da Meta, acompanhar a aprovação e enviar o template pelo Nitzap Omni.

**Como ler as imagens:** os círculos vermelhos numerados apontam para a parte da tela que está sendo explicada. O número no círculo é o mesmo da coluna **Nº** da tabela logo abaixo da imagem.

<!-- sumario:inicio -->
**Neste artigo:**

- [O que é preciso antes](#nitzap/templates/antes-de-comecar)
- [Abrir o Gerenciador do WhatsApp](#nitzap/templates/1-abrir-o-gerenciador-do-whatsapp)
- [Criar o modelo](#nitzap/templates/2-criar-o-modelo)
- [Escolher a categoria](#nitzap/templates/3-escolher-a-categoria)
- [Preencher o modelo](#nitzap/templates/4-preencher-o-modelo)
- [Acompanhar a aprovação](#nitzap/templates/5-acompanhar-a-analise)
- [Limites de envio da Meta](#nitzap/templates/limites-de-envio-da-meta)
- [Enviar o template pelo Omni](#nitzap/templates/enviar-o-template-pelo-omni)
- [Problemas comuns](#nitzap/templates/problemas-comuns)

<!-- sumario:fim -->

## Antes de começar

- **Conexão oficial.** Templates só existem nas conexões pela API oficial (Coexistência ou API Cloud). Nas conexões só QR Code, não há template da Meta. Veja [Conectar um número de WhatsApp](#nitzap/conexao-whatsapp).
- **Acesso ao portfólio empresarial na Meta** (o antigo Business Manager) em que está a conta do WhatsApp da conexão.

## Criar o template na Meta

### 1. Abrir o Gerenciador do WhatsApp

Entre em [business.facebook.com](https://business.facebook.com), abra **Configurações** e escolha o portfólio empresarial da empresa.

![Escolher o portfólio empresarial](images/template-meta-portfolio.png)

| Nº | O que é |
| :---: | --- |
| 1 | Portfólio aberto no momento. Clique para trocar. |
| 2 | O portfólio da empresa, onde está o número do WhatsApp. |

Em **Contas**, abra **Contas de mensagens**, escolha a conta do número e clique em **Gerenciador do WhatsApp**.

![Contas de mensagens no portfólio](images/template-meta-contas.png)

| Nº | O que é |
| :---: | --- |
| 1 | **Contas de mensagens.** |
| 2 | A conta do número que vai usar o template. |
| 3 | **Gerenciador do WhatsApp:** abre a tela dos modelos. |

### 2. Criar o modelo

No Gerenciador do WhatsApp, abra **Modelos de mensagem** > **Gerenciar modelos**.

![Gerenciar modelos no Gerenciador do WhatsApp](images/template-meta-gerenciar.png)

| Nº | O que é |
| :---: | --- |
| 1 | **Gerenciar modelos:** a lista de templates da conta. |
| 2 | **Criar modelo.** |
| 3 | A conta em que você está. O template vale só para os números dessa conta: confira antes de criar. |

### 3. Escolher a categoria

![Configurar o modelo: categoria e tipo](images/template-meta-categoria.png)

| Nº | O que é |
| :---: | --- |
| 1 | **Categoria** do template (tabela abaixo). |
| 2 | **Tipo** de mensagem. Para uma mensagem com texto e botões, use **Padrão**. |
| 3 | **Prévia do modelo:** um exemplo de como fica no WhatsApp. |
| 4 | **Avançar.** |

| Categoria | Para que serve |
| --- | --- |
| **Marketing** | Boas-vindas, promoções, ofertas, convites, novidades e retomada de contato. |
| **Utilidade** | Avisos sobre algo que o cliente já pediu ou contratou: pedido, pagamento, agendamento, atualização de conta. |
| **Autenticação** | Códigos de verificação e de acesso. |

A Meta confere a categoria na análise e pode mudá-la se o texto não combinar. O preço de cada mensagem também depende da categoria.

### 4. Preencher o modelo

Na etapa **Editar modelo**, preencha o nome, o idioma e o conteúdo. A prévia, à direita, mostra o resultado enquanto você digita.

![Editar o modelo: nome, conteúdo e botões](images/template-meta-editar.png)

| Nº | Campo | O que fazer |
| :---: | --- | --- |
| 1 | **Nome do modelo** | Só letras minúsculas, números e `_` (ex.: `abertura`, `lembrete_pagamento`). É o nome que aparece na lista de templates do Nitzap. |
| 2 | **Idioma** | **Portuguese (BR)** para clientes no Brasil. |
| 3 | **Tipo de variável** | **Nome** cria variáveis com nome, como `{{nome_cliente}}`. **Número** cria `{{1}}`, `{{2}}`. Com nome, fica mais fácil saber o que preencher no Nitzap. |
| 4 | **Amostra de mídia** | Opcional: imagem, vídeo ou documento no topo da mensagem. |
| 5 | **Cabeçalho** | Opcional: uma linha de título, até 60 caracteres. |
| 6 | **Corpo** | O texto da mensagem, até 1.024 caracteres. Os botões abaixo formatam o texto (negrito, itálico, tachado e código). |
| 7 | **Adicionar variável** | Insere uma variável onde está o cursor. É o que muda a cada envio, como o nome do cliente. |
| 8 | **Amostras de variáveis** | Um exemplo para cada variável (ex.: `Larissa`). Serve só para a Meta analisar e não é enviado ao cliente. Não use dados reais de clientes. |
| 9 | **Adicionar botão** | Opcional: até 10 botões. Com mais de 3, eles aparecem em uma lista. |
| 10 | **Texto do botão** | Em **Resposta rápida**, o texto que o cliente toca para responder (até 40 caracteres). |
| 11 | **Enviar para análise** | Manda o template para a Meta aprovar. |
| 12 | **Prévia do modelo** | Como a mensagem vai chegar, com as amostras no lugar das variáveis. |

Entre o corpo e os botões fica o **Rodapé**, também opcional: uma linha curta no fim da mensagem, até 60 caracteres.

**Dicas para ser aprovado:**

- Não comece nem termine o corpo com uma variável e não coloque duas variáveis seguidas.
- Escreva o texto completo, com a empresa identificada e o motivo do contato.
- Em **Marketing**, um botão de resposta rápida para sair da lista (ex.: **Não quero receber**) ajuda o cliente a pedir opt-out. Veja [Opt-out](#nitzap/disparo-campanha/opt-out-quem-nao-quer-receber).

### 5. Acompanhar a análise

Depois de enviado, o template aparece em **Gerenciar modelos** com o status **Em análise**. A Meta costuma responder em poucos minutos, mas pode levar até 24 horas.

![Lista de modelos com o template em análise](images/template-meta-lista.png)

| Nº | O que é |
| :---: | --- |
| 1 | Marque o template para ver as ações. |
| 2 | **Status** do template. |
| 3 | Ações: **Excluir**, **Copiar** (cria um template novo a partir deste), **Arquivar** e **Desarquivar**. |

| Status | O que significa |
| --- | --- |
| **Em análise** | A Meta ainda está avaliando. Ainda não aparece no Nitzap. |
| **Ativo** | Aprovado. Já aparece no Nitzap para envio. |
| **Rejeitado** | Recusado. Abra o template para ver o motivo, corrija e envie de novo. |
| **Pausado** ou **Desativado** | A Meta suspendeu o template por reclamações ou bloqueios dos clientes. Ele some do Nitzap enquanto estiver assim. |

O Nitzap mostra **só os templates aprovados**, e só os da conta do número que você está usando.

## Limites de envio da Meta

A Meta limita quantos clientes **diferentes** cada número pode procurar por template em 24 horas. Veja o seu limite em **Ferramentas da conta** > **Limites de mensagens**, no Gerenciador do WhatsApp.

![Limites de mensagens no Gerenciador do WhatsApp](images/template-meta-limites.png)

| Nº | O que é |
| :---: | --- |
| 1 | **Limite atual:** quantas conversas iniciadas pela empresa o número pode abrir em 24 horas. Os degraus são 250, 2.000, 10.000, 100.000 e Ilimitado. |
| 2 | **Como subir de degrau:** o requisito para o próximo limite e quanto já foi feito. A mudança pode levar até 24 horas. |

O limite conta só as conversas que a **empresa inicia**. Responder quem escreveu para você não entra na conta. Leve isso em conta antes de um [disparo de campanha](#nitzap/disparo-campanha) grande.

<!-- Criar o template pelo Salesforce: aguardando os prints (aba Templates Meta em Gerenciar conexão). -->

## Enviar o template pelo Omni

Quando a conversa está fechada (o cliente nunca escreveu ou não escreve há mais de 24 horas), a caixa de mensagem dá lugar a um aviso, e o único jeito de falar com o cliente é por template.

![Conversa fechada e a lista de templates da Meta](images/template-omni-fechada.png)

| Nº | O que é |
| :---: | --- |
| 1 | **Conversa fechada:** envie um template para retomar. Quando o cliente responder, a conversa reabre sozinha. |
| 2 | **Template:** abre a lista. |
| 3 | Aba **Meta:** os templates aprovados da conta deste número. |
| 4 | **Play:** abre o template para preencher e enviar. |
| 5 | **Agendar envio:** para mandar o template mais tarde. Veja [Agendar envio](#nitzap/omni/agendar-envio), no guia do Omni. |

![Preencher os parâmetros do template](images/template-omni-parametros.png)

| Nº | O que é |
| :---: | --- |
| 1 | **Visualização do Template:** como a mensagem vai chegar. |
| 2 | **Parâmetros do Template:** um campo para cada variável, com o nome usado na Meta (aqui, **nome_cliente**). Preencha todos. Se o template tiver mídia ou link dinâmico, os campos aparecem aqui também. Se não tiver variáveis, aparece **Este template não possui variáveis**. |
| 3 | **Concluir:** envia o template na hora. O Nitzap mostra **Template enviado com sucesso** ou o erro devolvido pela Meta. |

Com a conversa aberta, o botão de templates também fica na caixa de mensagem (nº 6 em [Caixa de mensagem](#nitzap/omni/caixa-de-mensagem)). Ali a aba **Meta** fica ao lado da aba **Nitzap**, que tem as mensagens prontas internas, sem aprovação da Meta.

O template enviado pelo Omni chega mesmo para quem está na lista de [opt-out](#nitzap/disparo-campanha/opt-out-quem-nao-quer-receber): o bloqueio vale só para os disparos de campanha.

## Problemas comuns

| Situação | O que fazer |
| --- | --- |
| O template não aparece no Nitzap. | Confira se o status na Meta é **Ativo** e se ele foi criado na mesma conta do número da conversa (nº 3 em [Criar o modelo](#nitzap/templates/2-criar-o-modelo)). |
| Não aparece o botão **Template** nem a aba **Meta**. | A conexão não é oficial. Templates da Meta só existem em conexões Coexistência e API Cloud. |
| O template foi rejeitado. | Abra o template na Meta para ver o motivo. Os mais comuns são categoria errada, variável no começo ou no fim do texto e conteúdo pouco claro. Corrija e envie de novo, ou use **Copiar** para criar outro. |
| Erro ao enviar pelo Omni. | O texto do erro é o motivo da Meta. Confira se todos os parâmetros foram preenchidos e se o template não foi pausado. |
| A conversa continua fechada depois do envio. | É normal: ela reabre quando o cliente responder. |
| Muitos envios falham no mesmo dia. | O número pode ter atingido o limite de conversas em 24 horas. Veja [Limites de envio da Meta](#nitzap/templates/limites-de-envio-da-meta). |
