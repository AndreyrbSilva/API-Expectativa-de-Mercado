from pymongo import MongoClient

class ExpectativaAnualRepositorio:
    
    def __init__(self, mongo_uri, mongo_db):
        self.cliente = MongoClient(mongo_uri)
        self.collection = self.cliente[mongo_db]['expectativa_anual']
        
    def insert(self, expectativa_anual):
        self.collection.insert_one(expectativa_anual.to_dict())