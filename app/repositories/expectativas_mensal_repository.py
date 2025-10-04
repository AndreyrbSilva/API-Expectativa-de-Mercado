from pymongo import MongoClient

class ExpectativasMensalRepository:
    
    def __init__(self, mongo_uri, mongo_db):
        self.cliente = MongoClient(mongo_uri)
        self.collection = self.cliente[mongo_db]['expectativas_mensal']
        
    def insert(self, expectativa_mensal):
        self.collection.insert_one(expectativa_mensal.to_dict())
