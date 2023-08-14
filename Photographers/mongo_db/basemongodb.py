from pymongo import MongoClient


class BaseMongo:
    def __init__(self, host, port, db_name):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]

    def insert_one(self, collection_name, document):
        collection = self.db[collection_name]
        result = collection.insert_one(document)
        return result.inserted_id

    def insert_many(self, collection_name, documents):
        collection = self.db[collection_name]
        result = collection.insert_many(documents)
        return result.inserted_ids

    def find_one(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find_one(query)

    def find(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find(query)