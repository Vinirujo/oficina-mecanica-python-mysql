# Oficina Mecânica - Python e MySQL

Projeto desenvolvido para praticar integração entre Python e MySQL, organização do código em módulos, operações CRUD e relacionamento entre tabelas utilizando chave estrangeira e `INNER JOIN`.

## Funcionalidades

### Clientes
- Cadastrar cliente
- Listar clientes
- Atualizar telefone
- Excluir cliente

### Veículos
- Cadastrar veículo
- Listar veículos
- Atualizar placa
- Excluir veículo

### Consultas
- Listar clientes junto com seus respectivos veículos utilizando `INNER JOIN`

## Tecnologias utilizadas

- Python
- MySQL
- MySQL Connector/Python
- Python Dotenv
- Git
- GitHub

## Estrutura do projeto

```text
Oficina_mecanica/
├── main.py
├── conexao.py
├── clientes.py
├── veiculos.py
├── consultas.py
├── banco.sql
├── .env.example
├── .gitignore
└── README.md
```

## Banco de dados

O projeto utiliza duas tabelas principais.

### clientes

- `id`
- `nome`
- `telefone`

### veiculos

- `id_veiculo`
- `modelo`
- `placa`
- `id_cliente`

A coluna `id_cliente` da tabela `veiculos` é uma chave estrangeira que referencia o `id` da tabela `clientes`.

O relacionamento entre as tabelas é de um para muitos:

```text
Cliente 1 ---- N Veículos
```

## Como executar

### 1. Instale as dependências

```bash
python -m pip install mysql-connector-python python-dotenv
```

### 2. Crie o banco de dados

Abra o arquivo `banco.sql` no MySQL Workbench e execute os comandos.

### 3. Configure o arquivo `.env`

Crie um arquivo `.env` seguindo o modelo disponível em `.env.example`.

Exemplo:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=oficina_mecanica
```

O arquivo `.env` não deve ser enviado para o GitHub.

### 4. Execute o programa

```bash
python main.py
```

## Conceitos praticados

- CRUD
- Funções
- Módulos Python
- Conexão Python com MySQL
- Variáveis de ambiente
- Chave primária
- Chave estrangeira
- Relacionamento 1:N
- `INNER JOIN`
- Git e GitHub

## Objetivo do projeto

Este projeto foi criado como parte dos meus estudos de desenvolvimento back-end, com o objetivo de consolidar conhecimentos de Python e banco de dados antes de avançar para estudos de APIs e REST.