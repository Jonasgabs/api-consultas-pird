## repo para o versionamento da api - projeto de redes

# 📌 API de Consultas Básicas

Esta é uma API de consultas básicas desenvolvida em **Python** utilizando **FastAPI**. O projeto inclui um sistema de gerenciamento de consultas com um banco de dados **SQLite**.

## 🚀 Tecnologias Utilizadas
- Python 3
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite

## 📁 Estrutura do Projeto
O diretório do projeto está organizado da seguinte maneira:

```
minha_api/
│── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── routes/
│   │   ├── consulta.py
│   └── __init__.py
├── .env
├── requirements.txt
├── README.md
```

### 📌 Descrição dos Arquivos

#### 📂 `app/`
Diretório principal onde está a lógica da API.

- **`main.py`**: Arquivo principal da API, responsável por inicializar o FastAPI e incluir as rotas.
- **`models.py`**: Define os modelos do banco de dados usando SQLAlchemy.
- **`schemas.py`**: Define os schemas de validação com Pydantic.
- **`database.py`**: Configuração do banco de dados e conexão com SQLAlchemy.
- **`routes/consulta.py`**: Contém as rotas para criar, listar e obter consultas.
- **`__init__.py`**: Arquivo necessário para transformar `app/` em um módulo Python.

#### 📂 `routes/`
Subdiretório contendo os módulos de rotas da API.

- **`consulta.py`**: Define os endpoints para criar e buscar consultas no banco de dados.

#### 📄 `.env`
Arquivo para armazenar variáveis de ambiente, como credenciais do banco de dados.

#### 📄 `requirements.txt`
Lista das dependências do projeto. Para instalá-las, use:
```bash
pip install -r requirements.txt
```

#### 📄 `README.md`
Documentação do projeto com instruções de instalação e uso.

---
