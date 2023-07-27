import json


class Booking:
    def __init__(self, **kwargs):
        self.firstname = 'Octav' if 'firstname' not in kwargs.keys() else kwargs.get('firstname')
        self.lastname = 'Marango' if 'lastname' not in kwargs.keys() else kwargs.get('lastname')
        self.totalprice = '777' if 'totalprice' not in kwargs.keys() else kwargs.get('totalprice')
        self.depositpaid = True if 'depositpaid' not in kwargs.keys() else kwargs.get('depositpaid')
        self.bookingdates = '{"checkin" : "2018-01-01","checkout" : "2019-01-01"}' if 'bookingdates' not \
                                                                                      in kwargs.keys() \
            else kwargs.get('bookingdates')

    def update_data(self, **kwargs):
        self.__dict__.update(**kwargs)

    def get_json(self):
        return json.dumps(self.__dict__)

    def get_dict(self):
        return self.__dict__
