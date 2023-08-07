from Photographers.alchemy.orders import Orders
from Photographers.alchemy.session_db import session


class OrderRepository:
    def __init__(self):
        self.__session = session

    def get_by_id(self, id_value: int):
        order = self.__session.get(Orders, id_value)
        return order

    def get_all(self):
        all_orders = self.__session.query(Orders).all()
        return all_orders

    def insert_one(self, order: Orders):
        self.__session.add(order)
        self.__session.commit()

    def delete_order(self, order: Orders):
        self.__session.delete(order)
        self.__session.commit()
