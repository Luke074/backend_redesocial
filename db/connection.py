from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["rede_social"]
collection_publicacoes = db["publicacoes"]

print(collection_publicacoes.find_one())
