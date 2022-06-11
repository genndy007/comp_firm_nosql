from pymongo import MongoClient
from pymongo.collection import Collection as MongoCollection
from app.mongo.secrets import get_mongo_conn_url
from app.mongo import DB_NAME, COL_CUSTOMERS, COL_SUPPLIERS


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class Mongo:
    def __init__(self, db_name=DB_NAME):
        conn_string = get_mongo_conn_url()
        self.client = MongoClient(conn_string)
        self.db = self.client[db_name]

    def all_collections(self):
        return self.db.list_collection_names()


class Collection:
    def __init__(self, col_name):
        self.collection: MongoCollection = Mongo().db[col_name]

    def insert_one(self, document) -> "ObjectId":
        item_id = self.collection.insert_one(document).inserted_id
        return item_id

    def find(self, params=None) -> list[dict]:
        if params is None:
            params = {}
        return list(self.collection.find(params))

    def find_one(self, params) -> dict:
        return self.collection.find_one(params)

    def count_documents(self, params=None) -> int:
        if params is None:
            params = {}
        return self.collection.count_documents(params)

    def delete_many(self, params=None) -> int:
        if params is None:
            params = {}
        d = self.collection.delete_many(params)
        return d.deleted_count


class Customer(Collection):
    def __init__(self):
        super().__init__(COL_CUSTOMERS)


class Supplier(Collection):
    def __init__(self):
        super().__init__(COL_SUPPLIERS)
