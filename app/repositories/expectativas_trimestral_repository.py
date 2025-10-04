from pymongo import MongoClient

class ExpectativasTrimestralRepository:

    def __init__(self, mongo_uri, mongo_db):
        self.client = MongoClient(mongo_uri)
        self.collection = self.client[mongo_db]["expectativas_trimestral"]

    def insert(self, expectativa_trimestral):
        self.collection.insert_one(expectativa_trimestral.to_dict())
