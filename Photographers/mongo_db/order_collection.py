from basemongodb import BaseMongo


class OrdersCollection(BaseMongo):
    def __init__(self, host, port, db_name):
        super().__init__(host, port, db_name, "orders")

    def find_orders_by_status(self, status):
        query = {"status": status}
        return list(self.find(query))
