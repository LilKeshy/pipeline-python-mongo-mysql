import pandas as pd
import os

class DataTransformer:
    def __init__(self, data_dir):
        """
        Classe responsável por transformar dados do pipeline.

        :param data_dir: Caminho onde estão os arquivos CSV de entrada e saída
        """
        self.data_dir = data_dir

    def load_csv(self, filename):
        """
        Carrega um arquivo CSV em um DataFrame.

        :param filename: Nome do arquivo CSV
        :return: DataFrame
        """
        path = os.path.join(self.data_dir, filename)
        return pd.read_csv(path)

    def filter_data(self, df, ano_col='ano_compra', categoria_col='categoria', ano_min=2021, categoria='Livros'):
        """
        Filtra os dados para compras a partir de 2021 e categoria Livros.

        :param df: DataFrame original
        :param ano_col: Coluna com o ano da compra
        :param categoria_col: Coluna com a categoria do produto
        :param ano_min: Ano mínimo
        :param categoria: Categoria desejada
        :return: DataFrame filtrado
        """
        df_filtrado = df[
            (df[ano_col] >= ano_min) &
            (df[categoria_col] == categoria)
        ]
        return df_filtrado

    def save_csv(self, df, filename):
        """
        Salva o DataFrame em CSV.

        :param df: DataFrame
        :param filename: Nome do arquivo CSV a salvar
        """
        path = os.path.join(self.data_dir, filename)
        df.to_csv(path, index=False)
        print(f"Arquivo salvo em {path}")

if __name__ == "__main__":
    # Caminho da pasta onde estão os CSVs
    DATA_DIR = "../data"  

    transformer = DataTransformer(DATA_DIR)

    # Carregar CSV de produtos
    df_produtos = transformer.load_csv("produtos_2021_em_diante.csv")

    # Filtrar dados: somente livros comprados a partir de 2021
    df_livros = transformer.filter_data(df_produtos)

    # Salvar resultado em CSV
    transformer.save_csv(df_livros, "livros_filtrados.csv")
