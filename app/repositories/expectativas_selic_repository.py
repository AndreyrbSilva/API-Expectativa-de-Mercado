from pymongo import MongoClient

class ExpectativasSelicRepository:

    def __init__(self, mongo_uri, mongo_db):
        self.client = MongoClient(mongo_uri)
        self.collection = self.client[mongo_db]["expectativas_selic"]

    def insert(self, expectativas_selic):
        self.collection.insert_one(expectativas_selic.to_dict())