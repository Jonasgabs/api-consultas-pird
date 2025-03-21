## Protocolo PIRD 


# 📌 Realiza pesquisa de produtos

Utilizando api de socket é possível realizar pesquisa de produtos pelo nome e pelo preço.

#### 📄 `README.md`
=======

Documentação do projeto com instruções de instalação e uso.


comando para rodar o cliente na raiz do projeto: python app/main.py

# Documentação do Protocolo

## Servidor

O servidor é responsável por processar requisições de clientes que interagem com a base de dados de produtos. Ele utiliza **sockets** para comunicação TCP e suporta múltiplas conexões simultâneas usando **threads**.

### Estrutura de Dados Interna
- **Objeto (`Produto`)**: Representa cada produto com os atributos `nome` e `preco`.
- **Dicionário (`dict`)**: Usado como banco de dados em memória, onde as **chaves** são os nomes dos produtos (em minúsculo) e os **valores** são instâncias da classe `Produto`.
- **Lista (`list`)**: Usada para armazenar os resultados de buscas por valor.

###  Comandos Suportados
- `SEARCH nome_produto` → Pesquisa um produto pelo nome.
- `SEARCH valor_produto` → Pesquisa todos os produtos com o valor exato informado.
- `CREATE nome_produto preco` → Cria um novo produto.
- `DELETE nome_produto` → Remove um produto pelo nome.
- `QUIT` → Encerra a conexão do cliente com o servidor.

###  Funcionalidades
- Suporte a múltiplos clientes simultâneos (via `threading`).
- Consulta de produtos por nome ou preço.
- Criação e remoção de produtos.
- Comunicação via socket TCP.
- Envio de respostas no formato:
  ```
  <STATUS_CODE>\n<JSON ou Mensagem>
  ```

### Códigos de Resposta
| Código | Significado               | Quando é Retornado                             |
|--------|---------------------------|------------------------------------------------|
| 200    | OK                        | Requisição bem-sucedida (busca, deleção).     |
| 201    | Produto criado            | Quando um produto é inserido com sucesso.     |
| 400    | Bad Request               | Requisição malformada (ex: preço inválido).   |
| 404    | Not Found                 | Produto não encontrado.                       |
| 409    | Conflict                  | Produto já existe.                            |

### ▶Execução do Servidor
Inicie o servidor com o seguinte comando (na raiz do projeto):
```bash
python -m app.servidor.servidor
```


##  Cliente

O cliente é responsável por capturar os comandos do usuário, formatar e enviar requisições ao servidor, e exibir as respostas de forma compreensível.

### Estrutura de Dados
- **Strings**: Utilizadas para compor os comandos e requisições.
- **Objeto `Cliente`**: Responsável por gerenciar conexão, envio de dados e desconexão.

### Comandos Utilizados
- `enviar_requisicao(requisicao)` → Envia a consulta (nome, valor, ou outro comando) ao servidor.
- `desconectar()` → Envia o comando `QUIT` ao servidor e encerra a conexão.

### Funcionalidades
- Interface de linha interativa com menu para facilitar uso.
- Envio de comandos de forma padronizada.
- Conexão e desconexão seguras com o servidor.
- Exibição de respostas formatadas:
  - Se for JSON: Mostra os produtos de forma organizada.
  - Se for texto: Mostra mensagem clara para o usuário.

###  Execução do Cliente
Execute a aplicação com:
```bash
python app/main.py
```
Ou especifique host e porta:
```bash
python app/main.py <host> <porta>
```

### Exemplo de Fluxo
1. O usuário executa o cliente e escolhe a opção desejada (buscar, criar, deletar).
2. O cliente monta a requisição e envia ao servidor.
3. O servidor processa e retorna o status e os dados.
4. O cliente interpreta e exibe a resposta.
5. O usuário pode continuar utilizando o sistema ou sair.

---
Essa documentação cobre toda a lógica de funcionamento da aplicação baseada em sockets e simulação de protocolo HTTP simplificado, com foco em clareza, padronização e funcionalidade em um ambiente de rede local.