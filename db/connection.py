from pymongo import MongoClient
import sqlite3

client = MongoClient("mongodb://localhost:27017/")
db = client["rede_social"]

collection_publicacoes = db["publicacoes"]

sqlite_db_path = "db/rede_social.db"
conexao_sqlite = sqlite3.connect(sqlite_db_path)
cursor = conexao_sqlite.cursor()


def verifica_conexao_mongo():
    try:
        client.admin.command("ping")
        print("Conexão estabelecida com sucesso!")
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")


def verifica_conexao_sqlite():
    try:
        conexao_sqlite.execute("SELECT 1")
        print("Conexão estabelecida com sucesso!")
    except Exception as e:
        print(f"Erro ao conectar ao SQLite: {e}")

def cria_banco_de_dados():
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, senha TEXT)")
        print("Banco de dados criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar banco de dados: {e}")