import json

class ChangeData:
    def __init__(self, **kwargs):
        self.firstname = 'Octav' if 'firstname' not in kwargs.keys() else kwargs.get('firstname')
        self.lastname = 'Marango' if 'lastname' not in kwargs.keys() else kwargs.get('lastname')
        self.totalprice = 777 if 'totalprice' not in kwargs.keys() else kwargs.get('totalprice')
        self.depositpaid = False if 'depositpaid' not in kwargs.keys() else kwargs.get('depositpaid')
        self.bookingdates = {"checkin": "2030-01-01", "checkout": "2030-02-01"} if 'bookingdates'\
                                                                                   not in kwargs.keys() \
            else kwargs.get('bookingdates')
        self.additionalneeds = 'Changed' if 'additionalneeds' not in kwargs.keys() else kwargs.get('additionalneeds')


    def update_data(self, **kwargs):
        self.__dict__.update(**kwargs)
        return json.dumps(self.__dict__)

    def get_dict(self):
        return self.__dict__
