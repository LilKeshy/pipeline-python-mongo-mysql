# ETL Pipeline - MongoDB → CSV → MySQL

## 🎯 Objetivo

O objetivo deste pipeline é **integrar dados de diferentes fontes**, realizando extração, transformação e carga (ETL) de dados de produtos e livros. O processo:

✅ Extrai dados do MongoDB Atlas  
✅ Transforma e limpa os dados em CSVs  
✅ Carrega as informações no banco de dados MySQL

Esse fluxo facilita análises, relatórios e integrações com sistemas que utilizam dados estruturados.

---

## 📦 Visão Geral do Projeto

Este projeto implementa um pipeline ETL (Extract, Transform, Load) para dados de produtos e livros. O fluxo percorre as seguintes etapas:

✅ **Extract**
- Dados extraídos de uma coleção MongoDB Atlas
- Armazenados em arquivos CSV

✅ **Transform**
- Dados limpos e transformados
- Padronização de nomes de colunas
- Conversão de tipos de dados

✅ **Load**
- Dados carregados em tabelas do MySQL

---

## 🗂️ Estrutura do Projeto

```
.
├── extract_and_save_data.py
├── transform_data.py
├── save_data_mysql.py
├── extract_and_save_data.ipynb
├── transform_data.ipynb
├── save_data_mysql.ipynb
├── data/
│   ├── tabela_livros.csv
│   ├── tabela_livros_transformada.csv
│   ├── tabela_2021_em_diante.csv
├── requirements.txt
├── README.md
```

---

## ⚙️ Como Funciona

### 1. Extração - MongoDB

Arquivo: `extract_and_save_data.py`

- Conecta ao MongoDB Atlas via URI
- Lê dados de uma collection
- Salva o resultado em CSV

---

### 2. Transformação - CSV

Arquivo: `transform_data.py`

- Carrega CSV
- Realiza transformações nos dados
- Exemplo incluído: cria coluna `nova_coluna`
- Salva novo CSV transformado

---

### 3. Carga - MySQL

Arquivo: `save_data_mysql.py`

- Lê CSV
- Corrige nomes de colunas
- Converte datas
- Insere dados dinamicamente em tabelas MySQL:
  - `tb_produtos_2021_em_diante`
  - `tb_Livros`

---

## 📊 Dados Usados

### `tabela_2021_em_diante.csv`

- Contém dados de produtos a partir de 2021
- Campos como:
  - Produto
  - Categoria do Produto
  - Preço
  - Frete
  - Data da Compra
  - etc.

---

### `tabela_livros.csv`

- Contém dados específicos de livros

---

### `tabela_livros_transformada.csv`

- Versão transformada do CSV de livros
- Inclui coluna adicional `nova_coluna`

---

## ▶️ Como Executar

### Pré-requisitos

- Python 3.10+
- Banco de dados MySQL
- MongoDB Atlas (se for extrair dados reais)

### 1. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 2. Configure Variáveis de Ambiente

Crie um arquivo `.env` com:

```
MONGO_USER=seu_usuario
MONGO_PASS=sua_senha
MONGO_CLUSTER=seu_cluster
```

---

### 3. Rode o pipeline

**Extração do MongoDB:**

```bash
python extract_and_save_data.py
```

**Transformação:**

```bash
python transform_data.py
```

**Carga no MySQL:**

```bash
python save_data_mysql.py
```

---

## 📝 Observações

- Certifique-se de ter as tabelas criadas no MySQL:
  - `tb_produtos_2021_em_diante`
  - `tb_Livros`
- O script de carga gera SQL dinâmico conforme as colunas do DataFrame.

---

## 📑 Licença

Projeto acadêmico / experimental – sem licença comercial definida.
