from pymongo import MongoClient


class BaseMongo:
    def __init__(self, host, port, db_name, collection_name):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_one(self, document):
        result = self.collection.insert_one(document)
        return result.inserted_id

    def insert_many(self, documents):
        result = self.collection.insert_many(documents)
        return result.inserted_ids

    def find_one(self, query):
        return self.collection.find_one(query)

    def find(self, query):
        return self.collection.find(query)
