---
layout: clean
---
# 1.494
- 2 Junho 2026

## 📦 Instalação
Clique no link abaixo para instalar o pacote na sua organização:

👉 [**Instalar Pacote**](https://login.salesforce.com/packaging/installPackage.apexp?p0=04tN50000003pyrIAA)
---

## Aba de evetos agora mais completa 
<img width="1420" height="540" alt="image" src="https://github.com/user-attachments/assets/a82ad039-edbe-4256-b47e-65f5eb82d53a" />

## Hierarquia omni mais inteligente
Agora quando regras são habitadas no omni, você poderá receber mensagem de alguém que já está cadastrado dentro da org e pertence ao outro usuário desde que use número diferente do proprietário

## Reprodução de aúdios em seguida automático
Agora audios seguidos reproduzem automaticamente

Também ao reproduzir 1 áudio, outros param de reproduzir

## Link MCP Por user e tbm em credenciais master
<img width="1258" height="341" alt="image" src="https://github.com/user-attachments/assets/c07b54d4-705e-4e05-8cd9-a3d4b76e6784" />

## Variáveis automáticas
Agora ao abrir um template meta, se a variável tiver nome {{nome_cliente}} ele pega o nome da pessoa automaticamente.
Outras variáveis ficam salvas em cache para futuros usos

<img width="1275" height="558" alt="image" src="https://github.com/user-attachments/assets/3a1c8e64-5d61-4c85-9352-699a4c71bb00" />


## pequenas mudanças
- Quando transfere atendimento para outro número, agora a mensagem vai para esse outro número
- Ao fechar atendimento, ele seta automaticamente  em TASK:
   Nitzap: Hora Primeira Mensagem Recebida	nitzap20__DateTime_First_Message_Received__c	
    Nitzap: Hora Primeira Mensagem Enviada	nitzap20__DateTime_First_Message_Sent__c
Obs: Nativamente será feito uma varredura disso automaticamente a cada meia hora para tasks abertas

### Correções
- Corrigido bugs relacionado a criação e transferencia de atendimentos de Contas
- Sussuro agora não conta como mensagem enviada no omni
