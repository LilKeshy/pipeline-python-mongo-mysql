# pipeline-python-mongo-mysql

Projeto em Python para pipeline de dados, integrando MongoDB Atlas, transformação de dados e armazenamento final em MySQL e CSV.

## 🚀 Objetivo

- Extrair dados de APIs ou arquivos CSV
- Armazenar dados no MongoDB Atlas
- Transformar dados filtrando:
  - **Apenas produtos comprados a partir de 2021**
  - **Apenas livros**
- Salvar dados transformados em CSV
- Salvar dados transformados no MySQL

## 🗂 Estrutura do Projeto

pipeline-python-mongo-mysql/
├── notebooks/
│ ├── extract_and_save_data.ipynb
│ ├── save_data_mysql.ipynb
│ ├── transform_data.ipynb
│ └── .env
├── scripts/
│ ├── extract_and_save_data.py
│ └── transform_data.py
├── data/
│ ├── produtos_2021_em_diante.csv
│ └── livros.csv
├── venv/
├── .gitignore
├── README.md
└── requirements.txt