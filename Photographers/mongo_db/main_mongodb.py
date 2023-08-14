from users_collection import UsersCollection
from order_collection import OrdersCollection


if __name__ == "__main__":
    host = "localhost"
    port = 5432
    db_name = "serhi_db"

    users_collection = UsersCollection(host, port, db_name)
    orders_collection = OrdersCollection(host, port, db_name)

    user = users_collection.find_user_by_name("john_doe")
    print("User:", user)

    pending_orders = orders_collection.find_orders_by_status("pending")
    print("Pending Orders:", pending_orders)
