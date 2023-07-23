import json


class Booking:
    def __init__(self, **kwargs):
        self.firstname = 'Mary' if 'firstname' not in kwargs.keys() else kwargs.get('firstname')
        self.lastname = 'Brown' if 'firstname' not in kwargs.keys() else kwargs.get('lastname')
        self.totalprice = '588' if 'firstname' not in kwargs.keys() else kwargs.get('totalprice')
        self.depositpaid = True if 'firstname' not in kwargs.keys() else kwargs.get('depositpaid')

    def update_data(self, **kwargs):
        self.__init__.update(**kwargs)

    def get_json(self):
        return json.dumps(self.__dict__)

    def get_dict(self):
        return self.__dict__
