## API de Rotas de Viagens 

Este repositório contém uma API construída com Flask para gerenciar viagens, links, participantes e atividades. Abaixo, você encontrará uma descrição detalhada de cada rota, suas funcionalidades e como acessá-las.

### Instalação

Para rodar o projeto, você precisa de:

- Python 3.8+
- Flask

Instale as dependências usando:

```bash
python -m venv venv
venv\Scripts\Activate (Se você estiver usando o windows)
pip install -r requirements.txt

Crie um banco de dados, crie um arquivo chamado: storage.db, ou então link com o banco de dados de sua preferência, as configurações de banco estão em: src/models/settings/db_connection_hander.py

No arquivo init/schema.sql tem todas as informações sobre as tabelas e os script que você precisa rodar no banco de dados, utilize um software como DBeaver para trabalhar melhor com as tabelas SQL.

execute o python create_email.py para criar um email na plataforma que irá enviar os emails para os destinatários, e em drivers/email_sender troque o "user" e "password" pelas adquiridas
site: ethereal.email
```

### Rodando a Aplicação

Para iniciar a aplicação, execute:

```bash
python run.py
```

## Rotas

### 1. Criar Viagem
**Endpoint:** `/trips`  
**Método:** `POST`  
**Descrição:** Cria uma nova viagem.  
**Corpo da Requisição:**  
```json
{
  "nome": "Viagem de Férias",
  "destino": "Paris",
  "data_inicio": "2024-08-01",
  "data_fim": "2024-08-15"
}
```
**Resposta:**  
```json
{
  "id": 1,
  "mensagem": "Viagem criada com sucesso."
}
```

### 2. Buscar Viagem por ID
**Endpoint:** `/trips/<tripId>`  
**Método:** `GET`  
**Descrição:** Busca os detalhes de uma viagem pelo seu ID.  
**Resposta:**  
```json
{
  "id": 1,
  "nome": "Viagem de Férias",
  "destino": "Paris",
  "data_inicio": "2024-08-01",
  "data_fim": "2024-08-15"
}
```

### 3. Confirmar Viagem
**Endpoint:** `/trips/<tripId>/confirm`  
**Método:** `GET`  
**Descrição:** Confirma uma viagem pelo seu ID.  
**Resposta:**  
```json
{
  "mensagem": "Viagem confirmada com sucesso."
}
```

### 4. Criar Link para Viagem
**Endpoint:** `/trips/<tripId>/links`  
**Método:** `POST`  
**Descrição:** Cria um novo link associado a uma viagem.  
**Corpo da Requisição:**  
```json
{
  "link": "http://exemplo.com"
}
```
**Resposta:**  
```json
{
  "id": 1,
  "mensagem": "Link criado com sucesso."
}
```

### 5. Buscar Links da Viagem
**Endpoint:** `/trips/<tripId>/links`  
**Método:** `GET`  
**Descrição:** Busca os links associados a uma viagem pelo seu ID.  
**Resposta:**  
```json
[
  {
    "id": 1,
    "link": "http://exemplo.com"
  }
]
```

### 6. Convidar Participantes para a Viagem
**Endpoint:** `/trips/<tripId>/invites`  
**Método:** `POST`  
**Descrição:** Convida novos participantes para a viagem.  
**Corpo da Requisição:**  
```json
{
  "email": "participante@exemplo.com"
}
```
**Resposta:**  
```json
{
  "id": 1,
  "mensagem": "Convite enviado com sucesso."
}
```

### 7. Criar Atividade na Viagem
**Endpoint:** `/trips/<tripId>/activities`  
**Método:** `POST`  
**Descrição:** Cria uma nova atividade associada a uma viagem.  
**Corpo da Requisição:**  
```json
{
  "atividade": "Visitar a Torre Eiffel"
}
```
**Resposta:**  
```json
{
  "id": 1,
  "mensagem": "Atividade criada com sucesso."
}
```

### 8. Buscar Participantes da Viagem
**Endpoint:** `/trips/<tripId>/participants`  
**Método:** `GET`  
**Descrição:** Busca os participantes de uma viagem pelo seu ID.  
**Resposta:**  
```json
[
  {
    "id": 1,
    "email": "participante@exemplo.com"
  }
]
```

### 9. Buscar Atividades da Viagem
**Endpoint:** `/trips/<tripId>/activities`  
**Método:** `GET`  
**Descrição:** Busca as atividades associadas a uma viagem pelo seu ID.  
**Resposta:**  
```json
[
  {
    "id": 1,
    "atividade": "Visitar a Torre Eiffel"
  }
]
```

### 10. Confirmar Participante
**Endpoint:** `/participants/<participantId>/confirm`  
**Método:** `PATCH`  
**Descrição:** Confirma a participação de um participante na viagem.  
**Resposta:**  
```json
{
  "mensagem": "Participação confirmada com sucesso."
}
```

## Contribuição

Para contribuir com o projeto, siga estas etapas:

1. Faça um fork deste repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto>/<local>`
5. Crie a solicitação de pull.

