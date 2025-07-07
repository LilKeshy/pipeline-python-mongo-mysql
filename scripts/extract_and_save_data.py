from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class MongoConnector:
    """
    Classe para gerenciar conexão com o MongoDB Atlas.
    """

    def __init__(self, env_path="../notebooks/.env"):
        """
        Inicializa o conector e carrega variáveis do .env.

        :param env_path: caminho relativo ao arquivo .env
        """
        self.load_env(env_path)
        self.client = None

    def load_env(self, env_path):
        """
        Carrega variáveis de ambiente do arquivo .env
        """
        # Calcula o caminho absoluto baseado no local deste arquivo .py
        abs_path = os.path.join(os.path.dirname(__file__), env_path)
        load_dotenv(dotenv_path=abs_path)

        self.mongo_user = os.getenv("MONGO_USER")
        self.mongo_pass = os.getenv("MONGO_PASS")
        self.mongo_cluster = os.getenv("MONGO_CLUSTER")

        if None in (self.mongo_user, self.mongo_pass, self.mongo_cluster):
            print("⚠️ Erro: Variáveis de ambiente não definidas!")
            exit(1)

    def build_uri(self):
        """
        Monta a URI de conexão ao MongoDB Atlas
        """
        uri = (
            f"mongodb+srv://{self.mongo_user}:{self.mongo_pass}"
            f"@{self.mongo_cluster}/?retryWrites=true&w=majority&appName=Cluster-pipeline"
        )
        return uri

    def connect(self):
        """
        Realiza a conexão ao MongoDB Atlas.
        """
        uri = self.build_uri()
        try:
            self.client = MongoClient(uri, server_api=ServerApi('1'))
            self.client.admin.command('ping')
            print("✅ Conectado ao MongoDB Atlas!")
        except Exception as e:
            print("Erro ao conectar:", e)

    def get_client(self):
        """
        Retorna o objeto client conectado.
        """
        if self.client is None:
            self.connect()
        return self.client

# -----------------------------
# Exemplo de uso standalone
# -----------------------------
if __name__ == "__main__":
    connector = MongoConnector(env_path="../notebooks/.env")
    connector.connect()

    # Teste: listar bancos
    client = connector.get_client()
    print("📂 Databases:", client.list_database_names())
