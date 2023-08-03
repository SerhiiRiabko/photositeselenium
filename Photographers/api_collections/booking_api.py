from Photographers.utilities.api_utilities.base_api import BaseAPI


class BookingAPI(BaseAPI):

    def __init__(self):
        super().__init__()

    def get_booking_by_id(self, booking_id, headers=None):
        response = self.get(f'/booking/{booking_id}', headers=headers)
        return response

    def create_booking(self, booking, headers=None):
        response = self.post('/booking', booking.get_dict(), headers=headers)
        return response

    def update_booking_by_id(self, booking_id, body, headers=None):
        if headers is None:
            headers = {'Cookie': 'token=abc123'}
        response = self.put(f'/booking/{booking_id}', body.get_dict(), headers=headers)
        return response
