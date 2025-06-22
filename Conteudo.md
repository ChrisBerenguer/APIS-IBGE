# APIs com Python

Elementos básicos do Langchain: 1) Models; 2)Prompt Templates; 3)Output Parsers

Models = Modelo de Linguagem
Prompt Templates = 'Esqueleto' é o prompt
Output Parsers = Comunicação/Saída da comunicação

| Método | Descrição | Equivalente em BD (CRUD) |
| --- | --- | --- |
| GET | Pegar um dado | Ler (Read) |
| POST | Criar um dado novo | Criar (Create) |
| PUT | Atualizar um dado (Cadastro inteiro) | Atualizar (Update) |
| PATCH | Atualizar um dado parcialmente | Atualizar (Update) |
| DELETE | Deletar um dado | Deletar (Delete) |

### **Status 1xx: Informativo**

- **100 Continue**: O servidor recebeu o cabeçalho da requisição e o cliente deve continuar com o corpo da requisição.
- **101 Switching Protocols**: O servidor está mudando os protocolos conforme solicitado pelo cliente.

### **Status 2xx: Sucesso**

- **200 OK**: A requisição foi bem-sucedida.
- **201 Created**: A requisição foi bem-sucedida e um novo recurso foi criado.
- **204 No Content**: A requisição foi bem-sucedida, mas não há conteúdo para retornar.

### Status 3xx: Redirecionamento

- **301 Moved Permanently**: O recurso solicitado foi movido permanentemente para uma nova URL.
- **302 Found**: O recurso solicitado foi encontrado, mas em uma URL diferente temporariamente.
- **304 Not Modified**: O recurso não foi modificado desde a última requisição.

### Status 4xx: Erro do Cliente

- **400 Bad Request**: A requisição é inválida ou malformada.
- **401 Unauthorized**: Autenticação é necessária e falhou ou não foi fornecida.
- **403 Forbidden**: O servidor entendeu a requisição, mas se recusa a autorizá-la.
- **404 Not Found**: O recurso solicitado não foi encontrado.
- **405 Method Not Allowed**: O método HTTP usado não é permitido para o recurso.
- **429 Too Many Requests**: O cliente enviou muitas requisições em um curto período de tempo.

### Status 5xx: Erro do Servidor

- **500 Internal Server Error**: O servidor encontrou uma condição inesperada que impediu a execução da requisição.
- **501 Not Implemented**: O servidor não suporta a funcionalidade necessária para atender à requisição.
- **502 Bad Gateway**: O servidor, ao atuar como gateway ou proxy, recebeu uma resposta inválida do servidor upstream.
- **503 Service Unavailable**: O servidor não está disponível para processar a requisição no momento (por exemplo, devido à manutenção).
- **504 Gateway Timeout**: O servidor, ao atuar como gateway ou proxy, não recebeu uma resposta a tempo do servidor upstream.

# API REST

- *Representation State Transfer* (Transferencia de Estado Representacional)
- Protocolo (http) **Cliente → Servidor**
- **Stateless** → Toda a requisição precisa ter todas as informações necessárias (o servidor não guarda estado)
- Recursos identificados por IDs únicos (URIs - *Uniform Resource Identify*)

![image.png](image.png)

| Conceito | Explicação |
| --- | --- |
| **Requisições HTTP** | Toda interação é feita por meio de métodos HTTP como: `GET`, `POST`, `PUT`, `DELETE`. |
| **Recursos** | Tudo é tratado como um recurso. Exemplo: `/usuarios`, `/produtos`. |
| **URL bem definida** | A URL representa a localização de um recurso. Exemplo: `/usuarios/10` representa o usuário de ID 10. |
| **Stateless** | O servidor **não guarda o estado da sessão** entre as requisições. Cada requisição traz todas as informações necessárias. |
| **Formato de resposta** | Normalmente o servidor devolve os dados no formato **JSON** (às vezes XML). |