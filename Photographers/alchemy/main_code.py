from Photographers.alchemy.product_repository import ProductRepository
from Photographers.alchemy.products import Products
from Photographers.alchemy.orders import Orders
from Photographers.alchemy.session_db import Session


product_repo = ProductRepository()


products_to_add = [
    Products(product_name='Banana', price=45),
    Products(product_name='Apple', price=30),
    Products(product_name='Orange', price=25),
    Products(product_name='Grapes', price=55),
    Products(product_name='Mango', price=50),
    Products(product_name='Watermelon', price=40)
]

for product in products_to_add:
    product_repo.insert_one(product)


orders_to_add = [
    Orders(product_id=1, quantity=2),
    Orders(product_id=2, quantity=3),
    Orders(product_id=3, quantity=1),
    Orders(product_id=4, quantity=4),
    Orders(product_id=5, quantity=2),
    Orders(product_id=6, quantity=3)
]

for order in orders_to_add:
    product_repo.insert_one(order)

products_alias = session.query(Products).alias('p')
orders_alias = session.query(Orders).alias('o')

result = session.query(
    products_alias.c.product_name,
    products_alias.c.price,
    orders_alias.c.quantity,
    (products_alias.c.price * orders_alias.c.quantity).label('total_price')
).join(orders_alias, products_alias.c.id == orders_alias.c.product_id).all()

for row in result:
    product_name = row.product_name
    price = row.price
    quantity = row.quantity
    total_price = row.total_price
    print(f"{product_name}, Price: {price}, Quantity: {quantity}, Total Price: {total_price}")
