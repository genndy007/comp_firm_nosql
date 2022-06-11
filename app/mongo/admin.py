from app.mongo.collections import Customer, Supplier


class MongoAdmin:
    def __init__(self):
        self.customer = Customer()
        self.supplier = Supplier()
