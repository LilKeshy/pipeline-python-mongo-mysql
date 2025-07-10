import pandas as pd
import mysql.connector


class MySQLConnector:
    def __init__(self, host, user, password, database):
        self.cnx = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.cnx.cursor()

    def insert_data(self, table_name, df):
        """
        Insere dados dinamicamente no MySQL.
        """
        cols = ", ".join([f"`{c}`" for c in df.columns])
        placeholders = ", ".join(["%s"] * len(df.columns))
        sql = f"""
            INSERT INTO {table_name}
            ({cols}) VALUES ({placeholders})
        """

        lista_dados = [tuple(row) for _, row in df.iterrows()]
        self.cursor.executemany(sql, lista_dados)
        self.cnx.commit()
        print(f"✔ {len(df)} registros inseridos na tabela {table_name}.")

    def close(self):
        self.cursor.close()
        self.cnx.close()


class BaseETL:
    """
    Classe base para ETLs genéricos.
    """
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None

    def load_csv(self):
        self.df = pd.read_csv(self.csv_path)
        # Limpa espaços em nomes das colunas
        self.df.columns = (
            self.df.columns
            .str.strip()
            .str.replace("\u00a0", " ", regex=False)
        )
        # Remove Unnamed se existir
        if "Unnamed: 0" in self.df.columns:
            self.df = self.df.drop(columns=["Unnamed: 0"])

    def rename_columns(self, rename_dict):
        self.df = self.df.rename(columns=rename_dict)

    def convert_date(self, date_columns):
        for col in date_columns:
            if col in self.df.columns:
                self.df[col] = pd.to_datetime(self.df[col]).dt.date


class ProdutoETL(BaseETL):
    def __init__(self, csv_path):
        super().__init__(csv_path)

    def process(self):
        self.load_csv()

        # Renomeia _id → id
        if "_id" in self.df.columns:
            self.df = self.df.rename(columns={"_id": "id"})

        # Converte datas
        self.convert_date(["Data da Compra"])

        # Faz renomeação das colunas
        self.rename_columns({
            "id": "id",
            "Produto": "produto",
            "Categoria do Produto": "categoria_produto",
            "Preço": "preco",
            "Frete": "frete",
            "Data da Compra": "Data_Compra",
            "Vendedor": "vendedor",
            "Local da compra": "local_compra",
            "Avaliação da compra": "Avaliacao_Compra",
            "Tipo de pagamento": "Tipo_Pagamento",
            "Quantidade de parcelas": "Qntd_Parcelas",
            "Latitude": "latitude",
            "Longitude": "longitude"
        })

        print(f"✔ ProdutoETL pronto, shape = {self.df.shape}")


class LivroETL(BaseETL):
    def __init__(self, csv_path):
        super().__init__(csv_path)

    def process(self):
        self.load_csv()

        # Converte datas
        self.convert_date(["Data da Compra"])

        # Faz renomeação das colunas
        self.rename_columns({
            "_id": "id",
            "Produto": "produto",
            "Categoria do Produto": "categoria_produto",
            "Preço": "preco",
            "Frete": "frete",
            "Data da Compra": "Data_Compra",
            "Vendedor": "vendedor",
            "Local da compra": "local_compra",
            "Avaliação da compra": "Avaliacao_Compra",
            "Tipo de pagamento": "Tipo_Pagamento",
            "Quantidade de parcelas": "Qntd_Parcelas",
            "Latitude": "latitude",
            "Longitude": "longitude"
        })

        print(f"✔ LivroETL pronto, shape = {self.df.shape}")


if __name__ == "__main__":
    # Configuração MySQL
    db_conf = {
        "host": "localhost",
        "user": "seu_usuario",
        "password": "sua_senha",
        "database": "dbprodutos"
    }

    # Processa produtos
    produtos_etl = ProdutoETL("../data/tabela_2021_em_diante.csv")
    produtos_etl.process()

    conn = MySQLConnector(**db_conf)
    conn.insert_data("tb_produtos_2021_em_diante", produtos_etl.df)
    conn.close()

    # Processa livros
    livros_etl = LivroETL("../data/tabela_Livros.csv")
    livros_etl.process()

    conn = MySQLConnector(**db_conf)
    conn.insert_data("tb_Livros", livros_etl.df)
    conn.close()
