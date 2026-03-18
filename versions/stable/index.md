---
layout: clean
---
# 1.409

## 📦 Instalação
Clique no link abaixo para instalar o pacote na sua organização:

👉 [**Instalar Pacote**](https://login.salesforce.com/packaging/installPackage.apexp?p0=04taj000000OwIz)

---

> [!CAUTION] 
> **ATENÇÃO:** As hierarquias do OMNI nesta versão em diante serão processadas por **conexão**. Se sua Org utiliza esta opção, siga o tutorial abaixo imediatamente após a instalação:

1. Vá até o perfil **dono da conexão** (o primeiro usuário que conectou a sessão).

2. Clique em **Conf. Sessão**.
   ![Configuração da Sessão](https://github.com/user-attachments/assets/46b91990-76df-4215-8a10-1356b7165373)

3. Vá até a aba **Configurações**.
  <img width="800"  alt="image" src="https://github.com/user-attachments/assets/5b2ecd76-9c86-4859-884f-edd8ba14b11b" />
  
4. Habilite a função **Omni: Regras de compartilhamento**.

### 👤 Usuários Prioritários
Adicionada a função para definir usuários que receberão contatos não cadastrados.
* **Comportamento:** Ao marcar esta opção, apenas os usuários prioritários receberão novos chats de Leads/Contatos não cadastrados.
* **Recomendação:** Deixe desmarcado para todos se desejar a distribuição padrão.



## 🛠️ Novidades e Melhorias

### 📄 Envio de Arquivos via Flow
Agora é possível enviar arquivos facilmente através de fluxos. Atente-se aos limites técnicos do Apex:
* **Limite:** Máximo de 50 arquivos por vez.
* **Processamento:** Enviar apenas em fluxo assíncrono.
* **Tamanho:** Máximo de 2 MB por arquivo.

![Envio via Flow](https://github.com/user-attachments/assets/d12c45e4-08db-40a0-a70b-5af403f92f23)

### 📞 Chamadas na Conversa
As chamadas recebidas agora são notificadas diretamente no componente de conversa.
![Chamadas na Conversa](https://github.com/user-attachments/assets/87e5322b-7951-452b-ac90-abf87bac86f8)

### 🏛️ Hierarquia em Histórico
A hierarquia de visibilidade agora é respeitada também no histórico das mensagens quando a função está habilitada.

### 🎨 Interface (UI)
* **Ajuste de Layout:** O tamanho dos balões de mensagem foi otimizado para **80%** do espaço livre (anteriormente era 65%), melhorando o aproveitamento de tela.

### Alteração nas opções padrão
<img width="344" height="291" alt="image" src="https://github.com/user-attachments/assets/6b67379c-92e5-4e6e-91a3-4d239f529e60" />
