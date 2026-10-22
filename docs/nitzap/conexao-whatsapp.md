# Conectar um número de WhatsApp ao Nitzap

Cada número de WhatsApp usado no Nitzap é uma **conexão**. Você pode conectar um número de duas formas: lendo um **QR Code** com o celular (WhatsApp Web) ou pela **API oficial da Meta**, entrando com o Facebook. Este guia mostra as duas, de onde começar e o que fazer depois que o número aparece na lista.

## Qual forma escolher

| Forma | Como funciona | Indicada para |
| --- | --- | --- |
| **WhatsApp (QR)** | O Nitzap entra como um aparelho conectado ao seu WhatsApp, como o WhatsApp Web. | Começar rápido com um número que já está no celular. |
| **WhatsApp Business: API Coex (Coexistência)** | API oficial da Meta ligada a um número que **continua ativo no app WhatsApp Business**. As mensagens aparecem no celular e no Nitzap ao mesmo tempo. | Empresas que já atendem pelo celular e não querem perder o número, os contatos nem o histórico. |
| **WhatsApp Business: API Cloud (só API oficial)** | O número funciona só pela API oficial e **deixa de existir no celular**. Se ele estiver ativo no WhatsApp ou no WhatsApp Business, a conta precisa ser excluída no app antes. | Números novos ou dedicados a atendimento em escala, automação e vários atendentes. |

Os templates aprovados na Meta e os disparos de campanha só funcionam nas conexões oficiais (Coex ou Cloud).

## Por onde começar

As duas formas de conexão abrem a mesma janela, **Adicionar conexão**. O ponto de partida depende do seu acesso.

### Se você administra o Nitzap: Nitzap Config

1. Clique na sua foto, no canto superior direito do Salesforce, e depois no seu nome para abrir o perfil.

   ![Menu do usuário com o link para o perfil](images/conexao-menu-perfil.png)

2. No perfil, abra a aba **Nitzap Config** e depois **Conexões**.

   ![Perfil do usuário com a aba Nitzap Config](images/conexao-perfil-nitzap-config.png)

3. Clique em **Adicionar conexão**. O contador ao lado mostra quantas conexões a organização já usa do limite contratado.

   ![Conexões WhatsApp e o botão Adicionar conexão](images/conexao-nitzap-config.png)

