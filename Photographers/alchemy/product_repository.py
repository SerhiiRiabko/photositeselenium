from Photographers.alchemy.products import Products
from Photographers.alchemy.session_db import session


class ProductRepository:
    def __init__(self):
        self.__session = session

    def get_by_id(self, id_value: int):
        product = self.__session.get(Products, {'id': id_value})
        return product

    def get_all(self):
        all_products = self.__session.query(Products).all()

    def insert_one(self, product: Products):
        self.__session.add(product)
        self.__session.commit()

    def delete_user(self, product):
        self.__session.delete(product)
        self.__session.commit()
