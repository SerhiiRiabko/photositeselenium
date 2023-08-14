from basemongodb import BaseMongo


class UsersCollection(BaseMongo):
    def __init__(self, host, port, db_name):
        super().__init__(host, port, db_name, "users")

    def find_user_by_name(self, username):
        query = {"username": username}
        return self.find_one(query)