Uma conexão criada pelo Nitzap Config começa **sem membros**. Depois de conectar, adicione quem vai atender por ela (veja [Depois de conectar](#nitzap/conexao-whatsapp/depois-de-conectar-nome-e-membros)).

### Se você não administra: Nitzap Connect

1. Clique na sua foto, no canto superior direito, e depois no seu nome para abrir o perfil.
2. No cartão **Nitzap Connect**, clique em **Conectar meu WhatsApp**.

   ![Cartão Nitzap Connect no perfil do usuário](images/conexao-nitzap-connect.png)

Quando a conexão termina, **você entra automaticamente como membro** dela e o número passa a aparecer no cartão, em **Conexões que você participa**.

Se o cartão mostrar **"Você ainda não tem um login no Nitzap"**, clique antes em **Criar login no Nitzap**. Só o próprio usuário consegue criar o seu login e conectar o seu WhatsApp. No perfil de outra pessoa, o botão não aparece.

## Escolher o tipo de conexão

A janela **Adicionar conexão** pergunta como você quer conectar o número.

![Escolha entre WhatsApp (QR) e WhatsApp Business](images/conexao-tipo.png)

- **WhatsApp (QR):** siga a seção [Conectar via QR Code](#nitzap/conexao-whatsapp/conectar-via-qr-code).
- **WhatsApp Business:** siga a seção [Conectar pela API oficial (Coexistência)](#nitzap/conexao-whatsapp/conectar-pela-api-oficial-coexistencia).

## Conectar via QR Code

1. Em **Escolha como conectar**, deixe **QR Code** selecionado e clique em **Gerar conexão**.

   ![Opção QR Code selecionada](images/conexao-qr-code.png)

2. O QR Code aparece na tela. No celular, abra o WhatsApp e vá em **Aparelhos conectados** > **Conectar aparelho**.
3. Aponte a câmera do celular para o QR Code da tela.
4. Aguarde a mensagem **Conectado!**. A janela fecha sozinha e o número aparece na lista de conexões.

### Sem câmera: conectar com código

Se não der para ler o QR Code, use um código de pareamento:

1. Selecione **Código**.
2. Em **Número com DDI**, digite o número completo, só com dígitos: DDI + DDD + número (exemplo: `5511999999999`).
3. Clique em **Gerar conexão**. O Nitzap mostra um código.
4. No celular, abra o WhatsApp, vá em **Aparelhos conectados** > **Conectar aparelho** e escolha **Conectar com número de telefone**.
5. Digite o código que aparece no Nitzap.

![Opção Código com o número com DDI](images/conexao-qr-codigo.png)

O Nitzap espera a leitura por até 10 minutos. Se passar disso, aparece **"Tempo esgotado aguardando a conexão"**: clique em **Gerar conexão** de novo para gerar um novo QR Code ou código.

## Conectar pela API oficial (Coexistência)

A conexão oficial é feita em uma janela do Facebook, na sua conta da Meta. Tenha à mão:

- O login do **Facebook** de quem administra o portfólio empresarial (Business Manager) da empresa.
- O **celular com o app WhatsApp Business** do número, que vai receber uma mensagem para confirmar a conexão.

### 1. Escolher Coexistência e entrar com o Facebook

Em **Como este número é usado hoje?**, deixe selecionado **API Coex (Coexistência)** e clique em **Entrar com Facebook**.

![Opção API Coex (Coexistência)](images/conexao-waba-coex.png)

Abre uma janela **Conectando ao WhatsApp Business**. Mantenha essa janela aberta: ela fecha sozinha no final.

![Janela Conectando ao WhatsApp Business](images/conexao-facebook-janela.png)

Se o navegador bloquear o pop-up do Facebook, libere pop-ups para o site (no Chrome, clique no ícone de pop-up bloqueado na barra de endereço e escolha **Sempre permitir**) e clique no link do facebook na parte superior.

![Aviso de pop-up bloqueado no navegador](images/conexao-facebook-popup-bloqueado.png)

### 2. Seguir os passos no Facebook

1. Na tela **Conecte sua conta facilmente a Datago Tecnologia**, clique em **Continuar**.

   ![Início do cadastro no Facebook](images/conexao-facebook-inicio.png)

2. Em **Adicione seu número de telefone do WhatsApp**, informe o número que está no app WhatsApp Business, escolha como receber a verificação (**SMS** ou **Ligação telefônica**) e clique em **Avançar**.

   ![Número de telefone do WhatsApp](images/conexao-facebook-numero.png)

3. Em **Verifique os detalhes da sua conta**, confira o nome e a foto do perfil comercial e clique em **Avançar**. Se algo estiver errado, volte e corrija o número.

   ![Detalhes da conta do WhatsApp Business](images/conexao-facebook-detalhes.png)

4. Em **Portfólio empresarial**, escolha o portfólio (Business Manager) da empresa e clique em **Avançar**.

   ![Seleção do portfólio empresarial](images/conexao-facebook-portfolio.png)

5. A tela **Importar contatos e histórico de conversas** mostra um QR Code para ler com o app WhatsApp Business. Deixe essa tela aberta e pegue o celular: o botão **Avançar** só é liberado depois que você confirmar no celular.

   ![QR Code do Facebook para ler com o app WhatsApp Business](images/conexao-facebook-qr-code.png)

### 3. Confirmar no celular

Ao mesmo tempo em que o QR Code aparece no Facebook, o WhatsApp Business do celular recebe uma mensagem da conta oficial do **Facebook Business**: *Connect to the Business Platform*. Você pode seguir por essa mensagem ou ler o QR Code com o app. Os dois caminhos levam às mesmas telas.

1. Abra a mensagem e toque em **Connect**. Se a mensagem não chegar, no app WhatsApp Business vá em **Configurações** > **Conta** > **Plataforma comercial** e leia o QR Code da tela do Facebook.

   ![Mensagem do Facebook Business no WhatsApp](images/conexao-celular-mensagem.jpeg)

2. Na tela **Conectar à Plataforma comercial**, toque em **Conectar à Plataforma comercial**.

   ![Tela Conectar à Plataforma comercial](images/conexao-celular-plataforma-comercial.jpeg)

3. Escolha se quer trazer o histórico e toque em **Confirmar**:
   - **Compartilhar todas as conversas:** traz até 6 meses de histórico das conversas individuais. Histórico de grupos não é compartilhado.
   - **Não compartilhar conversas:** as conversas começam do zero na plataforma.

   ![Escolha de compartilhar o histórico de conversas](images/conexao-celular-historico.jpeg)

4. Aguarde. A conexão pode levar até 45 segundos.

   ![Conectando a conta no celular](images/conexao-celular-conectando.jpeg)

5. Quando aparecer **Sua conta está conectada à empresa Datago Tecnologia**, toque em **OK**.

   ![Conta conectada à Datago Tecnologia no celular](images/conexao-celular-conectado.jpeg)

Para manter a coexistência ativa, **abra o app WhatsApp Business no celular pelo menos uma vez a cada 14 dias**. A conexão pode ser gerenciada no app em **Configurações** > **Conta** > **Plataforma comercial**.

### 4. Concluir no Facebook

Volte para a janela do Facebook no computador e clique em **Avançar** na tela do QR Code.

1. Em **Confirme ou edite sua conta do WhatsApp Business**, confira o **nome da conta** e o **fuso horário** e clique em **Avançar**.

   ![Nome da conta do WhatsApp Business e fuso horário](images/conexao-facebook-conta-waba.png)

2. Em **Reveja o que você vai compartilhar com Datago API**, confira a empresa, a conta do WhatsApp e as permissões e clique em **Confirmar**.

   ![Permissões solicitadas pela Datago API](images/conexao-facebook-permissoes.png)

3. Na tela **Sua conta está conectada a Datago Tecnologia**, clique em **Concluir**. A forma de pagamento da Meta pode ser cadastrada depois.

   ![Conta conectada à Datago Tecnologia no Facebook](images/conexao-facebook-concluido.png)

Aguarde a janela do Facebook fechar e o número aparece na lista de conexões com a etiqueta **Coex (Meta)**.

### API Cloud (só API oficial)

O caminho é o mesmo: selecione **API Cloud (só API oficial)** e clique em **Entrar com Facebook**. A diferença é que não existe a etapa no celular, porque é uma conexão apenas oficial sem utilizar o número no app de whatsapp. Antes de começar, confira se o número **não está ativo** no WhatsApp nem no WhatsApp Business. Se estiver, exclua a conta no app primeiro.

![Opção API Cloud (só API oficial)](images/conexao-waba-cloud.png)

## Depois de conectar: nome e membros

A conexão nova aparece em **Nitzap Config** > **Conexões**, identificada pelo número.

![Lista de conexões com a conexão nova](images/conexao-lista.png)

Clique na engrenagem (⚙) da conexão para abrir **Gerenciar conexão**.

### Dar um nome à conexão

Em **Nome da conexão**, digite um nome fácil de reconhecer (por exemplo, o setor ou a pessoa que usa o número) e clique em **Salvar nome**. Esse nome aparece no lugar do número nas listas do Nitzap.

### Adicionar membros

Os membros são os usuários do Salesforce que atendem por essa conexão.

1. Na aba **Membros**, em **Adicionar usuário**, busque o usuário pelo nome.
2. Clique em **Adicionar**.

![Gerenciar conexão: nome e busca de usuário](images/conexao-gerenciar-membros.png)

O usuário aparece na lista de membros. Repita para cada pessoa que vai usar o número.

![Membro adicionado à conexão](images/conexao-membro-adicionado.png)

### Outros pontos da tela Gerenciar conexão

- **Canal de envio vinculado (Api WEB Nitzap):** em uma conexão oficial, você pode conectar o mesmo número também via QR, em **Conectar canal de envio (QR)**, usando o mesmo celular. Assim, as mensagens do chat saem sem custo da Meta. Templates e o primeiro contato continuam pela API oficial. O uso do canal não oficial é de responsabilidade do cliente.
- **Reconectar:** abre de novo a janela de conexão para refazer a ligação do número, por exemplo quando ele cai ou o celular é trocado.
- As abas **Configurações**, **Etiquetas**, **Prompts IA** e **Templates Meta** têm os demais ajustes da conexão.

## Problemas comuns

| Mensagem ou situação | O que fazer |
| --- | --- |
| O navegador bloqueou a janela de login. | Libere pop-ups para o site e clique em **Entrar com Facebook** de novo. |
| Tempo esgotado aguardando a conexão. | O QR Code ou o código expirou. Clique em **Gerar conexão** para gerar outro. |
| Tempo esgotado aguardando o login do Facebook. | A janela do Facebook ficou aberta sem terminar. Feche-a e recomece em **Entrar com Facebook**. |
| A mensagem do Facebook Business não chegou no celular. | Confira se o número informado no Facebook é o mesmo do app WhatsApp Business e se o app está atualizado. |
| O número conectado não aparece no chat de um usuário. | O usuário não é membro da conexão. Adicione-o em **Gerenciar conexão** > **Membros**. |
| A coexistência caiu depois de alguns dias. | O app WhatsApp Business ficou mais de 14 dias sem ser aberto. Abra o app e use **Reconectar** se precisar. |
