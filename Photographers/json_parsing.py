import pytest
import json


class DataOrder:
    def __init__(self):
        self.id = 12345
        self.status = True
        self.owner = None

    def get_dict(self):
        return self.__dict__

    def get_json(self):
        return json.dumps(self.get_dict())

    def update_class(self, **kwargs):
        self.__dict__.update(**kwargs)


data_order = DataOrder().get_json()
new = json.loads(data_order)
